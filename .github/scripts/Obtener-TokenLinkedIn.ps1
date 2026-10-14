<#
.SYNOPSIS
  Obtiene un token de acceso de LinkedIn (60 días) para publicar en tu perfil desde GitHub Actions.

.DESCRIPTION
  Hace el flujo OAuth 2.0 de código de autorización (3-legged) en tu equipo:
    1. Abre el navegador para que autorices la app (scopes: openid profile w_member_social).
    2. Recoge el código en http://localhost:8765/callback.
    3. Lo canjea por el token y obtiene tu identificador de persona (urn:li:person:...).
    4. Con -GuardarEnGitHub, guarda los secretos en el repositorio con GitHub CLI (gh).

  La URL de redirección debe estar registrada en la app de LinkedIn
  (Developer Portal → tu app → Auth → Authorized redirect URLs).

  Documentación:
    https://learn.microsoft.com/linkedin/shared/authentication/authorization-code-flow
    https://learn.microsoft.com/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2

.EXAMPLE
  ./.github/scripts/Obtener-TokenLinkedIn.ps1 -ClientId '86abc123' -GuardarEnGitHub
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)] [string] $ClientId,
    [securestring] $ClientSecret,
    [string] $RedirectUri = 'http://localhost:8765/callback',
    [string] $Repositorio = 'luisadanmunoz/luisadanmunoz.github.io',
    [switch] $GuardarEnGitHub
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Web

if (-not $ClientSecret) {
    $ClientSecret = Read-Host -Prompt 'Client Secret de la app de LinkedIn' -AsSecureString
}
$secretoPlano = [System.Net.NetworkCredential]::new('', $ClientSecret).Password

$state  = [guid]::NewGuid().ToString('N')
$scopes = 'openid profile w_member_social'
$authUrl = 'https://www.linkedin.com/oauth/v2/authorization?response_type=code' +
    "&client_id=$([uri]::EscapeDataString($ClientId))" +
    "&redirect_uri=$([uri]::EscapeDataString($RedirectUri))" +
    "&state=$state" +
    "&scope=$([uri]::EscapeDataString($scopes))"

# Escucha local para recoger el código de autorización
$prefijo  = ([uri]$RedirectUri).GetLeftPart([System.UriPartial]::Authority) + '/'
$listener = [System.Net.HttpListener]::new()
$listener.Prefixes.Add($prefijo)
$listener.Start()
try {
    Write-Host 'Abriendo el navegador para autorizar la app en LinkedIn...'
    Start-Process $authUrl
    $ctx   = $listener.GetContext()
    $query = [System.Web.HttpUtility]::ParseQueryString($ctx.Request.Url.Query)
    $html  = '<html><body style="font-family:sans-serif"><h2>Listo. Ya puedes cerrar esta pestaña.</h2></body></html>'
    $bytes = [Text.Encoding]::UTF8.GetBytes($html)
    $ctx.Response.ContentType = 'text/html; charset=utf-8'
    $ctx.Response.OutputStream.Write($bytes, 0, $bytes.Length)
    $ctx.Response.Close()
}
finally {
    $listener.Stop()
}

if ($query['error']) { throw "LinkedIn devolvió un error: $($query['error']) - $($query['error_description'])" }
if ($query['state'] -ne $state) { throw 'El parámetro state no coincide. Repite el proceso.' }
$code = $query['code']

# Canje del código por el token
$token = Invoke-RestMethod -Method Post -Uri 'https://www.linkedin.com/oauth/v2/accessToken' `
    -ContentType 'application/x-www-form-urlencoded' -Body @{
        grant_type    = 'authorization_code'
        code          = $code
        redirect_uri  = $RedirectUri
        client_id     = $ClientId
        client_secret = $secretoPlano
    }

$caduca = (Get-Date).AddSeconds([int]$token.expires_in)

# Identificador de persona para el campo author de los posts
$yo = Invoke-RestMethod -Uri 'https://api.linkedin.com/v2/userinfo' -Headers @{ Authorization = "Bearer $($token.access_token)" }
$personUrn = "urn:li:person:$($yo.sub)"

Write-Host ''
Write-Host "Token obtenido para $($yo.name). Caduca el $($caduca.ToString('dd/MM/yyyy'))." -ForegroundColor Green
Write-Host "Person URN: $personUrn"

if ($GuardarEnGitHub) {
    if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw 'No encuentro GitHub CLI (gh). Instálalo con: winget install GitHub.cli' }
    $token.access_token | gh secret set LINKEDIN_ACCESS_TOKEN -R $Repositorio
    $personUrn          | gh secret set LINKEDIN_PERSON_URN   -R $Repositorio
    $ClientId           | gh secret set LINKEDIN_CLIENT_ID    -R $Repositorio
    $secretoPlano       | gh secret set LINKEDIN_CLIENT_SECRET -R $Repositorio
    Write-Host "Secretos guardados en $Repositorio." -ForegroundColor Green
}
else {
    Set-Clipboard -Value $token.access_token
    Write-Host 'El token está en el portapapeles. Guárdalo como secreto LINKEDIN_ACCESS_TOKEN en GitHub (Settings → Secrets and variables → Actions).'
}
