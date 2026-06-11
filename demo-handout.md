# 🧭 Constraint Compass: Demo Night Pocket Guide

> *"Stop asking 'How do I fix this error?' Start asking 'What boundary does this error reveal?'"*

## 1. The 3-Surface Matrix
When facing a timing or propagation constraint, the system layers will often split. Check all three surfaces to map the architecture:

* **Contents API** (Source of truth): `https://api.github.com/repos/{org}/{repo}/contents/{path}`
* **Pages CDN** (User-friendly caching): `https://{org}.github.io/{repo}/{path}`
* **Raw CDN** (Machine-optimized caching): `https://raw.githubusercontent.com/{org}/{repo}/{branch}/{path}`

## 2. The Absence Signatures (404 Philosophy)
An error isn't a dead end—it's an architectural signature revealing exactly which CDN layer boundary you've encountered.
* **Pages CDN 404 Boundary**: `9379 bytes` (sha256: `b620507312c5...`)
* **Raw CDN 404 Boundary**: `14 bytes` (sha256: `d5558cd419c8...`)

## 3. The 5-Step Observer Checklist
When facing an anomaly, execute this proof-first diagnostic protocol:
1. [ ] **Capture URL**: Record the exact endpoint (including cache-busting `?cb=` params).
2. [ ] **Capture Status**: Record HTTP status code (e.g., 200, 403, 404).
3. [ ] **Capture Bytes**: Measure exact `content-length` or character count.
4. [ ] **Capture Hash**: Generate SHA256/SHA12 of the payload to verify identical states.
5. [ ] **Capture Timestamp**: Note the exact UTC timestamp of the observation.

*Rule of Thumb: Avoid causal claims when layers disagree. Document the empirical strata instead.*
