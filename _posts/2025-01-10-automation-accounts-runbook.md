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
- **Dependencias**: [RG], [role_assignments], [vnet], [subnet], [private_dns_zone]


> [!tip] Notas Importantes

## 2. Arquitectura

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