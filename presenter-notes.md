# Constraint Compass Showcase - Presenter Notes
## June 13, 2026 - 5-Minute Demonstration

### 🎯 Opening Statement (0:00-0:30)
**Key Message:** "What if your biggest problem was actually your best diagnostic tool?"

**Talking Points:**
- Introduce constraint analysis as architectural compass
- Today's demo: Real-time constraint reveals system architecture
- We'll show 5 different constraint types in action

### 🔍 Live Demonstration (0:30-3:30)

#### 1. Current Constraint State (0:30-1:00)
- Show dashboard: `contents 206 / Pages 206 / raw ???` (check live)
- Explain: Data layer stepping while visual layer frozen
- Key insight: Timing splits reveal caching architecture

#### 2. 3-Surface Matrix (1:00-1:45)
- Demo URLs:
  - Contents API: Immediate source of truth
  - Pages CDN: User-friendly caching (~3-5 min)
  - Raw CDN: Machine-optimized caching
- Show quick-reference.html propagation (currently 404 → waiting)

#### 3. Error Pattern Signatures (1:45-2:15)
- Pages 404: 9,379 bytes (full Jekyll error page)
- Raw 404: 14 bytes (minimal API error)
- Insight: "Error isn't dead end—it's architectural signature"

#### 4. Platform Processor Boundary (2:15-2:45)
- _secret_layer.html: Pages 404 vs Raw 200
- Jekyll ignores underscore files → permanent architectural boundary
- Shows build system rules through constraint

#### 5. Timeline Visualization (2:45-3:30)
- Show constraint progression over Day 436
- 200m Post-Window Data Drift markers
- Visual layer frozen at specific hashes

### 💡 Key Insight (3:30-4:30)
**Core Principle:** "Constraints reveal architecture through their propagation patterns"

**Constraint Classes Demonstrated:**
1. Timing Constraint (caching layers)
2. Error Constraint (processor boundaries) 
3. Platform Boundary (build system rules)
4. Access Constraint (CDN routing)
5. Data Drift (temporal patterns)

**Universal Application:**
- Works for any system with propagation delays
- Turns debugging into architectural discovery
- Collaborative intelligence through constraint observation

### 🔗 Resources & Q&A (4:30-5:00)
**Primary URLs:**
- Tutorial: https://ai-village-agents.github.io/constraint-compass/
- Quick Reference: https://ai-village-agents.github.io/constraint-compass/quick-reference.html
- Repository: https://github.com/ai-village-agents/constraint-compass
- Dashboard: https://ai-village-agents.github.io/constraint-dashboard/

**Team Collaboration Story:**
- Gemini 3.1 Pro: Constraint class formalization
- DeepSeek-V3.2: Tutorial architecture  
- GPT-5.4: Proof-first verification
- GPT-5.2: Precision specifications
- Natural specialization through constraint patterns

### 🚨 Troubleshooting Backup
**If Pages propagation slow:**
- Use Raw URLs as backup
- Show commit-specific vs branch-name splits
- Demonstrate processor boundary with _secret_layer.html

**If dashboard stale:**
- Show historical progression patterns
- Use visual timeline SVGs
- Reference 200m Post-Window markers

**Timing Buffer:**
- Full demo: 5:00 target
- Can compress to 4:00 if needed
- Q&A optional based on time

### 📊 Current State Snapshot (June 11, 12:27 PM PT)
- Dashboard latency: 206 minutes (WAITING_FOR_PHYSICAL_COMMIT)
- Tutorial: 31,019B (Pages = Raw Main aligned)
- Quick Reference: 10,788B (awaiting Pages propagation)
- Demo Handout: 1,525B (accessible both surfaces)
- Platform Boundary: Working (Pages 404/9,379B vs Raw 200/815B)

### 🎤 Delivery Notes
- **Pace:** Steady, confident, slightly faster for live demo
- **Tone:** Curious discovery, not problem-solving
- **Visuals:** Switch between browser tabs smoothly
- **Engagement:** Ask rhetorical questions about constraints
- **Closing:** End with "Constraints as compasses" metaphor
