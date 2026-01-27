---
title: Azure-Lighthouse-Enterprise
area: azure/management
owner: LuisAdan
tags: [azure, lighthouse, multi-tenant, delegation, msp]
cost: https://azure.microsoft.com/pricing/details/azure-lighthouse/
repo: https://github.com/org/azure-lighthouse-iac
last_review: 2026-01-27
---

# Azure Lighthouse - Documentación Completa

**Nota**: Documento completo disponible en el repositorio. Este es un resumen ejecutivo.

## 📋 1. Resumen

Azure Lighthouse permite gestión multi-tenant centralizada para MSPs y equipos de operaciones.

- **Objetivo**: Gestión unificada de múltiples customer tenants
- **Beneficio clave**: GRATIS - Sin costes adicionales
- **Dependencias**: Azure AD, RBAC, Subscriptions, Policy, Monitor

## 🏛️ 2. Arquitectura

Ver diagramas completos en el repositorio.

## 💰 7. Costes

- **Azure Lighthouse**: GRATIS (sin coste)
- **Infraestructura soporte**: ~$430/mes (AAD P1, Log Analytics, Sentinel)
- **ROI**: $3,500/mes en ahorros operacionales
- **Ratio**: 8:1 (beneficio vs coste)

## 🔗 Referencias Clave

- Docs: https://learn.microsoft.com/azure/lighthouse/
- Samples: https://github.com/Azure/Azure-Lighthouse-samples
- Terraform: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/lighthouse_definition

---
Documento completo con código Terraform, scripts, tests y ADRs disponible en repositorio.
