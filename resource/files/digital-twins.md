# Azure Digital Twins

## 📋 Características

**Digital Twins** es IoT platform for creating digital models of physical environments. Twin graph, spatial intelligence, 3D visualization.

### Pricing

**Operations:**
- Twin API: $2.50/million operations
- Query: $0.50/million query units
- Event Routes: FREE

**Data egress:** Standard bandwidth pricing

**Example:**
```
Monthly usage:
10M twin updates: 10 × $2.50 = $25
50M queries (1 QU each): 50 × $0.50 = $25
Total: ~$50/mes
```

**No base cost** - pay per use

---

## 🏆 Best Practices

### Modeling
- ✅ **DTDL models**: Digital Twin Definition Language
- ✅ **Ontologies**: Reusable industry models
- ✅ **Relationships**: Twin graph connections
- ✅ **Properties**: State representation

### Integration
- ✅ **IoT Hub**: Device data ingestion
- ✅ **Event Grid**: Event routing
- ✅ **Functions**: Business logic
- ✅ **Time Series Insights**: Historical data
- ✅ **SignalR**: Real-time visualization

### Data Flow
- ✅ **Ingress**: IoT Hub → Functions → Digital Twins
- ✅ **Processing**: Azure Functions compute
- ✅ **Egress**: Event Routes → downstream services
- ✅ **Storage**: ADX, Time Series Insights

### Queries
- ✅ **Graph queries**: Traverse relationships
- ✅ **Property filters**: Query by state
- ✅ **Projections**: Select specific fields
- ✅ **JOIN**: Multi-twin queries

### Visualization
- ✅ **3D Scenes**: Azure Digital Twins Explorer
- ✅ **Custom apps**: SDK integration
- ✅ **Power BI**: Analytics dashboards
- ✅ **Real-time**: SignalR integration

---

## ⚠️ Limitaciones

- Max twins: Millions (soft limit)
- Query timeout: 30 seconds
- Model size: 1 MB max
- Relationship depth: Unbounded (performance impact)

---

## ✅ Checklist

- [ ] Digital Twins instance created
- [ ] Models uploaded (DTDL)
- [ ] Twins created
- [ ] Relationships defined
- [ ] IoT Hub integrated
- [ ] Event Routes configured
- [ ] Azure Functions deployed
- [ ] Queries tested
- [ ] Visualization configured
- [ ] Monitoring enabled
