---
title: Azure Media Services
area: azure/media
owner: LuisAdan
categories: [Resources, Multimedia]
tags:
  - azure
  - media-services
  - video-encoding
  - streaming
  - content-delivery
  - live-streaming
  - media-processing
  - transcoding
cost: https://azure.microsoft.com/pricing/details/media-services/
repo: https://github.com/org/azure-media-services-iac
last_review: 2026-02-18
---

## 📋 Características

**Media Services** es cloud media processing platform. Video encoding, streaming, live broadcast, content protection, analytics.

### Pricing Components

**Encoding:**
- Standard Encoder: $0.015/minute output (SD), $0.03 (HD), $0.06 (4K)
- Premium Encoder: $0.06/minute (SD), $0.12 (HD), $0.234 (4K)

**Streaming:**
- Streaming Endpoint: $0.25/hour (stopped: $0)
- Premium Streaming: $0.50/hour
- CDN: Azure CDN pricing

**Storage:**
- Standard Storage pricing (~$0.0184/GB/mes)

**Live Events:**
- Basic Pass-through: $0.50/hour
- Standard Pass-through: $1.20/hour
- Standard Encoding: $3.60/hour + transcoding

**Example:**
```
VOD platform:
100 hours HD video/mes: 100 × 60 × $0.03 = $180
Streaming endpoint 24/7: 730 × $0.25 = $182.50
Storage 1 TB: $18.40
Total: ~$381/mes

Live event (8h stream):
Standard encoding: 8 × $3.60 = $28.80
Streaming endpoint: 8 × $0.25 = $2
Total per event: ~$30.80
```

---

## 🏆 Best Practices

### Video-on-Demand (VOD)
- ✅ **Encoding**: Adaptive bitrate (ABR)
- ✅ **Formats**: HLS, DASH, Smooth Streaming
- ✅ **Content protection**: DRM (PlayReady, Widevine, FairPlay)
- ✅ **Storage**: Hot for popular, Cool for archive

### Live Streaming
- ✅ **Pass-through**: Pre-encoded input (cheaper)
- ✅ **Live encoding**: Single bitrate → ABR
- ✅ **Live transcription**: Real-time captions
- ✅ **DVR**: Time-shift up to 25 hours

### Delivery
- ✅ **Streaming Locators**: Access control
- ✅ **Dynamic packaging**: Format on-demand
- ✅ **CDN**: Azure CDN or third-party
- ✅ **Filters**: Client-side manifests

### Content Protection
- ✅ **AES-128**: Encryption
- ✅ **DRM**: Multi-DRM support
- ✅ **Token authentication**: JWT tokens
- ✅ **License delivery**: Built-in servers

### Analytics
- ✅ **Video Indexer**: AI insights
- ✅ **Metrics**: Playback stats
- ✅ **Monitoring**: Azure Monitor integration

### Cost Optimization
- ✅ **Stop streaming endpoints**: When not in use
- ✅ **Pass-through**: Avoid live encoding if possible
- ✅ **Archive to Cool**: Old content
- ✅ **Reserved units**: For high-volume encoding

---

## ⚠️ Limitaciones

- Encoding: Job queue limits
- Live events: Max 20 concurrent per account
- Streaming endpoints: Max 25 per account
- File size: Max 260 GB per asset

---

## ✅ Checklist

- [ ] Media Services account created
- [ ] Storage account linked
- [ ] Assets uploaded
- [ ] Transform created (encoding profile)
- [ ] Job submitted
- [ ] Streaming endpoint created
- [ ] Streaming locator created
- [ ] DRM configured (if needed)
- [ ] CDN configured
- [ ] Player tested
- [ ] Monitoring enabled
