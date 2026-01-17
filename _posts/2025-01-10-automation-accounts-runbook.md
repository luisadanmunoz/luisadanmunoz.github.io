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
role_assignments["Role Assignments (RBAC)"] --> automation_account["Automation Account"]
automation_account --> identity_type["Managed Identity (System/User Assigned)"]
automation_account --> private_dns_zone["Private DNS Zone"]
automation_account --> subnet["Subnet"]
automation_runbooks["Runbooks"] --> automation_account
automation_schedule["Schedules"] --> automation_account
automation_schedule --> automation_runbooks
vnet["VNet"] --> subnet
subnet --> private_dns_zone
private_dns_zone --> virtual_network_link["VNet Link"]
private_dns_zone --> private_endpoint["Private Endpoint"]
Runbook["Runbook Execution"] --> AzureResource["Azure Resources (VMs)"]

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