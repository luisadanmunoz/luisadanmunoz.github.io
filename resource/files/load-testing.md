# Azure Load Testing

## 📋 Características

**Load Testing** es fully managed load testing service. Apache JMeter-based, high-scale testing, auto-scaling, CI/CD integration.

### Pricing

**Virtual Users (VU):**
- FREE: 50 VU-hours/mes
- Paid: $0.003/VU-hour

**Example:**
```
Test: 500 virtual users, 2 hours
500 × 2 = 1,000 VU-hours
Cost: 1,000 × $0.003 = $3.00

Monthly testing (20 tests):
20,000 VU-hours × $0.003 = $60/mes
```

**No infrastructure costs** - fully managed

---

## 🏆 Best Practices

### Test Design
- ✅ **JMeter scripts**: Standard .jmx files
- ✅ **Ramp-up period**: Gradual load increase
- ✅ **Think time**: Realistic user behavior
- ✅ **Parameterization**: CSV data files
- ✅ **Assertions**: Validate responses

### Load Patterns
- ✅ **Baseline**: Steady state load
- ✅ **Stress**: Find breaking point
- ✅ **Spike**: Sudden traffic increase
- ✅ **Soak**: Long-duration stability

### Integration
- ✅ **CI/CD**: Azure Pipelines, GitHub Actions
- ✅ **Automated testing**: Pre-production gates
- ✅ **App Insights**: Correlation with app metrics
- ✅ **Load Test on demand**: Manual triggers

### Monitoring
- ✅ **Response time**: P50, P90, P95, P99
- ✅ **Throughput**: Requests per second
- ✅ **Error rate**: Failed requests %
- ✅ **App metrics**: CPU, memory, database

### Best Practices
- ✅ **Test from multiple regions**: Distributed load
- ✅ **Private endpoint**: Test private apps
- ✅ **Pass/fail criteria**: Automated validation
- ✅ **Baseline comparison**: Track performance

---

## ⚠️ Limitaciones

- Max virtual users: 45,000 per test
- Test duration: Max 3 hours
- Script size: 50 MB max
- Regional: Test runs in same region

---

## ✅ Checklist

- [ ] Load Testing resource created
- [ ] JMeter script prepared
- [ ] Test parameters configured
- [ ] Load pattern defined
- [ ] Virtual users allocated
- [ ] Pass/fail criteria set
- [ ] App Insights integrated
- [ ] Test executed
- [ ] Results analyzed
- [ ] CI/CD integrated
