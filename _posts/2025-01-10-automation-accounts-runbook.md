---
title: "Automation Accounts – Runbook"
date: 2025-01-10 10:00:00 +0100
categories: [Resources, Automation]
tags: [automation, automation-accounts, runbook]
description: ""
mermaid: true
---


Contenido de Automation Accounts – Runbook.
## 1. Resumen

- **Objetivo**:
- **Dependencias**:


> [!tip] Notas Importantes

## 2. Arquitectura

```mermaid
flowchart LR
User --> AzurePortal
AzurePortal --> FW
FW --> SubnetAZ
SubnetAZ --> AutomationAccount
AutomationAccount --> Runbook
Runbook --> AzureResources[(VMs, SQL, Key Vault, etc)]
```

## 3. Diseño

- Naming:
- SKU:
- Terraform: 
- Cost:
- Red: 
- Hybrid:

## 4. Implementación (IaC)
### Terraform
```terraform

```
## 5. Administración (CLI Azure)
### Powershell
```powershell

```
## 6. Referencias