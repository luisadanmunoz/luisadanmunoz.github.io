---
title: "Automation Accounts – Runbook"
date: 2025-01-10 10:00:00 +0100
categories: [Resources, Automation]
tags: [automation, automation-accounts, runbook, role_assignments, schedule]
description: "Uso de Azure Automation Accounts para la ejecución de Runbooks PowerShell con identidad administrada, controlados por schedules y RBAC."
mermaid: true
---


Contenido de Automation Accounts – Runbook.
## 1. Resumen

- **Objetivo**: Utilizar Azure Automation Account para ejecutar Runbooks PowerShell que gestionan el arranque y parada de máquinas virtuales, controlados mediante schedules y filtrados por tags.

- **Dependencias**: [RG], [role_assignments], [vnet], [subnet], [private_dns_zone]


> ⚠️ **Warning**
>
> public_network_access_enabled = false implica que debes validar conectividad privada (Private Endpoint/DNS) para operar según el diseño.
{: .prompt-warning }

> 💡 **Tip**
>
> Los vm_start_schedule_start_time deben ser fechas futuras en formato ISO8601 (en el código: 2026-01-15T...+01:00) y con vm_start_schedule_timezone = Europe/Madrid.
{: .prompt-tip }

> 💡 **Tip**
>
>Microsoft recomienda el uso de Managed Identities frente a credenciales embebidas para la ejecución de Runbooks.
{: .prompt-tip }

## 2. Arquitectura

> ℹ️ **Info**
>
> El Automation Account se despliega con System Assigned Managed Identity, acceso público deshabilitado y resolución de nombres mediante Private DNS Zone.
{: .prompt-info }


```mermaid
flowchart LR
role_assignments --> automation_account
automation_account --> identity_type
automation_account --> private_dns_zone
automation_account --> subnet
automation_runbooks --> automation_account
automation_schedule --> automation_account
automation_schedule --> automation_runbooks
vnet --> subnet
subnet --> private_dns_zone
private_dns_zone --> virtual_network_link
private_dns_zone --> private_endpoint
Runbook --> AzureResource[(VMs)]
Runbook --> automation_account
```

## 3. Diseño

- Naming: aa
- SKU: Automation Account: Basic (suficiente para ejecución de Runbooks sin características avanzadas como Update Management).
- Terraform: <a href="https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/automation_account" target="_blank" rel="noopener noreferrer">Azure Automation</a>
- Cost: Azure Automation se factura por tiempo de ejecución del job y número de jobs según el modelo vigente de Microsoft.
- Red: private endpoint
- Hybrid: No se utiliza Hybrid Runbook Worker en este diseño.

## 4. Implementación (IaC)
### Terraform
```terraform
resource "azurerm_automation_account" "this" {
  name                          = var.automation_account_name
  location                      = var.location
  resource_group_name           = var.resource_group_name
  sku_name                      = var.sku_name
  public_network_access_enabled = var.public_network_access_enabled

  identity {
    type = var.identity_type
  }
  tags = var.tags
}
#############################################################################
# PRIVATE ENDPOINT
#############################################################################
resource "azurerm_private_endpoint" "private_endpoint" {
  name                = "pe-${var.automation_account_name}"
  location            = azurerm_automation_account.this.location
  resource_group_name = azurerm_automation_account.this.resource_group_name
  subnet_id           = var.subnet_id

  private_service_connection {
    name                           = "psc-${var.automation_account_name}"
    private_connection_resource_id = azurerm_automation_account.this.id
    subresource_names              = ["Webhook"]
    is_manual_connection           = false
  }
 
  private_dns_zone_group {
    name                 = "pdnszg-${var.automation_account_name}"
    private_dns_zone_ids = [var.private_dns_zone_ids]
  }
    tags = var.tags
}
```
## 5. Administración (CLI Azure)
### Powershell
```powershell
# Requiere Azure CLI instalado y sesión iniciada
az login
az account show -o table

# (Opcional) Fijar suscripción
az account set --subscription "<SUBSCRIPTION_ID>"

# Variables de ejemplo (ajústalas a tu entorno)
$rg = "rg-lab-01"
$aa = "aa-prod"

# -------------------------------
# AUTOMATION ACCOUNT (consultas)
# -------------------------------

# Ver detalles del Automation Account
az automation account show `
  --resource-group $rg `
  --name $aa `
  -o jsonc

# Listar Automation Accounts en un RG
az automation account list `
  --resource-group $rg `
  -o table

# Listar Runbooks del Automation Account
az automation runbook list `
  --resource-group $rg `
  --automation-account-name $aa `
  -o table

# Ver detalles de un Runbook
az automation runbook show `
  --resource-group $rg `
  --automation-account-name $aa `
  --name "rb_vm_start" `
  -o jsonc

# -------------------------------
# SCHEDULES + VINCULOS (job schedules)
# -------------------------------

# Listar schedules del Automation Account
az automation schedule list `
  --resource-group $rg `
  --automation-account-name $aa `
  -o table

# Ver un schedule concreto
az automation schedule show `
  --resource-group $rg `
  --automation-account-name $aa `
  --name "sch-vm-start-daily-0800" `
  -o jsonc

# Listar vínculos Runbook <-> Schedule (Job Schedules)
az automation job-schedule list `
  --resource-group $rg `
  --automation-account-name $aa `
  -o table

# -------------------------------
# EJECUCION DE RUNBOOKS (jobs)
# -------------------------------

# Iniciar un Runbook (crea un Job)
# Nota: si tu runbook requiere parámetros, añádelos con --parameters
az automation runbook start `
  --resource-group $rg `
  --automation-account-name $aa `
  --name "rb_vm_start"

# Listar jobs recientes del Automation Account
az automation job list `
  --resource-group $rg `
  --automation-account-name $aa `
  -o table

# Ver detalle de un job
az automation job show `
  --resource-group $rg `
  --automation-account-name $aa `
  --name "<JOB_ID>" `
  -o jsonc

# Obtener el output del job
az automation job output show `
  --resource-group $rg `
  --automation-account-name $aa `
  --name "<JOB_ID>" `
  -o jsonc

# Obtener los streams (Verbose/Warning/Error/Progress) del job
az automation job stream list `
  --resource-group $rg `
  --automation-account-name $aa `
  --job-id "<JOB_ID>" `
  -o table

# Ver un stream concreto
az automation job stream show `
  --resource-group $rg `
  --automation-account-name $aa `
  --job-id "<JOB_ID>" `
  --stream-id "<STREAM_ID>" `
  -o jsonc

# -------------------------------
# IDENTIDAD (Managed Identity) + RBAC
# -------------------------------

# Ver la identidad del Automation Account (principalId / tenantId)
az automation account show `
  --resource-group $rg `
  --name $aa `
  --query "identity" `
  -o jsonc

# Listar role assignments (RBAC) asignados a la Managed Identity en un scope
# (ejemplo: RG)
$sub = "<SUBSCRIPTION_ID>"
$scopeRg = "/subscriptions/$sub/resourceGroups/$rg"

# Sustituye <PRINCIPAL_ID> por identity.principalId del Automation Account
az role assignment list `
  --assignee-object-id "<PRINCIPAL_ID>" `
  --scope $scopeRg `
  -o table

# Crear una asignación de rol (ejemplo)
az role assignment create `
  --assignee-object-id "<PRINCIPAL_ID>" `
  --assignee-principal-type ServicePrincipal `
  --role "Virtual Machine Contributor" `
  --scope "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RG_NAME>"

# -------------------------------
# RED PRIVADA (Private DNS Zone - consultas típicas)
# -------------------------------

# Listar Private DNS Zones en un RG
az network private-dns zone list `
  --resource-group $rg `
  -o table

# Ver una Private DNS Zone concreta
az network private-dns zone show `
  --resource-group $rg `
  --name "privatelink.azure-automation.net" `
  -o jsonc

# Listar Virtual Network Links de una Private DNS Zone
az network private-dns link vnet list `
  --resource-group $rg `
  --zone-name "privatelink.azure-automation.net" `
  -o table

# Listar Private Endpoints (si aplica en tu despliegue)
az network private-endpoint list `
  --resource-group $rg `
  -o table

```
## 6. Referencias


### Diagrama de Arquitectura

```mermaid
flowchart TB
    subgraph Azure["Azure Subscription"]
        subgraph RG["Resource Group"]
            AA["Automation Account<br/>(Managed Identity)"]
            PE["Private Endpoint"]
            
            subgraph Runbooks["Runbooks"]
                RB1["rb_vm_start<br/>(PowerShell)"]
                RB2["rb_vm_stop<br/>(PowerShell)"]
            end
            
            subgraph Schedules["Schedules"]
                SCH1["sch-vm-start<br/>(Daily 08:00)"]
                SCH2["sch-vm-stop<br/>(Daily 20:00)"]
            end
        end
        
        subgraph Network["Virtual Network"]
            SUBNET["Subnet"]
            DNS["Private DNS Zone<br/>privatelink.azure-automation.net"]
        end
        
        subgraph Resources["Azure Resources"]
            VM1["VM 1<br/>(env=prod)"]
            VM2["VM 2<br/>(env=prod)"]
            VM3["VM 3<br/>(env=dev)"]
        end
    end
    
    SCH1 -.Trigger.-> RB1
    SCH2 -.Trigger.-> RB2
    RB1 --> AA
    RB2 --> AA
    AA -->|RBAC: VM Contributor| Resources
    AA <-->|Private| PE
    PE --> SUBNET
    SUBNET --> DNS
    
    style AA fill:#0078d4,color:#fff
    style PE fill:#50e6ff,color:#000
    style DNS fill:#50e6ff,color:#000
```