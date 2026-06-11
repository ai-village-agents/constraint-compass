#!/usr/bin/env python3
"""
Update Constraint Compass tutorial with Practical Fallback Runbook section
"""

import re

def add_fallback_runbook():
    with open('index.html', 'r') as f:
        html_content = f.read()
    
    # Find the Universal Application section and add runbook after it
    # We'll insert the new section before the Live Demo section
    
    fallback_section = """
            <div id="fallback-runbook" class="section">
                <h2>Practical Fallback Runbook: Links & Diagnostics</h2>
                <p>When constraints appear, use this diagnostic runbook to identify system layers and fallback options.</p>
                
                <div class="example-box">
                    <h3>CDN Layer Diagnostic Protocol</h3>
                    <p><strong>Step 1: Check Contents API (Source of Truth)</strong></p>
                    <div class="code-block">
                        curl -s "https://api.github.com/repos/ai-village-agents/constraint-dashboard/contents/live_latency.json"
                        # Expected: JSON with current constraint state
                        # Diagnostic: If fails, check GitHub API status
                    </div>
                    
                    <p><strong>Step 2: Check Pages CDN (User-Friendly Layer)</strong></p>
                    <div class="code-block">
                        curl -s "https://ai-village-agents.github.io/constraint-dashboard/live_latency.json"
                        # Expected: Same JSON as Contents API (with possible delay)
                        # Diagnostic: If 404 with 9379 bytes → Pages CDN boundary
                        # Fallback: Switch to Raw CDN
                    </div>
                    
                    <p><strong>Step 3: Check Raw CDN (Machine-Optimized Layer)</strong></p>
                    <div class="code-block">
                        curl -s "https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/live_latency.json"
                        # Expected: Same JSON (with possible different delay pattern)
                        # Diagnostic: If 404 with 14 bytes → Raw CDN boundary  
                        # Fallback: Check Workers or direct API
                    </div>
                    
                    <p><strong>Step 4: Error Pattern Analysis</strong></p>
                    <div class="code-block">
                        # Pages CDN 404 (9379 bytes - user-friendly):
                        curl -I "https://ai-village-agents.github.io/api/live_latency.json"
                        
                        # Raw CDN 404 (14 bytes - machine-optimized):
                        curl -I "https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/api/live_latency.json"
                    </div>
                    
                    <p><strong>Step 5: Timeline Verification</strong></p>
                    <div class="code-block">
                        # Check visualization for propagation patterns:
                        open "https://ai-village-agents.github.io/constraint-dashboard/constraint_timeline.svg"
                        
                        # Key markers to look for:
                        # - 148m Inversion: Early Raw ahead of Pages
                        # - 158m Re-Inversion: Major Raw→Pages lead change  
                        # - tdgm Major Inversion: Another oscillation
                        # - 177m Window Closure: Final constraint state
                    </div>
                </div>
                
                <div class="interactive-area">
                    <h3>Try the Diagnostic Protocol</h3>
                    <p><strong>Scenario</strong>: Your dashboard shows stale data. Instead of "Why is it broken?", ask:</p>
                    <p><strong>"Which CDN layer boundary does this reveal?"</strong></p>
                    <p>Follow the 5-step protocol above to diagnose and find your fallback path.</p>
                </div>
            </div>
            
            <div id="live-demo" class="section">
"""
    
    # Replace the Live Demo section opening with our new section plus the original
    updated_html = html_content.replace('<div id="live-demo" class="section">', fallback_section)
    
    with open('index.html', 'w') as f:
        f.write(updated_html)
    
    print("Added Practical Fallback Runbook section to tutorial")

if __name__ == "__main__":
    add_fallback_runbook()
