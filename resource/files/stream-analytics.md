# Azure Stream Analytics

## 📋 Características

**Stream Analytics** es real-time analytics service. Process streaming data from IoT, logs, events. SQL-like queries, temporal operators, windowing.

### Pricing

**Streaming Units (SU):**
- 1 SU = 1 MB/s throughput capacity
- $0.11/SU/hour (~$80/SU/mes 24/7)

**Example:**
```
3 SU job running 24/7:
3 × $0.11 × 730 hours = $240.90/mes

Intermittent job (8h/day):
3 × $0.11 × 240 hours = $79.20/mes
```

**No charge when stopped**

---

## 🏆 Best Practices

### Input Sources
- ✅ **Event Hubs**: High-throughput streaming
- ✅ **IoT Hub**: Device telemetry
- ✅ **Blob Storage**: Reference data
- ✅ **Data Lake**: Historical data

### Query Design
- ✅ **Windowing**: Tumbling, hopping, sliding, session
- ✅ **JOIN**: Stream-to-stream, stream-to-reference
- ✅ **Aggregations**: COUNT, SUM, AVG, MIN, MAX
- ✅ **Temporal operators**: LAG, LAST, DATEDIFF

### Output Sinks
- ✅ **SQL Database**: Structured results
- ✅ **Cosmos DB**: NoSQL storage
- ✅ **Event Hubs**: Downstream processing
- ✅ **Power BI**: Real-time dashboards
- ✅ **Blob Storage**: Archive
- ✅ **Data Lake**: Analytics

### Performance
- ✅ **Partition input**: Parallel processing
- ✅ **Partition key**: Align with query
- ✅ **SU scaling**: Match throughput needs
- ✅ **Late arrival policy**: Handle delayed events

### Monitoring
- ✅ **SU utilization**: Scale when >80%
- ✅ **Watermark delay**: Data freshness
- ✅ **Input events**: Monitor throughput
- ✅ **Errors**: Runtime/data errors

---

## ⚠️ Limitaciones

- Max 192 SU per job
- Query timeout: None (continuous)
- Late arrival: Max 21 days
- Out-of-order: Max 21 days

---

## ✅ Checklist

- [ ] Job created
- [ ] Inputs configured
- [ ] Query written and tested
- [ ] Outputs configured
- [ ] SU allocated
- [ ] Compatibility level set
- [ ] Job started
- [ ] Monitoring configured
- [ ] Alerts set (SU >80%)
