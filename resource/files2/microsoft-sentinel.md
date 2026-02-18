# Microsoft Sentinel (SIEM/SOAR)

## 📋 Características

**Microsoft Sentinel** es cloud-native SIEM/SOAR. Security analytics, threat intelligence, automated response. Formerly Azure Sentinel.

### Pricing

**Data Ingestion:**
- Pay-as-you-go: $2.76/GB
- Commitment Tiers: $2.20-2.46/GB (100-5000 GB/día)

**Data Retention:**
- First 90 days: FREE
- 90+ days: $0.12/GB/mes

**Example:**
```
200 GB/día ingestion:
Commitment 200 GB: 200 × 30 × $2.30 = $13,800/mes

With retention 365 días:
Extra 275 días × 6 TB = ~1,650 TB × $0.12 = $19,800/mes
Total: ~$33,600/mes
```

**Log Analytics included** - Sentinel pricing covers LA ingestion

---

## 🏆 Best Practices

### Data Connectors
- ✅ **Microsoft 365**: Azure AD, Exchange, SharePoint
- ✅ **Azure services**: Activity logs, NSG, Firewall
- ✅ **Security solutions**: Microsoft Defender, third-party
- ✅ **Syslog/CEF**: On-prem devices, firewalls
- ✅ **Custom**: REST API, Logstash

### Analytics Rules
- ✅ **Scheduled**: Query-based detection
- ✅ **Microsoft**: Built-in templates
- ✅ **ML Behavioral**: Anomaly detection
- ✅ **Threat Intelligence**: IoC matching
- ✅ **Fusion**: Multi-stage attack detection

### Incident Management
- ✅ **Triage**: Assign, investigate, close
- ✅ **Investigation graph**: Visual timeline
- ✅ **Entities**: IP, user, host correlation
- ✅ **MITRE ATT&CK**: Framework mapping

### Automation (SOAR)
- ✅ **Playbooks**: Logic Apps integration
- ✅ **Automation rules**: Auto-response
- ✅ **Watchlists**: Allow/deny lists
- ✅ **Notebooks**: Jupyter for hunting

### Threat Hunting
- ✅ **KQL queries**: Advanced hunting
- ✅ **Hunting queries**: Pre-built templates
- ✅ **Bookmarks**: Save interesting findings
- ✅ **Livestream**: Real-time monitoring

### Cost Optimization
- ✅ **Commitment tiers**: 100+ GB/día
- ✅ **Data filtering**: Ingest only necessary
- ✅ **Archive**: Long-term to Storage
- ✅ **Health monitoring**: Avoid duplicates

---

## ⚠️ Limitaciones

- Requires Log Analytics workspace
- Retention: Max 730 días in workspace
- Query timeout: 10 minutes
- Some connectors: Premium licenses needed

---

## ✅ Checklist

- [ ] Log Analytics workspace created
- [ ] Sentinel enabled
- [ ] Data connectors configured
- [ ] Analytics rules enabled
- [ ] Automation rules/playbooks created
- [ ] Threat intelligence integrated
- [ ] UEBA enabled
- [ ] Watchlists configured
- [ ] Hunting queries deployed
- [ ] Incident response process defined
- [ ] Team trained
