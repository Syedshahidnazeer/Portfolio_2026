"""
HTML Component Generator.

This module helps generate HTML components for the Streamlit application.
It decouples the logic from the main application file, ensuring better maintainability.
Data is pulled dynamically from `config.py`.
"""
from typing import List, Dict, Any
from config import PROFILE, SKILLS, PROJECTS, STATS, EDUCATION, CERTIFICATIONS, LOGOS, RESUMES, EXPERIENCE
from utils import img_to_bytes
# Force Deploy Update

def get_navbar_html() -> str:
    """Generates the sticky navigation bar HTML."""
    return f"""
    <nav class="nav">
        <div class="nav-brand">SHAHID<span style="color:var(--accent)">.dev</span></div>
        <div class="nav-pill">
            <a onclick="switchView('main')" id="link-main" class="nav-item active">Home</a>
            <a onclick="switchView('education')" id="link-education" class="nav-item">Education</a>
            <a onclick="switchView('experience')" id="link-experience" class="nav-item">Experience</a>
            <a onclick="switchView('skills')" id="link-skills" class="nav-item">Skills</a>
            <a onclick="switchView('projects')" id="link-projects" class="nav-item">Projects</a>
            <a onclick="switchView('certifications')" id="link-certifications" class="nav-item">Certifications</a>
            <a onclick="switchView('contact')" id="link-contact" class="nav-item">Contact</a>
        </div>
        <div class="nav-status" style="display:flex; align-items:center; gap:15px;">
            <button onclick="toggleDarkMode()" id="theme-toggle" style="background:none; border:none; cursor:pointer; font-size:1.2rem; padding:5px; border-radius:50%; transition:transform 0.3s ease;">
                🌓
            </button>
            <span><span style="color:#2EC4B6">●</span> {STATS['status'].upper()}</span>
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

def get_education_mascot_html() -> str:
    """Generates the Education view mascot - Graduate theme."""
    return """
    <div class="view-mascot-wrapper">
        <div class="view-mascot mascot-education" id="mascot-education">
            <div class="mascot-cap"></div>
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

def get_experience_mascot_html() -> str:
    """Generates the Experience view mascot - Professional Working Guy theme."""
    return """
    <div class="view-mascot-wrapper">
        <div class="view-mascot mascot-experience" id="mascot-experience">
            <div class="mascot-collar"></div>
            <div class="mascot-tie"></div>
            <div class="mascot-briefcase"></div>
            <div class="mascot-glasses"></div>
            <div class="eyebrows">
                <div class="eyebrow left"></div>
                <div class="eyebrow right"></div>
            </div>
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

def get_skills_mascot_html() -> str:
    """Generates the Skills view mascot - VR / Cyber theme."""
    return """
    <div class="view-mascot-wrapper" style="pointer-events: auto;"> 
        <div class="view-mascot mascot-skills" id="mascot-skills">
            <div class="mascot-visor"></div>
            <div class="mascot-earpiece left"></div>
            <div class="mascot-earpiece right"></div>
            <div class="mouth">
                <div class="tongue"></div>
            </div>
            <!-- Glitch Elements -->
            <div class="glitch-layer blue"></div>
            <div class="glitch-layer red"></div>
        </div>
    </div>
    """

def get_projects_mascot_html() -> str:
    """Generates the Projects view mascot - Builder theme."""
    return """
    <div class="view-mascot-wrapper">
        <div class="view-mascot mascot-projects" id="mascot-projects">
            <div class="mascot-hardhat"></div>
            <div class="mascot-tool"></div>
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

def get_certifications_mascot_html() -> str:
    """Generates the Certifications view mascot - Achievement theme."""
    return """
    <div class="view-mascot-wrapper">
        <div class="view-mascot mascot-certifications" id="mascot-certifications">
            <div class="mascot-trophy"></div>
            <div class="mascot-medal"></div>
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

def get_contact_mascot_html() -> str:
    """Generates the Contact view mascot - Friendly theme."""
    return """
    <div class="view-mascot-wrapper">
        <div class="view-mascot mascot-contact" id="mascot-contact">
            <div class="mascot-wave-hand"></div>
            <div class="mascot-heart"></div>
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
    
    cards_html = ""
    for i, project in enumerate(PROJECTS):
        delay = 0.1 + (i * 0.1)
        
        # Tags Generation
        tags_html = "".join([f'<span class="skill-tag" style="font-size:0.75rem; padding:4px 10px; background:var(--bg-secondary); border:1px solid var(--border); color:var(--text-dim);">{tag}</span>' for tag in project.get('tags', [])])
        
        gradient = project.get('gradient', 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)')

        cards_html += f"""
        <div class="card tilt-card spotlight-card anim-stagger" data-tilt style="padding:0; overflow:hidden; border:none; display:flex; flex-direction:column; animation-delay:{delay}s; height:320px;">
            <!-- Gradient Header -->
            <div style="height:140px; background:{gradient}; position:relative; display:flex; align-items:flex-end; padding:1.5rem;">
                <div style="font-size:3rem; opacity:0.2; position:absolute; top:10px; right:15px; font-weight:900; color:white;">0{i+1}</div>
            </div>
            
            <!-- Content -->
            <div style="padding:1.5rem; flex:1; display:flex; flex-direction:column; background:var(--card-bg);">
                <h3 style="font-family:'Fredoka'; font-size:1.4rem; margin-bottom:0.5rem; line-height:1.2;">{project['title']}</h3>
                <p style="font-size:0.9rem; color:var(--text-dim); margin-bottom:1rem; flex:1; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">
                    {project.get('desc', 'Innovative solution leveraging advanced algorithms and modern tech stacks.')}
                </p>
                
                <div style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:1rem;">
                    {tags_html}
                </div>
                
                <a href="#" style="font-size:0.85rem; color:var(--accent); font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:5px;">
                    View Project <span style="font-size:1rem;">&rarr;</span>
                </a>
            </div>
        </div>
        """
    
    return f"""
    <div id="view-projects" class="view-section">
        <div class="dashboard-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:2rem; max-width:1200px; margin: 0 auto;">
             <div style="grid-column: 1/-1; text-align:center; margin-bottom:1rem; padding-top:1rem;">
                {get_projects_mascot_html()}
                <div style="font-family:'Fredoka'; color:var(--accent); font-size:1rem; letter-spacing:1px; margin-bottom:0.5rem;">PORTFOLIO</div>
                <h2 style="font-family:'Fredoka'; font-size:2.5rem; color:var(--text);">Innovation <span style="color:var(--accent)">Gallery</span></h2>
                <p style="color:var(--text-dim); margin-top:0.5rem;">A collection of my work in AI, Data Science, and Development.</p>
            </div>
            {cards_html}
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
    """Generates the Education view with a Bento Grid layout (Detailed Light Theme)."""
    # Helper for safe access
    def e(idx): return EDUCATION[idx] if idx < len(EDUCATION) else EDUCATION[0]

    return f"""
    <div id="view-education" class="view-section">
        <!-- Scripts: Vanilla Tilt + Canvas Confetti -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.7.0/vanilla-tilt.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

        <script type="text/javascript">
            // 1. Initialize Tilt
            const initEducationTilt = () => {{
                VanillaTilt.init(document.querySelectorAll(".tilt-card"), {{
                    max: 5, speed: 400, glare: true, "max-glare": 0.2
                }});
            }};

            // 2. Spotlight Effect (Mouse Tracking)
            const initEducationSpotlight = () => {{
                const cards = document.querySelectorAll(".spotlight-card");
                cards.forEach(card => {{
                    card.addEventListener("mousemove", (e) => {{
                        const rect = card.getBoundingClientRect();
                        const x = e.clientX - rect.left;
                        const y = e.clientY - rect.top;
                        card.style.setProperty("--x", `${{x}}px`);
                        card.style.setProperty("--y", `${{y}}px`);
                    }});
                }});
            }};

            // 3. Confetti Trigger
            const triggerConfetti = () => {{
                var duration = 3 * 1000;
                var animationEnd = Date.now() + duration;
                var defaults = {{ startVelocity: 30, spread: 360, ticks: 60, zIndex: 9999 }};

                function random(min, max) {{ return Math.random() * (max - min) + min; }}

                var interval = setInterval(function() {{
                    var timeLeft = animationEnd - Date.now();
                    if (timeLeft <= 0) {{ return clearInterval(interval); }}
                    var particleCount = 50 * (timeLeft / duration);
                    // multiple origins
                    confetti(Object.assign({{}}, defaults, {{ particleCount, origin: {{ x: random(0.1, 0.3), y: Math.random() - 0.2 }} }}));
                    confetti(Object.assign({{}}, defaults, {{ particleCount, origin: {{ x: random(0.7, 0.9), y: Math.random() - 0.2 }} }}));
                }}, 250);
            }};

            // Run Init
            setTimeout(() => {{
                initEducationTilt();
                initEducationSpotlight();
                
                // Attach click to Growth Card
                const growthCard = document.getElementById("growth-card");
                if(growthCard) {{
                    growthCard.addEventListener("click", triggerConfetti);
                }}
            }}, 100);
        </script>

        <div class="dashboard-grid" style="grid-template-rows: repeat(auto-fit, minmax(200px, 1fr)); gap:1.2rem;">
            
            <!-- 1. HEADER -->
            <div class="card spotlight-card anim-stagger" style="display:flex; justify-content:space-between; align-items:center; padding:2rem; animation-delay: 0.1s;">
                <div>
                    <div style="font-family:'Fredoka'; color:var(--accent); font-size:1rem; letter-spacing:1px;">ACADEMIC</div>
                    <h2 style="font-family:'Fredoka'; font-size:2rem; line-height:1.1;">Educational<br>Journey</h2>
                    <div style="margin-top:1rem; font-size:0.9rem; color:var(--text-dim);">Foundations of my technical expertise.</div>
                </div>
                {get_education_mascot_html()}
            </div>

            <!-- 2. MAIN DEGREE (B.Tech) -->
            <div class="card span-2 tilt-card spotlight-card anim-stagger" data-tilt style="position:relative; overflow:hidden; display:flex; flex-direction:column; justify-content:flex-start; animation-delay: 0.2s;">
                <div style="position:absolute; top:2rem; right:2rem; display:flex; gap:10px; z-index:3;">
                    <div style="background:var(--bg); padding:8px; border-radius:12px; border:1px solid var(--border);">
                        <img src="{img_to_bytes(e(0).get('logo', ''))}" style="width:60px; height:60px; object-fit:contain;">
                    </div>
                    {f'''
                    <div style="background:var(--bg); padding:8px; border-radius:12px; border:1px solid var(--border);">
                        <img src="{img_to_bytes(e(0).get('logo_secondary', ''))}" style="width:60px; height:60px; object-fit:contain;">
                    </div>
                    ''' if e(0).get('logo_secondary') else ''}
                </div>
                
                <div style="margin-top:0; z-index:3;">
                    <div class="skill-tag core" style="margin:0 0 1rem 0;">{e(0)['duration']}</div>
                    <h3 style="font-family:'Fredoka'; font-size:1.8rem; margin-bottom:0.5rem; line-height:1.2;">{e(0)['degree']}</h3>
                    <div style="font-size:1.1rem; color:var(--text); font-weight:600; margin-bottom:0.2rem;">{e(0)['institution']}</div>
                    <div style="font-size:0.9rem; color:var(--text-dim); margin-bottom:1rem;">{e(0)['university']}</div>
                    
                     <p style="font-size:0.95rem; line-height:1.6; color:var(--text-dim); max-width:85%; margin-top:1.5rem;">
                        {e(0)['desc']}
                    </p>
                </div>

                <div style="margin-top:2rem; padding-top:1.5rem; border-top:1px dashed var(--border); display:flex; gap:2rem; flex-wrap:wrap; z-index:3;">
                     <div style="min-width:120px;">
                        <div style="font-size:0.75rem; color:var(--text-dim); text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">Percentage</div>
                        <div style="font-family:'JetBrains Mono'; font-size:1.2rem; font-weight:700; color:var(--accent);">{e(0)['grade']}</div>
                        <div class="grade-bar-container"><div class="grade-bar-fill" style="background:var(--accent); --percent: 68%;"></div></div>
                     </div>
                     <div style="min-width:150px;">
                        <div style="font-size:0.75rem; color:var(--text-dim); text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">Academic Performance</div>
                        <div style="font-family:'JetBrains Mono'; font-size:1.1rem; font-weight:600; color:var(--accent-3);">{e(0)['cgpa']}</div>
                         <div class="grade-bar-container"><div class="grade-bar-fill" style="background:var(--accent-3); --percent: 92%;"></div></div>
                     </div>
                </div>
            </div>

            <!-- 3. GROWTH WIDGET (Clickable Confetti) -->
            <div id="growth-card" class="card tilt-card spotlight-card anim-stagger confetti-trigger" data-tilt style="display:flex; align-items:center; justify-content:center; background:var(--accent); color:white; border:none; animation-delay: 0.3s;">
                <div style="text-align:center; pointer-events:none;">
                    <div style="font-size:3.5rem; font-weight:700;">4</div>
                    <div style="font-family:'JetBrains Mono'; opacity:0.9; font-size:1.2rem;">Years</div>
                    <div style="font-size:0.9rem; margin-top:0.5rem; opacity:0.9;">Engineering Excellence</div>
                </div>
            </div>

            <!-- 4. 12th Grade -->
            <div class="card span-2 tilt-card spotlight-card anim-stagger" data-tilt style="display:flex; flex-direction:column; justify-content:space-between; animation-delay: 0.4s;">
                <div style="display:flex; justify-content:space-between; align-items:start; z-index:3;">
                    <div>
                         <span class="skill-tag" style="margin-bottom:0.8rem;">{e(1)['duration']}</span>
                         <h4 style="font-family:'Fredoka'; font-size:1.4rem; margin-bottom:0.5rem;">{e(1)['degree']}</h4>
                         <div style="font-weight:600; color:var(--text);">{e(1)['institution']}</div>
                         <div style="font-size:0.85rem; color:var(--text-dim); margin-top:0.2rem;">{e(1)['board']}</div>
                    </div>
                    <img src="{img_to_bytes(e(1).get('logo', ''))}" style="width:50px; height:50px; object-fit:contain; border-radius:8px;">
                </div>
                
                 <p style="font-size:0.9rem; line-height:1.5; color:var(--text-dim); margin:1.5rem 0; z-index:3;">
                    {e(1)['desc']}
                </p>

                <div style="margin-top:auto; padding-top:1rem; border-top:1px solid var(--border); z-index:3;">
                    <span style="font-size:0.8rem; color:var(--text-dim); margin-right:8px;">Score:</span>
                    <span style="font-family:'JetBrains Mono'; font-weight:700; color:var(--accent-3); font-size:1.1rem;">{e(1)['grade']}</span>
                     <div class="grade-bar-container"><div class="grade-bar-fill" style="background:var(--accent-3); --percent: 75%;"></div></div>
                </div>
            </div>

            <!-- 5. QUOTE -->
            <div class="card spotlight-card anim-stagger" style="background:var(--bg-secondary); border:none; display:flex; align-items:center; justify-content:center; text-align:center; padding:2rem; animation-delay: 0.5s;">
                <div style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.1rem; color:var(--text-dim); z-index:3;">
                    "Learning is not attained by chance, it must be sought for with ardor and attended to with diligence."
                </div>
            </div>

            <!-- 6. 10th Grade -->
            <div class="card span-2 tilt-card spotlight-card anim-stagger" data-tilt style="display:flex; flex-direction:column; justify-content:space-between; animation-delay: 0.6s;">
               <div style="display:flex; justify-content:space-between; align-items:start; z-index:3;">
                    <div>
                         <span class="skill-tag" style="margin-bottom:0.8rem;">{e(2)['duration']}</span>
                         <h4 style="font-family:'Fredoka'; font-size:1.4rem; margin-bottom:0.5rem;">{e(2)['degree']}</h4>
                         <div style="font-weight:600; color:var(--text);">{e(2)['institution']}</div>
                         <div style="font-size:0.85rem; color:var(--text-dim); margin-top:0.2rem;">{e(2)['board']}</div>
                    </div>
                    <img src="{img_to_bytes(e(2).get('logo', ''))}" style="width:50px; height:50px; object-fit:contain; border-radius:8px;">
                </div>
                
                 <p style="font-size:0.9rem; line-height:1.5; color:var(--text-dim); margin:1.5rem 0; z-index:3;">
                    {e(2)['desc']}
                </p>

                <div style="margin-top:auto; padding-top:1rem; border-top:1px solid var(--border); z-index:3;">
                    <span style="font-size:0.8rem; color:var(--text-dim); margin-right:8px;">GPA:</span>
                    <span style="font-family:'JetBrains Mono'; font-weight:700; color:var(--accent-3); font-size:1.1rem;">{e(2)['grade']}</span>
                     <div class="grade-bar-container"><div class="grade-bar-fill" style="background:var(--orange, #FF9F1C); --percent: 88%;"></div></div>
                </div>
            </div>

        </div>
    </div>
    """

def get_experience_view_html() -> str:
    """Generates the Work Experience view."""
    # Prepare HTML for Left and Right Columns
    exp_left_html = ""
    exp_right_html = ""
    
    # Counter for items in each column to check for first item
    left_count = 0
    right_count = 0

    for i, job in enumerate(EXPERIENCE):
        delay = 0.1 + (i * 0.1)
        
        details_html = "".join([f'<li style="margin-bottom:0.3rem;">{d}</li>' for d in job['details']])
        
        logo_tag = f'<img src="{img_to_bytes(job.get("logo", ""))}" style="width:50px; height:50px; object-fit:contain; border-radius:8px; margin-bottom:1rem;">' if job.get('logo') else ''

        # Distribute: Even index -> Left, Odd index -> Right
        is_left = (i % 2 == 0)
        
        # Add margin-top:0 to the first card in each column to align them perfectly at the top
        extra_style = "margin-top: 0;" if (is_left and left_count == 0) or (not is_left and right_count == 0) else ""

        job_html = f"""
        <div class="card tilt-card spotlight-card anim-stagger" data-tilt style="margin-bottom:2rem; animation-delay:{delay}s; padding:2rem; border-left:4px solid var(--accent); {extra_style}">
            <div style="display:flex; justify-content:space-between; flex-wrap:wrap; align-items:flex-start; margin-bottom:1rem;">
                <div style="flex:1;">
                    {logo_tag}
                    <h3 style="font-family:'Fredoka'; font-size:1.5rem; margin-bottom:0.2rem;">{job['role']}</h3>
                    <div style="font-size:1rem; color:var(--accent); font-weight:600; margin-bottom:0.5rem;">{job['company']} <span style="color:var(--text-dim); font-weight:400;">| {job['location']}</span></div>
                </div>
                <div class="cyber-label" style="font-size:0.9rem; margin-top:0.5rem;">{job['date']}</div>
            </div>
            
            <p style="font-style:italic; color:var(--text-dim); margin-bottom:1.5rem; border-bottom:1px solid var(--border); padding-bottom:1rem;">
                "{job['desc']}"
            </p>

            <ul style="padding-left:1.5rem; color:var(--text); line-height:1.6; font-size:0.95rem;">
                {details_html}
            </ul>
        </div>
        """
        
        if is_left:
             exp_left_html += job_html
             left_count += 1
        else:
             exp_right_html += job_html
             right_count += 1

    return f"""
    <div id="view-experience" class="view-section">
        <!-- 1. Title Row (Centered) -->
        <div class="card spotlight-card anim-stagger" style="text-align:center; padding:1.5rem; margin-bottom:4rem; max-width:800px; margin-left:auto; margin-right:auto;">
            <h2 class="intro-title" style="margin-bottom:0.5rem;">Professional <span style="color:var(--accent)">Experience</span></h2>
            <p class="intro-sub" style="margin:0;">My career journey and contributions.</p>
        </div>

        <!-- 2. Content Grid: Left Cards | Center Mascot | Right Cards -->
        <div class="dashboard-grid" style="grid-template-columns: 1fr 220px 1fr; gap:2rem; max-width:1800px; margin:0 auto; align-items:start;">
            
            <!-- Left Column -->
            <div style="display:flex; flex-direction:column;">
                {exp_left_html}
            </div>

            <!-- Center Column (Sticky Mascot) -->
            <div style="position:sticky; top:100px; display:flex; justify-content:center; align-items:center;">
                 {get_experience_mascot_html()}
            </div>

            <!-- Right Column -->
            <div style="display:flex; flex-direction:column;">
                {exp_right_html}
            </div>
        </div>
    </div>
    """

def get_skills_detailed_view_html() -> str:
    """Generates the 'Tech Arsenal' grid view."""
    
    # Categories Definition
    tech_stacks = {
        "AI & Generative Tech": ["Generative AI", "LLM", "NLP", "RAG"],
        "Data Science & ML": ["Python", "Data Science", "ML", "DL"],
        "Tools & Platforms": ["MySQL", "PowerBI", "Excel"]
    }

    # Flatten skills for Orbit Layout
    all_skills_flat = []
    for cat, skills in tech_stacks.items():
        for s in skills:
            all_skills_flat.append(s)
            
    # Distribute into Rings
    # Inner Ring: Core AI & Python (First ~5)
    inner_skills = all_skills_flat[:5]
    # Outer Ring: The rest
    outer_skills = all_skills_flat[5:]
    
    def generate_orbit_items(skills_list, ring_name):
        html = ""
        total = len(skills_list)
        for i, skill_name in enumerate(skills_list):
            logo_path = LOGOS.get(skill_name, LOGOS.get(skill_name.split()[0], ""))
            img_tag = f'<img src="{img_to_bytes(logo_path)}" class="planet-icon">' if logo_path else '<div class="planet-icon-placeholder">⚡</div>'
            
            html += f"""
            <div class="skill-planet" style="--i:{i}; --total:{total};">
                <div class="planet-content">
                    {img_tag}
                    <span class="planet-label">{skill_name}</span>
                </div>
            </div>
            """
        return html

    return f"""
    <div id="view-skills" class="view-section skill-galaxy-view">
        <h2 class="intro-title" style="text-align:center; margin-bottom:1rem; position:absolute; top:20px; width:100%; z-index:10; pointer-events:none;">
            Technical <span style="color:var(--accent)">Universe</span>
        </h2>
        
        <div class="galaxy-container">
            <!-- Center Core: The Cyber Mascot -->
            <div class="galaxy-core">
                {get_skills_mascot_html()}
            </div>

            <!-- Inner Orbit -->
            <div class="orbit-ring inner">
                {generate_orbit_items(inner_skills, "inner")}
            </div>

            <!-- Outer Orbit -->
            <div class="orbit-ring outer">
                {generate_orbit_items(outer_skills, "outer")}
            </div>
        </div>
        
        <!-- Mobile Fallback / Accessibility List (Hidden on Desktop via CSS if needed, or we rely on Galaxy responsive) -->
    </div>
    """

def get_certifications_view_html() -> str:
    """Generates the Certifications view - 3-Column Layout (Left | Mascot | Right)."""
    
    cert_left = ""
    cert_right = ""
    delay = 0.1

    for i, cert in enumerate(CERTIFICATIONS):
        # Card HTML
        logo = LOGOS.get(cert['issuer'], "")
        img_tag = f'<img src="{img_to_bytes(logo)}" style="width:50px; height:50px; object-fit:contain; border-radius:4px; margin-bottom:1rem;">' if logo else '<div style="font-size:2rem; margin-bottom:1rem;">🏆</div>'
        
        card_html = f"""
        <div class="card tilt-card spotlight-card anim-stagger" data-tilt style="padding:2rem; margin-bottom:2rem; display:flex; flex-direction:column; align-items:flex-start; text-align:left; animation-delay:{delay}s; border:1px solid var(--border);">
            <div style="width:100%; display:flex; justify-content:space-between; align-items:start;">
                 {img_tag}
                 <div style="font-family:'JetBrains Mono'; color:var(--text-dim); font-size:0.8rem;">{cert.get('date', '')}</div>
            </div>
            
            <!-- Certificate Image Preview -->
            <div style="width:100%; height:200px; overflow:hidden; border-radius:8px; margin-bottom:1rem; border:1px solid var(--border); background:rgba(0,0,0,0.2); display:flex; justify-content:center; align-items:center;">
                <img src="{img_to_bytes(cert.get('image', ''))}" style="max-width:100%; max-height:100%; object-fit:contain; transition:transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>

            <h3 style="font-family:'Fredoka'; font-size:1.4rem; color:var(--text); margin-bottom:0.5rem; line-height:1.3;">{cert['title']}</h3>
            <div style="color:var(--accent); font-weight:700; font-size:0.9rem; margin-bottom:1rem;">{cert['issuer']}</div>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <span class="skill-tag" style="font-size:0.75rem;">Credential ID: {cert.get('id', 'N/A')}</span>
            </div>
            <a href="{cert.get('link', img_to_bytes(cert.get('image', '')))}" target="_blank" class="cta-btn secondary" style="margin-top:1.5rem; font-size:0.85rem; padding:0.5rem 1rem;">Verify Credential &#x2197;</a>
        </div>
        """
        
        if i % 2 == 0:
            cert_left += card_html
        else:
            cert_right += card_html
            
        delay += 0.1

    return f"""
    <div id="view-certifications" class="view-section">
        <!-- Title Header -->
         <div class="card spotlight-card anim-stagger" style="display:flex; justify-content:space-between; align-items:center; padding:2rem; margin-bottom:3rem; max-width:1400px; margin-left:auto; margin-right:auto;">
            <div style="text-align:left;">
                <div style="font-family:'Fredoka'; color:var(--accent); font-size:1rem; letter-spacing:1px; margin-bottom:0.5rem;">ACHIEVEMENTS</div>
                <h2 style="font-family:'Fredoka'; font-size:2.5rem; color:var(--text); line-height:1.2;">Credential <span style="color:var(--accent)">Vault</span></h2>
                <p style="color:var(--text-dim); margin-top:0.5rem;">Verified technical competencies & awards.</p>
            </div>
        </div>

        <!-- 3-Column Layout -->
        <div class="dashboard-grid" style="grid-template-columns: 1fr 220px 1fr; gap:2rem; max-width:1800px; margin:0 auto; align-items:start;">
            
            <!-- Left Column -->
            <div style="display:flex; flex-direction:column;">
                {cert_left}
            </div>

            <!-- Center Column (Sticky Mascot) -->
            <div style="position:sticky; top:100px; display:flex; justify-content:center; align-items:center;">
                 {get_certifications_mascot_html()}
            </div>

            <!-- Right Column -->
            <div style="display:flex; flex-direction:column;">
                {cert_right}
            </div>
        </div>
    </div>
    """

def get_contact_view_html() -> str:
    """Generates the Contact view."""
    socials = PROFILE['socials']
    
    # Calculate resume links outside f-string
    resume_links = "".join([f'<a href="{path}" target="_blank" class="resume-chip">{role}</a>' for role, path in RESUMES.items()])
    
    return f"""
    <div id="view-contact" class="view-section">
        <div class="card spotlight-card anim-stagger" style="display:flex; justify-content:space-between; align-items:center; padding:2rem; margin-bottom:2rem; max-width:900px; margin-left:auto; margin-right:auto;">
            <div style="text-align:left;">
                <h2 class="intro-title" style="margin-bottom:0.5rem;">Lets <span style="color:var(--accent)">Connect</span></h2>
                <p class="intro-sub" style="margin:0;">Always open to discussing new opportunities.</p>
            </div>
            <div>
                {get_contact_mascot_html()}
            </div>
        </div>
        <div class="dashboard-grid" style="grid-template-columns: 1fr; max-width:600px; margin: 0 auto; text-align:center;">
            <div class="card" style="padding:3rem;">
                <p class="intro-sub" style="margin:1rem auto 2rem;">
                    Always open to discussing new opportunities, collaborations, or just a chat about AI.
                </p>
                
                <a href="mailto:{PROFILE['email']}" class="cta-btn" style="display:inline-block; text-decoration:none; margin-bottom:2rem;">
                    {PROFILE['email']}
                </a>
                
                <div style="display:flex; justify-content:center; gap:20px; font-size:1rem; margin-bottom:3rem;">
                    <a href="{socials['LinkedIn']}" target="_blank" class="nav-item">LinkedIn</a>
                    <a href="{socials['GitHub']}" target="_blank" class="nav-item">GitHub</a>
                </div>

                <!-- Resume Hub -->
                <div style="border-top:1px solid var(--border); padding-top:2rem;">
                    <h3 style="font-family:'Fredoka'; font-size:1.2rem; margin-bottom:1.5rem;">Resume Versions</h3>
                    <div style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center;">
                        {resume_links}
                    </div>
                </div>
                
                <div style="margin-top:3rem; font-size:0.8rem; color:var(--text-dim);">
                    Location: {PROFILE['location']}
                </div>
             </div>
        </div>
    </div>
    """
