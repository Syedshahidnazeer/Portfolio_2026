"""
HTML Component Generator.

This module helps generate HTML components for the Streamlit application.
It decouples the logic from the main application file, ensuring better maintainability.
Data is pulled dynamically from `config.py`.
"""
from typing import List, Dict, Any
from config import PROFILE, SKILLS, PROJECTS, STATS, EDUCATION, CERTIFICATIONS
# Force Deploy Update

def get_navbar_html() -> str:
    """Generates the sticky navigation bar HTML."""
    return f"""
    <nav class="nav">
        <div class="nav-brand">SHAHID<span style="color:var(--accent)">.dev</span></div>
        <div class="nav-pill">
            <a onclick="switchView('main')" id="link-main" class="nav-item active">Home</a>
            <a onclick="switchView('education')" id="link-education" class="nav-item">Education</a>
            <a onclick="switchView('skills')" id="link-skills" class="nav-item">Skills</a>
            <a onclick="switchView('projects')" id="link-projects" class="nav-item">Work</a>
            <a onclick="switchView('certifications')" id="link-certifications" class="nav-item">Certifications</a>
            <a onclick="switchView('contact')" id="link-contact" class="nav-item">Contact</a>
        </div>
        <div class="nav-status">
            <span style="color:#2EC4B6">●</span> {STATS['status'].upper()}
        </div>
    </nav>
    """

def get_intro_card_html() -> str:
    """Generates the 'Intro/Hero' card with dynamic name splitting."""
    name_parts = PROFILE['name'].split()
    display_name = f"{name_parts[0]} {name_parts[1]}" if len(name_parts) > 1 else PROFILE['name']
    
    return f"""
    <div class="card card-intro">
        <div style="font-family:'JetBrains Mono'; color:var(--accent); font-size:0.8rem; font-weight:700; margin-bottom:0.5rem; letter-spacing:1px;">
            {PROFILE['title'].upper()}
        </div>
        <h1 class="intro-title"><span style="color:var(--text)">{PROFILE['name']}</span></h1>
        <p class="intro-sub">
            {PROFILE['intro_text'].replace(chr(10), '<br>')}
        </p>
        <button onclick="changeEmotion('happy')" class="cta-btn">Say Hello 👋</button>
    </div>
    """

def get_stats_card_html() -> str:
    """Generates the 'Stats & Data' card."""
    return f"""
    <div class="card card-stats">
        <div style="font-family:'Fredoka'; font-size:1.2rem; margin-bottom:1rem;">Stats & Data</div>
        <div class="stat-row">
            <span class="stat-label">Experience</span>
            <span class="stat-val">{STATS['hours']}</span>
        </div>
        <div class="stat-row">
            <span class="stat-label">Projects</span>
            <span class="stat-val">{STATS['projects']}</span>
        </div>
        <div class="stat-row" style="border:none;">
            <span class="stat-label">Status</span>
            <span class="stat-val" style="color:var(--accent-2)">{STATS['status']}</span>
        </div>
    </div>
    """

def get_mascot_html() -> str:
    """Generates the interactive Mascot HTML structure."""
    return """
    <div class="mascot-wrapper">
        <div class="bubble" style="top:20%; left:10%; animation-delay:0s;">AI Systems 🤖</div>
        <div class="bubble" style="bottom:25%; right:5%; animation-delay:2s;">Full Stack 💻</div>
        <div class="bubble" style="top:15%; right:20%; animation-delay:1s;">Agentic AI 🧠</div>

        <div class="mascot-face" id="mascot">
            <div class="eyes-row">
                <div class="eye"><div class="pupil"></div></div>
                <div class="eye"><div class="pupil"></div></div>
            </div>
            <div class="cheeks">
                <div class="cheek"></div>
                <div class="cheek"></div>
            </div>
            <div class="mouth">
                <div class="tongue"></div>
            </div>
        </div>
    </div>
    """

def get_skills_card_html() -> str:
    """Generates the 'Skill Stack' card with categorized tags."""
    skills_html = "".join([
        f'<span class="skill-tag {"core" if s["val"] > 90 else "high" if s["val"] > 80 else ""}">{s["name"]}</span>' 
        for s in SKILLS
    ])
    return f"""
    <div class="card card-skills">
        <div style="font-family:'Fredoka'; font-size:1.2rem; margin-bottom:1rem;">Skill Stack</div>
        <div style="display:flex; flex-wrap:wrap;">
            {skills_html}
        </div>
        <div style="margin-top:auto; padding-top:1rem; border-top:1px solid #eee;">
            <div style="font-size:0.75rem; color:#888;">Recent Focus</div>
            <div style="font-weight:600; color:var(--text);">Agentic Coding Workflows</div>
        </div>
    </div>
    """

def get_map_card_html() -> str:
    """Generates the 'Global Reach' decorative map card."""
    return f"""
    <div class="card card-map">
        <div style="position:absolute; top:1rem; left:1rem; z-index:2; font-family:'Fredoka';">Global Reach</div>
        <svg class="map-svg" viewBox="0 0 300 150">
            <path d="M 20 60 Q 50 30 100 80 T 200 60 T 280 90" stroke="#FFBF69" stroke-width="2" fill="none" stroke-dasharray="4,4" />
            <circle cx="20" cy="60" r="4" fill="#FF9F1C" />
            <circle cx="280" cy="90" r="4" fill="#FF9F1C" />
            <circle cx="50" cy="50" r="2" fill="#ddd" />
            <circle cx="70" cy="80" r="2" fill="#ddd" />
            <circle cx="150" cy="40" r="2" fill="#ddd" />
            <circle cx="220" cy="70" r="2" fill="#ddd" />
            
            <!-- Location Pin for Bangalore -->
            <circle cx="205" cy="75" r="6" fill="#EF233C" opacity="0.8">
                <animate attributeName="r" values="6;10;6" dur="2s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.8;0.2;0.8" dur="2s" repeatCount="indefinite" />
            </circle>
            <text x="215" y="78" font-family="sans-serif" font-size="8" fill="#555">Bengaluru</text>
        </svg>
    </div>
    """

def get_projects_view_html() -> str:
    """
    Generates the 'Cyberpunk Grid' for the Work View.
    Includes scoped canvas for particles and specific Bento widgets.
    """
    # Helper to get project at index safely
    def p(idx: int) -> Dict[str, Any]: 
        return PROJECTS[idx] if idx < len(PROJECTS) else PROJECTS[0]
    
    return f"""
    <div id="view-projects" class="view-section">
        <!-- Scoped Particle Background -->
        <canvas id="particles-js"></canvas>

        <div class="cyber-grid">
            <!-- 1. HEADER CELL (Span 2x2) -->
            <div class="cyber-card span-2 span-2-vert">
                <div class="cyber-label">------ ABOUT</div>
                <h1 class="cyber-title">Creative Developer</h1>
                <p class="cyber-desc">
                    Crafting digital experiences at the intersection of AI, design, and technology.
                    <br><br>
                    <span class="cyber-accent">#001</span> SYSTEM ONLINE
                </p>
                <div class="wireframe-globe"></div>
            </div>

            <!-- 2. STATS CELLS -->
            <div class="cyber-card">
                <div class="cyber-label">STATUS: ACTIVE</div>
                <div class="cyber-title" style="color:var(--accent-2)">50+</div>
                <div class="cyber-label">Projects</div>
            </div>
            <div class="cyber-card">
                <div class="cyber-label">EXP</div>
                <div class="cyber-title" style="color:var(--accent-2)">{STATS['hours']}</div>
                <div class="cyber-label">Years</div>
            </div>

            <!-- 3. SYNCPOINT WIDGET -->
            <div class="cyber-card">
                <div class="cyber-label">SYNCPOINT</div>
                <div class="cyber-title">2026</div>
                <div style="margin-top:auto; border-radius:50%; width:40px; height:40px; border:2px solid #00FF88; display:flex; align-items:center; justify-content:center; font-size:0.7rem; color:#00FF88;">75%</div>
            </div>

            <!-- 4. PROJECT 1 (Main Feature) -->
            <div class="cyber-card span-2-vert">
                <div class="cyber-label">PROJECT.01</div>
                <h2 class="cyber-title">{p(0)['title']}</h2>
                <p class="cyber-desc">AI-driven analysis for strategic decision making.</p>
                <div style="margin-top:auto;">
                    <div class="cyber-label">STACK</div>
                    <div class="p-tag-row">
                        {' '.join([f'<span class="cyber-btn" style="font-size:0.6rem; padding:4px 8px;">{t}</span>' for t in p(0)['tags']])}
                    </div>
                </div>
            </div>

            <!-- 5. TECH STACK WIDGET -->
            <div class="cyber-card span-2">
                <div class="cyber-label">CORE SKILLS</div>
                <h3 class="cyber-title" style="font-size:1.4rem;">Tech Stack</h3>
                <div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:1rem;">
                    <span class="cyber-btn">Python</span>
                    <span class="cyber-btn">TensorFlow</span>
                    <span class="cyber-btn">PyTorch</span>
                    <span class="cyber-btn">React</span>
                    <span class="cyber-btn">Streamlit</span>
                </div>
            </div>

            <!-- 6. GRID SYNC DECORATION -->
            <div class="cyber-card">
                <div class="cyber-label">HEXAFORGE</div>
                <div class="cyber-title">Grid Sync</div>
                <div class="cyber-label">8.9902 / 33.7</div>
            </div>

            <!-- 7. ENERGY WAVE WIDGET (Span 2) -->
            <div class="cyber-card span-2">
                <div style="display:flex; justify-content:space-between;">
                    <div class="cyber-label">SYS-01 RESET</div>
                    <div class="cyber-mono">100%</div>
                </div>
                <h3 class="cyber-title" style="font-size:1.4rem;">Energy Wave</h3>
                <div class="energy-bar"><div class="energy-fill" style="--w:80%"></div></div>
                <div class="energy-bar"><div class="energy-fill" style="--w:60%"></div></div>
                <div class="energy-bar"><div class="energy-fill" style="--w:90%"></div></div>
            </div>

            <!-- 8. PROJECT 2 (Tall) -->
            <div class="cyber-card">
                <div class="cyber-label">SEKTOR</div>
                <h2 class="cyber-title" style="font-size:1.2rem;">{p(1)['title']}</h2>
                <div class="wireframe-globe" style="width:60px; height:60px; right:10px; bottom:10px;"></div>
            </div>

            <!-- 9. PROJECT 3 -->
            <div class="cyber-card span-2 span-2-vert">
                <div class="cyber-label">PROTOCOL</div>
                <h2 class="cyber-title">{p(2)['title']}</h2>
                <p class="cyber-desc">Advanced data structures and prediction algorithms.</p>
                <div style="margin-top:auto; text-align:right;">
                    <div class="cyber-title" style="font-size:3rem; color:#222;">#777</div>
                </div>
            </div>

             <!-- 10. CORE BRUTALIA WIDGET (Footer) -->
            <div class="cyber-card span-2">
                <div style="display:flex; align-items:center; gap:1rem;">
                    <div style="font-size:2rem;">🌐</div>
                    <div>
                        <div class="cyber-title" style="font-size:1.2rem;">Core Brutalia</div>
                        <div class="cyber-label">{STATS['status']}</div>
                    </div>
                    <div style="margin-left:auto; font-size:1.5rem; font-weight:700;">64%</div>
                </div>
                <div class="energy-bar" style="margin-top:1rem;"><div class="energy-fill" style="--w:64%"></div></div>
            </div>
            
        </div>
        
        <div style="text-align:center; margin-top:3rem;">
            <button onclick="switchView('main')" class="cyber-btn" style="padding:12px 24px;">Return to Main System</button>
        </div>
    </div>
    """

def get_main_dashboard_html() -> str:
    """Generates the Main Dashboard (Home View) layout."""
    return f"""
    <div id="view-main" class="view-section active-view">
        <div class="dashboard-grid">
            <!-- Left Column -->
            <div class="col-left">
                {get_intro_card_html()}
                {get_stats_card_html()}
            </div>
            
            <!-- Center Column (Mascot) -->
            <div class="col-center">
                {get_mascot_html()}
            </div>
            
            <!-- Right Column -->
            <div class="col-right">
                {get_skills_card_html()}
                {get_map_card_html()}
            </div>
        </div>
    </div>
    """

def get_education_view_html() -> str:
    """Generates the Education timeline view."""
    ed_html = ""
    for ed in EDUCATION:
        ed_html += f"""
        <div class="cyber-card" style="margin-bottom:1rem; position:relative; overflow:hidden;">
             <div class="cyber-label">{ed['duration']}</div>
             <h3 class="cyber-title" style="font-size:1.4rem;">{ed['degree']}</h3>
             <div style="color:var(--text-dim); font-size:0.9rem; margin-top:0.5rem;">{ed['institution']}</div>
             <div style="margin-top:0.5rem; font-family:'JetBrains Mono'; font-size:0.8rem; color:var(--accent);">{ed['grade']}</div>
             <div class="wireframe-globe" style="width:40px; height:40px; right:10px; opacity:0.1;"></div>
        </div>
        """
    
    return f"""
    <div id="view-education" class="view-section">
        <div class="dashboard-grid" style="grid-template-columns: 1fr; max-width:800px;">
            <div style="text-align:center; margin-bottom:2rem;">
                <h2 class="intro-title">Academic <span style="color:var(--accent)">Timeline</span></h2>
                <p class="intro-sub">Foundations of my technical journey.</p>
            </div>
            {ed_html}
        </div>
    </div>
    """

def get_skills_detailed_view_html() -> str:
    """Generates the Detailed Skills view."""
    # Group skills for display
    categories = {
        "AI & LLMs": ["Generative AI", "LLMs & NLP", "RAG Systems", "Prompt Eng."],
        "Development": ["Python", "MLOps", "SQL/NoSQL", "Data Science"]
    }
    
    html = ""
    for cat, items in categories.items():
        tags = "".join([f'<span class="skill-tag" style="font-size:1rem; padding:10px 20px;">{item}</span>' for item in items])
        html += f"""
        <div class="card" style="margin-bottom:1.5rem;">
            <div style="font-family:'Fredoka'; font-size:1.4rem; margin-bottom:1rem; color:var(--text);">{cat}</div>
            <div style="display:flex; flex-wrap:wrap; gap:10px;">
                {tags}
            </div>
        </div>
        """

    return f"""
    <div id="view-skills" class="view-section">
        <div class="dashboard-grid" style="grid-template-columns: 1fr; max-width:800px;">
             <div style="text-align:center; margin-bottom:2rem;">
                <h2 class="intro-title">Technical <span style="color:var(--accent)">Arsenal</span></h2>
                <p class="intro-sub">Tools and technologies I work with.</p>
            </div>
            {html}
        </div>
    </div>
    """

def get_certifications_view_html() -> str:
    """Generates the Certifications grid view."""
    cert_html = ""
    for c in CERTIFICATIONS:
        cert_html += f"""
        <div class="card" style="position:relative; transition:transform 0.3s; cursor:default;">
            <div class="cyber-label" style="color:var(--accent-2)">{c['date']}</div>
            <h3 style="font-family:'Fredoka'; font-size:1.2rem; margin:0.5rem 0;">{c['title']}</h3>
            <div style="font-size:0.9rem; color:var(--text-dim);">{c['issuer']}</div>
            <div style="font-size:0.8rem; margin-top:0.8rem; opacity:0.8;">{c['desc']}</div>
        </div>
        """
        
    return f"""
    <div id="view-certifications" class="view-section">
        <div class="dashboard-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:1.5rem;">
            <div style="grid-column: 1/-1; text-align:center; margin-bottom:2rem;">
                <h2 class="intro-title">Professional <span style="color:var(--accent)">Certifications</span></h2>
            </div>
            {cert_html}
        </div>
    </div>
    """

def get_contact_view_html() -> str:
    """Generates the Contact view."""
    socials = PROFILE['socials']
    return f"""
    <div id="view-contact" class="view-section">
        <div class="dashboard-grid" style="grid-template-columns: 1fr; max-width:600px; text-align:center;">
             <div class="card" style="padding:3rem;">
                <h2 class="intro-title">Let's <span style="color:var(--accent)">Connect</span></h2>
                <p class="intro-sub" style="margin:1rem auto 2rem;">
                    Always open to discussing new opportunities, collaborations, or just a chat about AI.
                </p>
                
                <a href="mailto:{PROFILE['email']}" class="cta-btn" style="display:inline-block; text-decoration:none; margin-bottom:2rem;">
                    {PROFILE['email']}
                </a>
                
                <div style="display:flex; justify-content:center; gap:20px; font-size:1rem;">
                    <a href="{socials['LinkedIn']}" target="_blank" class="nav-item">LinkedIn</a>
                    <a href="{socials['GitHub']}" target="_blank" class="nav-item">GitHub</a>
                </div>
                
                <div style="margin-top:3rem; font-size:0.8rem; color:var(--text-dim);">
                    Location: {PROFILE['location']}
                </div>
             </div>
        </div>
    </div>
    """
