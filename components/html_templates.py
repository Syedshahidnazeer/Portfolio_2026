from config import PROFILE, SKILLS, PROJECTS, STATS, EDUCATION, CERTIFICATIONS, LOGOS, RESUMES, EXPERIENCE
from utils import img_to_bytes


def get_navbar_html() -> str:
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
            <span><span style="color:var(--accent)">●</span> {STATS['status'].upper()}</span>
        </div>
    </nav>
    """


def get_intro_card_html() -> str:
    name_parts = PROFILE['name'].split()
    display_name = f"{name_parts[0]} {name_parts[1]}" if len(name_parts) > 1 else PROFILE['name']

    return f"""
    <div class="card card-intro">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:0.8rem;">
            <div style="font-family:'Fredoka'; color:var(--accent); font-size:0.8rem; font-weight:700; letter-spacing:1px;">
                {PROFILE['title'].upper()}
            </div>
            <div class="available-badge">OPEN TO WORK</div>
        </div>
        <div id="time-greeting" style="font-size:0.85rem; color:var(--text-dim); margin-bottom:0.3rem; font-weight:500;"></div>
        <h1 class="intro-title">
            <span id="hero-typed" data-text="{PROFILE['name']}" style="color:var(--text)">{PROFILE['name']}</span><span class="typing-cursor"></span>
        </h1>
        <p class="intro-sub" style="margin-bottom:0.5rem;">
            {PROFILE['intro_text'].replace(chr(10), '<br>')}
        </p>
        <div id="role-cycle" style="font-size:0.82rem; color:var(--accent); font-weight:600; height:1.4em; overflow:hidden; margin-bottom:0.8rem;">
            <span id="role-text"></span><span class="typing-cursor" style="height:0.9rem;"></span>
        </div>
        <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap;">
            <button onclick="sayHello()" class="cta-btn">Say Hello &#128075;</button>
            <span style="font-size:0.7rem; color:var(--text-dim); opacity:0.5;">Press &#8593;&#8593;&#8595;&#8595;&#8592;&#8594;&#8592;&#8594;BA for a surprise</span>
        </div>
    </div>
    """


def get_stats_card_html() -> str:
    return f"""
    <div class="card card-stats">
        <div style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.2rem; margin-bottom:1rem;">Stats & Data</div>
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
            <span class="stat-val" style="color:var(--accent)">{STATS['status']}</span>
        </div>
    </div>
    """


def get_mascot_html() -> str:
    return """
    <div class="mascot-wrapper">
        <div class="bubble" style="top:20%; left:10%; animation-delay:0s;">AI Systems 🌸</div>
        <div class="bubble" style="bottom:25%; right:5%; animation-delay:2s;">Full Stack 🌿</div>
        <div class="bubble" style="top:15%; right:20%; animation-delay:1s;">Agentic AI 🦋</div>

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
        <div style="margin-top:auto; padding-top:1rem; border-top:1px solid var(--border);">
            <div style="font-size:0.75rem; color:var(--text-dim);">Recent Focus</div>
            <div style="font-weight:600; color:var(--text);">Agentic Coding Workflows</div>
        </div>
    </div>
    """


def get_map_card_html() -> str:
    return f"""
    <div class="card card-map">
        <div style="position:absolute; top:1rem; left:1rem; z-index:2; font-family:'Fredoka';">Global Reach</div>
        <svg class="map-svg" viewBox="0 0 300 150">
            <path d="M 20 60 Q 50 30 100 80 T 200 60 T 280 90" stroke="var(--accent-2)" stroke-width="2" fill="none" stroke-dasharray="4,4" />
            <circle cx="20" cy="60" r="4" fill="var(--accent)" />
            <circle cx="280" cy="90" r="4" fill="var(--accent)" />
            <circle cx="50" cy="50" r="2" fill="var(--border)" />
            <circle cx="70" cy="80" r="2" fill="var(--border)" />
            <circle cx="150" cy="40" r="2" fill="var(--border)" />
            <circle cx="220" cy="70" r="2" fill="var(--border)" />
            <circle cx="205" cy="75" r="6" fill="var(--accent)" opacity="0.8">
                <animate attributeName="r" values="6;10;6" dur="2s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.8;0.2;0.8" dur="2s" repeatCount="indefinite" />
            </circle>
            <text x="215" y="78" font-family="sans-serif" font-size="8" fill="var(--text-dim)">Bengaluru</text>
        </svg>
    </div>
    """


def get_main_dashboard_html() -> str:
    return f"""
    <div id="view-main" class="view-section active-view">
        <div class="dashboard-grid">
            <div class="col-left">
                {get_intro_card_html()}
                {get_stats_card_html()}
            </div>
            <div class="col-center">
                {get_mascot_html()}
            </div>
            <div class="col-right">
                {get_skills_card_html()}
                {get_map_card_html()}
            </div>
        </div>
    </div>
    """


def get_education_view_html() -> str:
    def e(idx):
        return EDUCATION[idx] if idx < len(EDUCATION) else EDUCATION[0]

    return f"""
    <div id="view-education" class="view-section">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.7.0/vanilla-tilt.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

        <script type="text/javascript">
            const initEducationTilt = () => {{
                VanillaTilt.init(document.querySelectorAll(".tilt-card"), {{
                    max: 5, speed: 400, glare: true, "max-glare": 0.15
                }});
            }};

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

            const triggerConfetti = () => {{
                var duration = 3 * 1000;
                var animationEnd = Date.now() + duration;
                var defaults = {{ startVelocity: 30, spread: 360, ticks: 60, zIndex: 9999, colors: ['#B388EB', '#E8A0BF', '#A8D5BA', '#FFE4A0', '#D5B4F7'] }};
                function random(min, max) {{ return Math.random() * (max - min) + min; }}
                var interval = setInterval(function() {{
                    var timeLeft = animationEnd - Date.now();
                    if (timeLeft <= 0) {{ return clearInterval(interval); }}
                    var particleCount = 50 * (timeLeft / duration);
                    confetti(Object.assign({{}}, defaults, {{ particleCount, origin: {{ x: random(0.1, 0.3), y: Math.random() - 0.2 }} }}));
                    confetti(Object.assign({{}}, defaults, {{ particleCount, origin: {{ x: random(0.7, 0.9), y: Math.random() - 0.2 }} }}));
                }}, 250);
            }};

            setTimeout(() => {{
                initEducationTilt();
                initEducationSpotlight();
                const growthCard = document.getElementById("growth-card");
                if(growthCard) {{
                    growthCard.addEventListener("click", triggerConfetti);
                }}
            }}, 100);
        </script>

        <div class="section-header anim-stagger" style="text-align:center; padding:2rem 3rem 0; animation-delay:0.05s;">
            <div style="display:inline-block; padding:6px 18px; border-radius:50px; background:var(--watercolor-1); color:var(--accent); font-family:'Fredoka'; font-size:0.85rem; font-weight:600; letter-spacing:1px; margin-bottom:1rem;">ACADEMIC</div>
            <h2 style="font-family:'Playfair Display', serif; font-size:2.8rem; font-style:italic; color:var(--text); line-height:1.2; margin-bottom:0.5rem;">Educational <span class="gradient-text">Journey</span></h2>
            <p style="color:var(--text-dim); font-size:1rem; max-width:500px; margin:0 auto;">The foundations of my technical expertise and lifelong learning path.</p>
        </div>

        <div class="dashboard-grid" style="grid-template-rows: repeat(auto-fit, minmax(200px, 1fr)); gap:1.2rem; margin-top:2rem;">

            <div class="card span-2 tilt-card spotlight-card anim-stagger" data-tilt style="position:relative; overflow:hidden; display:flex; flex-direction:column; justify-content:flex-start; animation-delay: 0.15s;">
                <div style="position:absolute; top:2rem; right:2rem; display:flex; gap:10px; z-index:3;">
                    <div style="background:var(--bg); padding:8px; border-radius:12px; border:1px solid var(--border);">
                        <img src="{img_to_bytes(e(0).get('logo', ''))}" style="width:60px; height:60px; object-fit:contain;">
                    </div>
                    {f'<div style="background:var(--bg); padding:8px; border-radius:12px; border:1px solid var(--border);"><img src="{img_to_bytes(e(0).get("logo_secondary", ""))}" style="width:60px; height:60px; object-fit:contain;"></div>' if e(0).get('logo_secondary') else ''}
                </div>

                <div style="margin-top:0; z-index:3;">
                    <div class="skill-tag core" style="margin:0 0 1rem 0;">{e(0)['duration']}</div>
                    <h3 style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.8rem; margin-bottom:0.5rem; line-height:1.2;">{e(0)['degree']}</h3>
                    <div style="font-size:1.1rem; color:var(--text); font-weight:600; margin-bottom:0.2rem;">{e(0)['institution']}</div>
                    <div style="font-size:0.9rem; color:var(--text-dim); margin-bottom:1rem;">{e(0)['university']}</div>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-dim); max-width:85%; margin-top:1rem;">{e(0)['desc']}</p>
                </div>

                <div style="margin-top:2rem; padding-top:1.5rem; border-top:1px dashed var(--border); display:flex; gap:2rem; flex-wrap:wrap; z-index:3;">
                     <div style="min-width:120px;">
                        <div style="font-size:0.75rem; color:var(--text-dim); text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">Percentage</div>
                        <div style="font-family:'Fredoka'; font-size:1.2rem; font-weight:700; color:var(--accent);">{e(0)['grade']}</div>
                        <div class="grade-bar-container"><div class="grade-bar-fill" style="background:var(--accent); --percent: 68%;"></div></div>
                     </div>
                     <div style="min-width:150px;">
                        <div style="font-size:0.75rem; color:var(--text-dim); text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">Academic Performance</div>
                        <div style="font-family:'Fredoka'; font-size:1.1rem; font-weight:600; color:var(--accent-3);">{e(0)['cgpa']}</div>
                        <div class="grade-bar-container"><div class="grade-bar-fill" style="background:var(--accent-3); --percent: 92%;"></div></div>
                     </div>
                </div>
            </div>

            <div id="growth-card" class="card tilt-card spotlight-card anim-stagger confetti-trigger" data-tilt style="display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg, var(--accent) 0%, var(--accent-2) 100%); color:white; border:none; animation-delay: 0.2s; cursor:pointer;">
                <div style="text-align:center; pointer-events:none;">
                    <div style="font-size:3.5rem; font-weight:700;">4</div>
                    <div style="font-family:'Fredoka'; opacity:0.9; font-size:1.2rem;">Years</div>
                    <div style="font-size:0.9rem; margin-top:0.5rem; opacity:0.9;">Engineering Excellence</div>
                    <div style="font-size:0.7rem; margin-top:0.8rem; opacity:0.7;">Click me! 🎉</div>
                </div>
            </div>

            <div class="card span-2 tilt-card spotlight-card anim-stagger" data-tilt style="display:flex; flex-direction:column; justify-content:space-between; animation-delay: 0.3s;">
                <div style="display:flex; justify-content:space-between; align-items:start; z-index:3;">
                    <div>
                         <span class="skill-tag" style="margin-bottom:0.8rem;">{e(1)['duration']}</span>
                         <h4 style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.4rem; margin-bottom:0.5rem;">{e(1)['degree']}</h4>
                         <div style="font-weight:600; color:var(--text);">{e(1)['institution']}</div>
                         <div style="font-size:0.85rem; color:var(--text-dim); margin-top:0.2rem;">{e(1)['board']}</div>
                    </div>
                    <img src="{img_to_bytes(e(1).get('logo', ''))}" style="width:50px; height:50px; object-fit:contain; border-radius:12px;">
                </div>
                <p style="font-size:0.9rem; line-height:1.5; color:var(--text-dim); margin:1.5rem 0; z-index:3;">{e(1)['desc']}</p>
                <div style="margin-top:auto; padding-top:1rem; border-top:1px solid var(--border); z-index:3;">
                    <span style="font-size:0.8rem; color:var(--text-dim); margin-right:8px;">Score:</span>
                    <span style="font-family:'Fredoka'; font-weight:700; color:var(--accent-3); font-size:1.1rem;">{e(1)['grade']}</span>
                    <div class="grade-bar-container"><div class="grade-bar-fill" style="background:var(--accent-3); --percent: 75%;"></div></div>
                </div>
            </div>

            <div class="card spotlight-card anim-stagger" style="background:var(--watercolor-1); border:none; display:flex; align-items:center; justify-content:center; text-align:center; padding:2rem; animation-delay: 0.35s;">
                <div style="z-index:3;">
                    <div style="font-size:2.5rem; margin-bottom:0.8rem; opacity:0.3;">🌿</div>
                    <div style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.1rem; color:var(--text-dim); line-height:1.6;">
                        "Learning is not attained by chance, it must be sought for with ardor and attended to with diligence."
                    </div>
                </div>
            </div>

            <div class="card span-2 tilt-card spotlight-card anim-stagger" data-tilt style="display:flex; flex-direction:column; justify-content:space-between; animation-delay: 0.4s;">
               <div style="display:flex; justify-content:space-between; align-items:start; z-index:3;">
                    <div>
                         <span class="skill-tag" style="margin-bottom:0.8rem;">{e(2)['duration']}</span>
                         <h4 style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.4rem; margin-bottom:0.5rem;">{e(2)['degree']}</h4>
                         <div style="font-weight:600; color:var(--text);">{e(2)['institution']}</div>
                         <div style="font-size:0.85rem; color:var(--text-dim); margin-top:0.2rem;">{e(2)['board']}</div>
                    </div>
                    <img src="{img_to_bytes(e(2).get('logo', ''))}" style="width:50px; height:50px; object-fit:contain; border-radius:12px;">
                </div>
                <p style="font-size:0.9rem; line-height:1.5; color:var(--text-dim); margin:1.5rem 0; z-index:3;">{e(2)['desc']}</p>
                <div style="margin-top:auto; padding-top:1rem; border-top:1px solid var(--border); z-index:3;">
                    <span style="font-size:0.8rem; color:var(--text-dim); margin-right:8px;">GPA:</span>
                    <span style="font-family:'Fredoka'; font-weight:700; color:var(--accent-3); font-size:1.1rem;">{e(2)['grade']}</span>
                    <div class="grade-bar-container"><div class="grade-bar-fill" style="background:var(--accent-2); --percent: 88%;"></div></div>
                </div>
            </div>

        </div>
    </div>
    """


def get_experience_view_html() -> str:
    exp_cards_html = ""

    for i, job in enumerate(EXPERIENCE):
        delay = 0.15 + (i * 0.1)
        logo_tag = f'<img src="{img_to_bytes(job.get("logo", ""))}" style="width:55px; height:55px; object-fit:contain; border-radius:16px; border:1px solid var(--border); padding:6px; background:var(--bg);">' if job.get('logo') else ''

        exp_cards_html += f"""
        <div class="card tilt-card spotlight-card anim-stagger" data-tilt style="padding:2.5rem; margin-bottom:2rem; animation-delay:{delay}s; border-left:4px solid var(--accent); position:relative;">
            <div style="position:absolute; top:1.5rem; right:2rem; font-family:'Playfair Display', serif; font-size:4rem; font-weight:700; color:var(--accent); opacity:0.08;">0{i+1}</div>

            <div style="display:flex; align-items:center; gap:1.2rem; margin-bottom:1.5rem;">
                {logo_tag}
                <div style="flex:1;">
                    <h3 style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.5rem; margin-bottom:0.3rem;">{job['role']}</h3>
                    <div style="font-size:1rem; color:var(--accent); font-weight:600;">{job['company']} <span style="color:var(--text-dim); font-weight:400;">| {job['location']}</span></div>
                </div>
                <div style="padding:6px 16px; border-radius:50px; background:var(--watercolor-1); color:var(--accent); font-family:'Fredoka'; font-size:0.8rem; font-weight:600; white-space:nowrap;">{job['date']}</div>
            </div>

            <p style="font-style:italic; color:var(--text-dim); margin-bottom:1.5rem; padding-bottom:1rem; border-bottom:1px solid var(--border); line-height:1.6;">
                "{job['desc']}"
            </p>

            <ul style="padding-left:1.5rem; color:var(--text); font-size:0.95rem; list-style-type:none;">
                {"".join([f'<li style="margin-bottom:0.5rem; line-height:1.6; position:relative; padding-left:1.2rem;"><span style="position:absolute; left:0; color:var(--accent);">→</span> {d}</li>' for d in job['details']])}
            </ul>
        </div>
        """

    return f"""
    <div id="view-experience" class="view-section">
        <div class="section-header anim-stagger" style="text-align:center; padding:2rem 3rem 0; animation-delay:0.05s;">
            <div style="display:inline-block; padding:6px 18px; border-radius:50px; background:var(--watercolor-3); color:#4a8c65; font-family:'Fredoka'; font-size:0.85rem; font-weight:600; letter-spacing:1px; margin-bottom:1rem;">CAREER</div>
            <h2 style="font-family:'Playfair Display', serif; font-size:2.8rem; font-style:italic; color:var(--text); line-height:1.2; margin-bottom:0.5rem;">Professional <span class="gradient-text">Experience</span></h2>
            <p style="color:var(--text-dim); font-size:1rem; max-width:500px; margin:0 auto;">My career journey building AI solutions and driving innovation.</p>
        </div>

        <div style="max-width:800px; margin:2rem auto; padding:0 2rem;">
            {exp_cards_html}
        </div>
    </div>
    """


def get_skills_detailed_view_html() -> str:
    tech_stacks = {
        "AI & Generative Tech": [("Generative AI", 95), ("LLM", 95), ("NLP", 90), ("RAG", 90)],
        "Data Science & ML": [("Python", 85), ("Data Science", 85), ("ML", 80), ("DL", 78)],
        "Tools & Platforms": [("MySQL", 75), ("PowerBI", 70), ("Excel", 75), ("Analytics", 72)]
    }

    cat_icons = {"AI & Generative Tech": "🧠", "Data Science & ML": "📊", "Tools & Platforms": "🛠️"}
    cat_colors = {"AI & Generative Tech": "var(--watercolor-2)", "Data Science & ML": "var(--watercolor-1)", "Tools & Platforms": "var(--watercolor-3)"}

    categories_html = ""
    cat_delay = 0.1

    for cat, skills in tech_stacks.items():
        skills_items = ""
        for skill_name, skill_val in skills:
            logo_path = LOGOS.get(skill_name, LOGOS.get(skill_name.split()[0], ""))
            img_tag = f'<img src="{img_to_bytes(logo_path)}" style="width:32px; height:32px; object-fit:contain; border-radius:8px;">' if logo_path else f'<div style="width:32px; height:32px; border-radius:8px; background:var(--watercolor-1); display:flex; align-items:center; justify-content:center; font-size:0.9rem;">⚡</div>'

            skills_items += f"""
            <div style="display:flex; align-items:center; gap:1rem; padding:0.8rem 0; border-bottom:1px solid var(--border);">
                {img_tag}
                <div style="flex:1;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                        <span style="font-weight:600; font-size:0.9rem;">{skill_name}</span>
                        <span style="font-family:'Fredoka'; font-size:0.85rem; color:var(--accent);">{skill_val}%</span>
                    </div>
                    <div class="grade-bar-container">
                        <div class="grade-bar-fill" style="background:linear-gradient(90deg, var(--accent), var(--accent-2)); --percent:{skill_val}%;"></div>
                    </div>
                </div>
            </div>
            """

        categories_html += f"""
        <div class="card spotlight-card anim-stagger" style="padding:2rem; animation-delay:{cat_delay}s;">
            <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:1.5rem;">
                <div style="width:45px; height:45px; border-radius:14px; background:{cat_colors.get(cat, 'var(--watercolor-1)')}; display:flex; align-items:center; justify-content:center; font-size:1.4rem;">{cat_icons.get(cat, '💡')}</div>
                <h3 style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.3rem;">{cat}</h3>
            </div>
            {skills_items}
        </div>
        """
        cat_delay += 0.1

    return f"""
    <div id="view-skills" class="view-section">
        <div class="section-header anim-stagger" style="text-align:center; padding:2rem 3rem 0; animation-delay:0.05s;">
            <div style="display:inline-block; padding:6px 18px; border-radius:50px; background:var(--watercolor-1); color:var(--accent-3); font-family:'Fredoka'; font-size:0.85rem; font-weight:600; letter-spacing:1px; margin-bottom:1rem;">EXPERTISE</div>
            <h2 style="font-family:'Playfair Display', serif; font-size:2.8rem; font-style:italic; color:var(--text); line-height:1.2; margin-bottom:0.5rem;">Technical <span class="gradient-text">Arsenal</span></h2>
            <p style="color:var(--text-dim); font-size:1rem; max-width:500px; margin:0 auto;">A curated skillset spanning AI, data science, and engineering.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(340px, 1fr)); gap:1.5rem; max-width:1200px; margin:2rem auto; padding:0 3rem;">
            {categories_html}
        </div>
    </div>
    """


def get_projects_view_html() -> str:
    cards_html = ""
    for i, project in enumerate(PROJECTS):
        delay = 0.15 + (i * 0.1)
        tags_html = "".join([f'<span style="display:inline-block; padding:4px 12px; border-radius:50px; font-size:0.75rem; font-weight:600; background:var(--watercolor-1); color:var(--accent-3); margin-right:6px;">{tag}</span>' for tag in project.get('tags', [])])
        gradient = project.get('gradient', 'linear-gradient(135deg, #E8D5F5, #F5D5E8)')

        cards_html += f"""
        <div class="card tilt-card spotlight-card anim-stagger" data-tilt style="padding:0; overflow:hidden; border:none; display:flex; flex-direction:column; animation-delay:{delay}s; height:350px;">
            <div style="height:160px; background:{gradient}; position:relative; display:flex; align-items:flex-end; padding:1.5rem;">
                <div style="font-size:4rem; opacity:0.15; position:absolute; top:10px; right:15px; font-weight:900; color:white; font-family:'Playfair Display', serif;">0{i+1}</div>
                <div style="font-size:0.75rem; color:rgba(255,255,255,0.7); background:rgba(255,255,255,0.2); backdrop-filter:blur(10px); padding:4px 12px; border-radius:50px; font-weight:600;">Featured Project</div>
            </div>

            <div style="padding:1.5rem; flex:1; display:flex; flex-direction:column; background:var(--card-bg);">
                <h3 style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.4rem; margin-bottom:0.5rem; line-height:1.2;">{project['title']}</h3>
                <p style="font-size:0.9rem; color:var(--text-dim); margin-bottom:1rem; flex:1; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; line-height:1.6;">
                    {project.get('desc', 'Innovative solution leveraging advanced algorithms and modern tech stacks.')}
                </p>

                <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:1rem;">
                    {tags_html}
                </div>

                <a href="#" style="font-size:0.85rem; color:var(--accent); font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:5px; transition:gap 0.3s;" onmouseover="this.style.gap='10px'" onmouseout="this.style.gap='5px'">
                    View Project <span style="font-size:1rem;">&rarr;</span>
                </a>
            </div>
        </div>
        """

    return f"""
    <div id="view-projects" class="view-section">
        <div class="section-header anim-stagger" style="text-align:center; padding:2rem 3rem 0; animation-delay:0.05s;">
            <div style="display:inline-block; padding:6px 18px; border-radius:50px; background:var(--watercolor-2); color:#c25a8a; font-family:'Fredoka'; font-size:0.85rem; font-weight:600; letter-spacing:1px; margin-bottom:1rem;">PORTFOLIO</div>
            <h2 style="font-family:'Playfair Display', serif; font-size:2.8rem; font-style:italic; color:var(--text); line-height:1.2; margin-bottom:0.5rem;">Innovation <span class="gradient-text">Gallery</span></h2>
            <p style="color:var(--text-dim); font-size:1rem; max-width:500px; margin:0 auto;">A collection of my work in AI, Data Science, and Development.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.5rem; max-width:1200px; margin:2rem auto; padding:0 3rem;">
            {cards_html}
        </div>
    </div>
    """


def get_certifications_view_html() -> str:
    cert_cards = ""
    delay = 0.15

    for i, cert in enumerate(CERTIFICATIONS):
        logo = LOGOS.get(cert['issuer'], "")
        img_tag = f'<img src="{img_to_bytes(logo)}" style="width:45px; height:45px; object-fit:contain; border-radius:12px; padding:4px; background:var(--bg); border:1px solid var(--border);">' if logo else '<div style="font-size:2rem;">🏆</div>'

        cert_cards += f"""
        <div class="card tilt-card spotlight-card anim-stagger" data-tilt style="padding:0; overflow:hidden; animation-delay:{delay}s; border:none;">
            <div style="width:100%; height:220px; overflow:hidden; background:var(--bg-secondary); display:flex; justify-content:center; align-items:center; border-bottom:1px solid var(--border);">
                <img src="{img_to_bytes(cert.get('image', ''))}" style="max-width:100%; max-height:100%; object-fit:contain; transition:transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);" onmouseover="this.style.transform='scale(1.08)'" onmouseout="this.style.transform='scale(1)'">
            </div>

            <div style="padding:1.8rem;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
                    {img_tag}
                    <div style="font-family:'Fredoka'; color:var(--text-dim); font-size:0.8rem; padding:4px 12px; border-radius:50px; background:var(--watercolor-1);">{cert.get('date', '')}</div>
                </div>

                <h3 style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.3rem; color:var(--text); margin-bottom:0.5rem; line-height:1.3;">{cert['title']}</h3>
                <div style="color:var(--accent); font-weight:600; font-size:0.9rem; margin-bottom:1rem;">{cert['issuer']}</div>

                <div style="display:flex; justify-content:space-between; align-items:center; padding-top:1rem; border-top:1px solid var(--border);">
                    <span style="font-size:0.75rem; color:var(--text-dim);">ID: {cert.get('id', 'N/A')}</span>
                    <a href="{cert.get('link', img_to_bytes(cert.get('image', '')))}" target="_blank" style="font-size:0.85rem; color:var(--accent); font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:5px;">
                        Verify &#x2197;
                    </a>
                </div>
            </div>
        </div>
        """
        delay += 0.1

    return f"""
    <div id="view-certifications" class="view-section">
        <div class="section-header anim-stagger" style="text-align:center; padding:2rem 3rem 0; animation-delay:0.05s;">
            <div style="display:inline-block; padding:6px 18px; border-radius:50px; background:var(--watercolor-1); color:var(--accent); font-family:'Fredoka'; font-size:0.85rem; font-weight:600; letter-spacing:1px; margin-bottom:1rem;">ACHIEVEMENTS</div>
            <h2 style="font-family:'Playfair Display', serif; font-size:2.8rem; font-style:italic; color:var(--text); line-height:1.2; margin-bottom:0.5rem;">Credential <span class="gradient-text">Vault</span></h2>
            <p style="color:var(--text-dim); font-size:1rem; max-width:500px; margin:0 auto;">Verified technical competencies and professional awards.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:1.5rem; max-width:1200px; margin:2rem auto; padding:0 3rem;">
            {cert_cards}
        </div>
    </div>
    """


def get_contact_view_html() -> str:
    socials = PROFILE['socials']
    resume_links = "".join([f'<a href="{path}" target="_blank" class="resume-chip">{role}</a>' for role, path in RESUMES.items()])

    return f"""
    <div id="view-contact" class="view-section">
        <div class="section-header anim-stagger" style="text-align:center; padding:2rem 3rem 0; animation-delay:0.05s;">
            <div style="display:inline-block; padding:6px 18px; border-radius:50px; background:var(--watercolor-2); color:#c25a8a; font-family:'Fredoka'; font-size:0.85rem; font-weight:600; letter-spacing:1px; margin-bottom:1rem;">HELLO</div>
            <h2 style="font-family:'Playfair Display', serif; font-size:2.8rem; font-style:italic; color:var(--text); line-height:1.2; margin-bottom:0.5rem;">Let's <span class="gradient-text">Connect</span></h2>
            <p style="color:var(--text-dim); font-size:1rem; max-width:500px; margin:0 auto;">Always open to discussing new opportunities and collaborations.</p>
        </div>

        <div style="max-width:650px; margin:2rem auto; padding:0 2rem;">
            <div class="card anim-stagger" style="padding:3rem; text-align:center; animation-delay:0.15s;">
                <div style="margin-bottom:2.5rem;">
                    <div style="font-size:2.5rem; margin-bottom:1rem; opacity:0.15;">✉️</div>
                    <a href="mailto:{PROFILE['email']}" class="cta-btn" style="display:inline-block; text-decoration:none; font-size:1rem; padding:14px 36px;">
                        {PROFILE['email']}
                    </a>
                </div>

                <div style="display:flex; justify-content:center; gap:1rem; margin-bottom:2.5rem;">
                    <a href="{socials['LinkedIn']}" target="_blank" style="padding:10px 24px; border-radius:50px; background:var(--watercolor-1); color:var(--accent-3); text-decoration:none; font-weight:600; font-size:0.9rem; transition:all 0.3s;" onmouseover="this.style.background='var(--accent)'; this.style.color='#fff'" onmouseout="this.style.background='var(--watercolor-1)'; this.style.color='var(--accent-3)'">LinkedIn</a>
                    <a href="{socials['GitHub']}" target="_blank" style="padding:10px 24px; border-radius:50px; background:var(--watercolor-3); color:#4a8c65; text-decoration:none; font-weight:600; font-size:0.9rem; transition:all 0.3s;" onmouseover="this.style.background='var(--accent)'; this.style.color='#fff'" onmouseout="this.style.background='var(--watercolor-3)'; this.style.color='#4a8c65'">GitHub</a>
                </div>

                <div style="border-top:1px solid var(--border); padding-top:2rem;">
                    <h3 style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.2rem; margin-bottom:1.5rem;">Resume Versions</h3>
                    <div style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center;">
                        {resume_links}
                    </div>
                </div>

                <div style="margin-top:2.5rem; font-size:0.8rem; color:var(--text-dim);">
                    📍 {PROFILE['location']}
                </div>
             </div>
        </div>
    </div>
    """


def get_footer_html() -> str:
    social_links = ""
    if PROFILE.get('linkedin'):
        social_links += f'<a href="{PROFILE["linkedin"]}" target="_blank" class="social-link" title="LinkedIn">in</a>'
    if PROFILE.get('github'):
        social_links += f'<a href="{PROFILE["github"]}" target="_blank" class="social-link" title="GitHub">GH</a>'
    if PROFILE.get('email'):
        social_links += f'<a href="mailto:{PROFILE["email"]}" class="social-link" title="Email">@</a>'

    return f"""
    <footer class="portfolio-footer">
        <div class="footer-glow"></div>
        <div class="footer-content">
            <div class="footer-brand">SHAHID<span style="color:var(--accent)">.dev</span></div>
            <div class="footer-tagline">Crafted with 💜 by {PROFILE['name']}</div>
            <div class="footer-socials">{social_links}</div>
            <div class="footer-meta">
                &copy; 2026 &bull; Built with Streamlit &bull; Designed to inspire
            </div>
            <div class="footer-shortcut">
                Press <kbd>Ctrl+K</kbd> to open command palette
            </div>
        </div>
    </footer>
    """
