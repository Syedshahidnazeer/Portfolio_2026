const isTouchDevice = window.matchMedia('(hover: none)').matches || 'ontouchstart' in window;
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

window.addEventListener('load', () => {
    const delay = isTouchDevice ? 1200 : 2000;
    setTimeout(() => {
        const loader = document.querySelector('.loading-screen');
        if (loader) loader.classList.add('loaded');
    }, delay);
});

if (!isTouchDevice) {
    const cursorDot = document.createElement('div');
    cursorDot.className = 'cursor-dot';
    document.body.appendChild(cursorDot);

    const cursorRing = document.createElement('div');
    cursorRing.className = 'cursor-ring';
    document.body.appendChild(cursorRing);

    let mouseX = 0, mouseY = 0;
    let ringX = 0, ringY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        cursorDot.style.left = mouseX + 'px';
        cursorDot.style.top = mouseY + 'px';
    }, { passive: true });

    function animateCursorRing() {
        ringX += (mouseX - ringX) * 0.12;
        ringY += (mouseY - ringY) * 0.12;
        cursorRing.style.left = ringX + 'px';
        cursorRing.style.top = ringY + 'px';
        requestAnimationFrame(animateCursorRing);
    }
    animateCursorRing();

    document.addEventListener('mouseover', (e) => {
        const t = e.target;
        if (t.matches && t.matches('a, button, .cta-btn, .nav-item, .skill-tag, .card, .resume-chip')) {
            cursorDot.style.width = '20px';
            cursorDot.style.height = '20px';
            cursorRing.style.width = '56px';
            cursorRing.style.height = '56px';
            cursorRing.style.borderColor = 'var(--accent-2)';
        }
    });

    document.addEventListener('mouseout', (e) => {
        const t = e.target;
        if (t.matches && t.matches('a, button, .cta-btn, .nav-item, .skill-tag, .card, .resume-chip')) {
            cursorDot.style.width = '12px';
            cursorDot.style.height = '12px';
            cursorRing.style.width = '40px';
            cursorRing.style.height = '40px';
            cursorRing.style.borderColor = 'var(--accent)';
        }
    });
}

if (!isTouchDevice && !prefersReducedMotion) {
    const sparkleColors = ['#B388EB', '#E8A0BF', '#A8D5BA', '#D5B4F7', '#FFE4A0'];
    let sparkleTimer = 0;

    document.addEventListener('mousemove', (e) => {
        sparkleTimer++;
        if (sparkleTimer % 5 !== 0) return;

        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle';
        sparkle.style.left = e.clientX + 'px';
        sparkle.style.top = e.clientY + 'px';
        sparkle.style.background = sparkleColors[Math.floor(Math.random() * sparkleColors.length)];
        sparkle.style.setProperty('--dx', (Math.random() - 0.5) * 25 + 'px');
        sparkle.style.setProperty('--dy', (Math.random() - 0.5) * 25 + 'px');
        const size = Math.random() * 4 + 2 + 'px';
        sparkle.style.width = size;
        sparkle.style.height = size;
        document.body.appendChild(sparkle);

        setTimeout(() => sparkle.remove(), 700);
    }, { passive: true });
}

function setMascotEmotion(element, emotion) {
    if (!element) return;
    element.classList.remove('happy', 'surprised', 'blink', 'cheeky', 'angry', 'anxious');
    if (emotion !== 'neutral') element.classList.add(emotion);
}

function changeEmotion(emotion) {
    const mascot = document.querySelector('.mascot-face');
    if (mascot) setMascotEmotion(mascot, emotion);
}

function initMascotInteractions() {
    const mascots = document.querySelectorAll('.mascot-face');
    mascots.forEach(m => {
        if (m.dataset.initialized) return;
        m.dataset.initialized = 'true';

        if (isTouchDevice) {
            m.addEventListener('touchstart', () => {
                setMascotEmotion(m, 'surprised');
                setTimeout(() => setMascotEmotion(m, 'happy'), 300);
                setTimeout(() => setMascotEmotion(m, 'neutral'), 1500);
            }, { passive: true });
        } else {
            m.addEventListener('mouseenter', () => setMascotEmotion(m, 'cheeky'));
            m.addEventListener('mouseleave', () => setMascotEmotion(m, 'neutral'));
            m.addEventListener('click', () => {
                setMascotEmotion(m, 'surprised');
                setTimeout(() => setMascotEmotion(m, 'happy'), 300);
                setTimeout(() => setMascotEmotion(m, 'neutral'), 1500);
            });
        }
    });
}

initMascotInteractions();

if (!isTouchDevice) {
    document.addEventListener('mousemove', (e) => {
        const mascotFace = document.querySelector('.mascot-face');
        if (mascotFace && (mascotFace.classList.contains('happy') || mascotFace.classList.contains('blink'))) return;

        const pupils = document.querySelectorAll('.mascot-face .pupil');
        pupils.forEach(pupil => {
            const eye = pupil.parentElement;
            const eyeRect = eye.getBoundingClientRect();
            const eyeCenterX = eyeRect.left + eyeRect.width / 2;
            const eyeCenterY = eyeRect.top + eyeRect.height / 2;

            const angle = Math.atan2(e.clientY - eyeCenterY, e.clientX - eyeCenterX);
            const distance = Math.min(12, Math.hypot(e.clientX - eyeCenterX, e.clientY - eyeCenterY) / 10);

            const x = Math.cos(angle) * distance;
            const y = Math.sin(angle) * distance;

            pupil.style.transform = `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`;
        });
    }, { passive: true });
}

window.switchView = function (viewName) {
    document.querySelectorAll('.view-section').forEach(v => {
        v.classList.remove('active-view', 'fade-in');
        v.style.display = 'none';
    });

    const target = document.getElementById('view-' + viewName);
    if (target) {
        target.style.display = 'block';
        void target.offsetWidth;
        target.classList.add('active-view', 'fade-in');

        setTimeout(() => {
            initSpotlight();
            initCounters();
        }, 100);
    }

    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
    const link = document.getElementById('link-' + viewName);
    if (link) link.classList.add('active');

    window.scrollTo({ top: 0, behavior: 'smooth' });
};

setInterval(() => {
    const mascotFace = document.querySelector('.mascot-face');
    if (mascotFace && mascotFace.classList.length === 1) {
        changeEmotion('blink');
        setTimeout(() => changeEmotion('neutral'), 200);
    }
}, 4000);

function typeWriter(elementId, text, speed = 50) {
    const el = document.getElementById(elementId);
    if (!el) return;
    el.innerHTML = '';
    let i = 0;
    function type() {
        if (i < text.length) {
            el.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    setTimeout(type, 500);
}

setTimeout(() => {
    const heroTitle = document.getElementById('hero-typed');
    if (heroTitle) {
        const text = heroTitle.dataset.text || heroTitle.textContent;
        typeWriter('hero-typed', text, 60);
    }
}, 2200);

function animateCounter(el, target, duration = 1800) {
    const startTime = performance.now();
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(eased * target);
        if (progress < 1) requestAnimationFrame(update);
        else el.textContent = target;
    }
    requestAnimationFrame(update);
}

function initCounters() {
    document.querySelectorAll('.counter-val').forEach(counter => {
        if (counter.dataset.animated) return;
        counter.dataset.animated = 'true';
        const target = parseInt(counter.dataset.target, 10);
        if (!isNaN(target)) animateCounter(counter, target);
    });
}

setTimeout(initCounters, 2500);

let scrollTicking = false;
function updateScrollProgress() {
    const bar = document.querySelector('.scroll-progress');
    if (!bar) return;
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (scrollHeight > 0) {
        bar.style.width = Math.min((window.scrollY / scrollHeight) * 100, 100) + '%';
    }
    scrollTicking = false;
}
window.addEventListener('scroll', () => {
    if (!scrollTicking) {
        requestAnimationFrame(updateScrollProgress);
        scrollTicking = true;
    }
}, { passive: true });

function initSpotlight() {
    document.querySelectorAll('.spotlight-card').forEach(card => {
        if (card.dataset.spotlightInit) return;
        card.dataset.spotlightInit = 'true';
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            card.style.setProperty('--x', `${e.clientX - rect.left}px`);
            card.style.setProperty('--y', `${e.clientY - rect.top}px`);
        });
    });
}

setTimeout(initSpotlight, 500);

if (!isTouchDevice) {
    document.querySelectorAll('.cta-btn').forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            btn.style.transform = `translate(${x * 0.12}px, ${y * 0.12}px) scale(1.03)`;
        });
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = '';
        });
    });
}

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            entry.target.style.transition = 'opacity 0.8s cubic-bezier(0.25, 0.8, 0.25, 1), transform 0.8s cubic-bezier(0.25, 0.8, 0.25, 1)';
        }
    });
}, { threshold: 0.1 });

setTimeout(() => {
    document.querySelectorAll('.card').forEach(card => {
        revealObserver.observe(card);
    });
}, 3000);

const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
let konamiIndex = 0;

document.addEventListener('keydown', (e) => {
    if (e.key === konamiSequence[konamiIndex]) {
        konamiIndex++;
        if (konamiIndex === konamiSequence.length) {
            konamiIndex = 0;
            triggerKonamiEasterEgg();
        }
    } else {
        konamiIndex = 0;
    }
});

function triggerKonamiEasterEgg() {
    const colors = ['#B388EB', '#E8A0BF', '#A8D5BA', '#FFE4A0', '#D5B4F7', '#F5D5E8'];
    const duration = 4000;
    const end = Date.now() + duration;

    function frame() {
        for (let i = 0; i < 6; i++) {
            const particle = document.createElement('div');
            particle.style.cssText = `
                position: fixed;
                width: ${Math.random() * 12 + 6}px;
                height: ${Math.random() * 12 + 6}px;
                background: ${colors[Math.floor(Math.random() * colors.length)]};
                left: ${Math.random() * 100}vw;
                top: -20px;
                z-index: 99999;
                pointer-events: none;
                border-radius: ${Math.random() > 0.5 ? '50%' : '3px'};
                animation: confettiFall ${Math.random() * 2 + 2}s linear forwards;
            `;
            document.body.appendChild(particle);
            setTimeout(() => particle.remove(), 4000);
        }
        if (Date.now() < end) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);

    changeEmotion('surprised');
    setTimeout(() => changeEmotion('happy'), 500);
    setTimeout(() => changeEmotion('cheeky'), 1500);
    setTimeout(() => changeEmotion('neutral'), 3000);

    const msg = document.createElement('div');
    msg.innerHTML = '🎮 Achievement Unlocked: <b>Secret Code Master!</b>';
    msg.style.cssText = `
        position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%);
        padding: 16px 32px; border-radius: 50px; z-index: 99999;
        background: var(--glass); backdrop-filter: blur(20px);
        border: 1px solid var(--accent); color: var(--text);
        font-size: 0.9rem; font-weight: 600;
        box-shadow: 0 8px 32px rgba(179, 136, 235, 0.3);
        animation: slideUpFade 0.5s ease forwards;
    `;
    document.body.appendChild(msg);
    setTimeout(() => {
        msg.style.opacity = '0';
        msg.style.transition = 'opacity 0.5s';
        setTimeout(() => msg.remove(), 500);
    }, 3500);
}

const confettiStyle = document.createElement('style');
confettiStyle.textContent = `
    @keyframes confettiFall {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(${Math.random() * 720}deg); opacity: 0; }
    }
`;
document.head.appendChild(confettiStyle);

function setTimeGreeting() {
    const el = document.getElementById('time-greeting');
    if (!el) return;
    const hour = new Date().getHours();
    let greeting, emoji;
    if (hour >= 5 && hour < 12) { greeting = 'Good Morning'; emoji = '☀️'; }
    else if (hour >= 12 && hour < 17) { greeting = 'Good Afternoon'; emoji = '🌤️'; }
    else if (hour >= 17 && hour < 21) { greeting = 'Good Evening'; emoji = '🌅'; }
    else { greeting = 'Good Night'; emoji = '🌙'; }
    el.textContent = `${emoji} ${greeting}! Welcome to my portfolio.`;
}
setTimeout(setTimeGreeting, 2300);

const roles = [
    'AI/ML Solutions Engineer',
    'Data Science Specialist',
    'Cloud Architecture Enthusiast',
    'Full-Stack Problem Solver'
];
let roleIndex = 0;
let roleCharIndex = 0;
let roleDeleting = false;

function cycleRoles() {
    const el = document.getElementById('role-text');
    if (!el) return;

    const currentRole = roles[roleIndex];

    if (!roleDeleting) {
        el.textContent = currentRole.substring(0, roleCharIndex + 1);
        roleCharIndex++;

        if (roleCharIndex === currentRole.length) {
            setTimeout(() => { roleDeleting = true; cycleRoles(); }, 2000);
            return;
        }
        setTimeout(cycleRoles, 55);
    } else {
        el.textContent = currentRole.substring(0, roleCharIndex - 1);
        roleCharIndex--;

        if (roleCharIndex === 0) {
            roleDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            setTimeout(cycleRoles, 400);
            return;
        }
        setTimeout(cycleRoles, 30);
    }
}

setTimeout(cycleRoles, 4000);

if (isTouchDevice && window.DeviceOrientationEvent) {
    window.addEventListener('deviceorientation', (e) => {
        const pupils = document.querySelectorAll('.mascot-face .pupil');
        if (!pupils.length) return;

        const gamma = e.gamma || 0;
        const beta = e.beta || 0;

        const x = Math.max(-12, Math.min(12, gamma / 4));
        const y = Math.max(-12, Math.min(12, (beta - 45) / 4));

        pupils.forEach(pupil => {
            pupil.style.transform = `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`;
        });
    }, { passive: true });
}

let helloCount = 0;
const helloMessages = [
    'Nice to meet you! 👋',
    'Thanks for visiting! ✨',
    'You look great today! 🌟',
    'Let\'s build something amazing! 🚀',
    'I appreciate you being here! 💜'
];

window.sayHello = function () {
    changeEmotion('happy');
    setTimeout(() => changeEmotion('surprised'), 600);
    setTimeout(() => changeEmotion('cheeky'), 1200);
    setTimeout(() => changeEmotion('neutral'), 2500);

    const msg = document.createElement('div');
    msg.textContent = helloMessages[helloCount % helloMessages.length];
    msg.style.cssText = `
        position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%) scale(0);
        padding: 20px 40px; border-radius: 24px; z-index: 99999;
        background: var(--glass); backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border); color: var(--text);
        font-size: 1.1rem; font-weight: 600;
        box-shadow: 0 16px 48px rgba(179, 136, 235, 0.2);
        transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.5s;
    `;
    document.body.appendChild(msg);

    requestAnimationFrame(() => {
        msg.style.transform = 'translate(-50%, -50%) scale(1)';
    });

    setTimeout(() => {
        msg.style.transform = 'translate(-50%, -50%) scale(0)';
        msg.style.opacity = '0';
        setTimeout(() => msg.remove(), 500);
    }, 2000);

    for (let i = 0; i < 12; i++) {
        const p = document.createElement('div');
        const colors = ['#B388EB', '#E8A0BF', '#A8D5BA', '#FFE4A0'];
        p.style.cssText = `
            position: fixed; width: 8px; height: 8px;
            background: ${colors[i % colors.length]};
            border-radius: 50%; pointer-events: none; z-index: 99999;
            left: 50%; top: 50%;
            animation: confettiBurst 0.8s ease-out forwards;
            --angle: ${(i / 12) * 360}deg;
        `;
        document.body.appendChild(p);
        setTimeout(() => p.remove(), 800);
    }

    helloCount++;
};

const burstStyle = document.createElement('style');
burstStyle.textContent = `
    @keyframes confettiBurst {
        0% { transform: translate(-50%, -50%) rotate(0deg); opacity: 1; }
        100% {
            transform: translate(
                calc(-50% + cos(var(--angle)) * 120px),
                calc(-50% + sin(var(--angle)) * 120px)
            ) rotate(720deg);
            opacity: 0;
        }
    }
`;
document.head.appendChild(burstStyle);

let scrollTopTicking = false;
window.addEventListener('scroll', () => {
    if (!scrollTopTicking) {
        requestAnimationFrame(() => {
            const btn = document.getElementById('scroll-top-btn');
            if (btn) {
                if (window.scrollY > 400) {
                    btn.classList.add('visible');
                } else {
                    btn.classList.remove('visible');
                }
            }
            scrollTopTicking = false;
        });
        scrollTopTicking = true;
    }
}, { passive: true });

const cmdItems = [
    { icon: '&#127968;', label: 'Home', action: () => switchView('main'), shortcut: '1' },
    { icon: '&#127891;', label: 'Education', action: () => switchView('education'), shortcut: '2' },
    { icon: '&#128188;', label: 'Experience', action: () => switchView('experience'), shortcut: '3' },
    { icon: '&#9889;', label: 'Skills', action: () => switchView('skills'), shortcut: '4' },
    { icon: '&#128640;', label: 'Projects', action: () => switchView('projects'), shortcut: '5' },
    { icon: '&#127942;', label: 'Certifications', action: () => switchView('certifications'), shortcut: '6' },
    { icon: '&#128231;', label: 'Contact', action: () => switchView('contact'), shortcut: '7' },
    { icon: '&#127769;', label: 'Toggle Dark Mode', action: () => { if (typeof toggleDarkMode === 'function') toggleDarkMode(); }, shortcut: 'D' },
    { icon: '&#128279;', label: 'Copy Portfolio Link', action: () => sharePortfolio(), shortcut: '' },
    { icon: '&#127916;', label: 'Matrix Mode', action: () => toggleMatrix(), shortcut: '' },
];

let cmdPaletteOpen = false;
let cmdSelectedIndex = 0;

window.openCmdPalette = function () {
    const overlay = document.getElementById('cmd-palette-overlay');
    const input = document.getElementById('cmd-palette-input');
    if (!overlay) return;
    overlay.classList.add('active');
    cmdPaletteOpen = true;
    cmdSelectedIndex = 0;
    if (input) { input.value = ''; input.focus(); }
    renderCmdItems('');
};

window.closeCmdPalette = function (e) {
    if (e && e.target !== document.getElementById('cmd-palette-overlay')) return;
    const overlay = document.getElementById('cmd-palette-overlay');
    if (overlay) overlay.classList.remove('active');
    cmdPaletteOpen = false;
};

function renderCmdItems(query) {
    const container = document.getElementById('cmd-palette-items');
    if (!container) return;

    const filtered = cmdItems.filter(item =>
        item.label.toLowerCase().includes(query.toLowerCase())
    );

    container.innerHTML = filtered.map((item, i) => `
        <div class="cmd-palette-item ${i === cmdSelectedIndex ? 'selected' : ''}"
             onclick="executeCmdItem(${cmdItems.indexOf(item)})"
             onmouseenter="cmdSelectedIndex=${i}; renderCmdItems(document.getElementById('cmd-palette-input').value)">
            <span class="cmd-icon">${item.icon}</span>
            <span>${item.label}</span>
            ${item.shortcut ? `<span class="cmd-shortcut">${item.shortcut}</span>` : ''}
        </div>
    `).join('');
}

window.executeCmdItem = function (index) {
    cmdItems[index].action();
    const overlay = document.getElementById('cmd-palette-overlay');
    if (overlay) overlay.classList.remove('active');
    cmdPaletteOpen = false;
};

document.getElementById('cmd-palette-input')?.addEventListener('input', (e) => {
    cmdSelectedIndex = 0;
    renderCmdItems(e.target.value);
});

if (!isTouchDevice) {
    function initTiltCards() {
        document.querySelectorAll('.card').forEach(card => {
            if (card.dataset.tiltInit) return;
            card.dataset.tiltInit = 'true';

            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;

                const rotateX = -(y - centerY) / 20;
                const rotateY = (x - centerX) / 20;

                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = '';
                card.style.transition = 'transform 0.5s cubic-bezier(0.22, 0.61, 0.36, 1)';
                setTimeout(() => { card.style.transition = ''; }, 500);
            });
        });
    }
    setTimeout(initTiltCards, 3500);
}

let matrixActive = false;
let matrixInterval = null;

window.toggleMatrix = function () {
    const canvas = document.getElementById('matrix-canvas');
    if (!canvas) return;

    matrixActive = !matrixActive;

    if (matrixActive) {
        canvas.classList.add('active');
        startMatrixRain(canvas);
    } else {
        canvas.classList.remove('active');
        if (matrixInterval) clearInterval(matrixInterval);
    }
};

function startMatrixRain(canvas) {
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()_+-=[]{}|;:,.<>?'.split('');
    const fontSize = 14;
    const columns = Math.floor(canvas.width / fontSize);
    const drops = Array(columns).fill(1);

    const isDark = document.body.classList.contains('dark-mode');
    const color = isDark ? '#B388EB' : '#957DAD';

    function draw() {
        ctx.fillStyle = isDark ? 'rgba(12, 10, 20, 0.06)' : 'rgba(253, 248, 244, 0.06)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = color;
        ctx.font = fontSize + 'px monospace';

        for (let i = 0; i < drops.length; i++) {
            const char = chars[Math.floor(Math.random() * chars.length)];
            ctx.fillText(char, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }

    if (matrixInterval) clearInterval(matrixInterval);
    matrixInterval = setInterval(draw, 35);
}

window.addEventListener('resize', () => {
    const canvas = document.getElementById('matrix-canvas');
    if (canvas && matrixActive) {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
});

window.sharePortfolio = function () {
    const url = window.location.href;
    if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(() => {
            const toast = document.getElementById('share-toast');
            if (toast) {
                toast.classList.add('visible');
                setTimeout(() => toast.classList.remove('visible'), 2500);
            }
        });
    }
};

function updateFavicon() {
    const isDark = document.body.classList.contains('dark-mode');
    const emoji = isDark ? '🌙' : '☀️';
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y="80" font-size="80">${emoji}</text></svg>`;
    let link = document.querySelector("link[rel*='icon']");
    if (!link) {
        link = document.createElement('link');
        link.rel = 'icon';
        document.head.appendChild(link);
    }
    link.href = 'data:image/svg+xml,' + encodeURIComponent(svg);
}

const origToggle = window.toggleDarkMode;
if (typeof origToggle === 'function') {
    window.toggleDarkMode = function () {
        origToggle();
        updateFavicon();
    };
}
setTimeout(updateFavicon, 2500);

const sectionMoods = {
    'main': 'neutral',
    'education': 'happy',
    'experience': 'cheeky',
    'skills': 'surprised',
    'projects': 'happy',
    'certifications': 'cheeky',
    'contact': 'happy'
};

const origSwitchView = window.switchView;
if (typeof origSwitchView === 'function') {
    window.switchView = function (viewId) {
        origSwitchView(viewId);
        const mood = sectionMoods[viewId] || 'neutral';
        setTimeout(() => changeEmotion(mood), 600);
        setTimeout(() => changeEmotion('neutral'), 3000);
    };
}

document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        if (cmdPaletteOpen) {
            closeCmdPalette();
        } else {
            openCmdPalette();
        }
        return;
    }

    if (e.key === 'Escape' && cmdPaletteOpen) {
        closeCmdPalette();
        return;
    }

    if (cmdPaletteOpen) {
        const input = document.getElementById('cmd-palette-input');
        const query = input ? input.value : '';
        const filtered = cmdItems.filter(item =>
            item.label.toLowerCase().includes(query.toLowerCase())
        );

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            cmdSelectedIndex = Math.min(cmdSelectedIndex + 1, filtered.length - 1);
            renderCmdItems(query);
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            cmdSelectedIndex = Math.max(cmdSelectedIndex - 1, 0);
            renderCmdItems(query);
        } else if (e.key === 'Enter' && filtered.length > 0) {
            e.preventDefault();
            const realIndex = cmdItems.indexOf(filtered[cmdSelectedIndex]);
            executeCmdItem(realIndex);
        }
        return;
    }

    const viewMap = { '1': 'main', '2': 'education', '3': 'experience', '4': 'skills', '5': 'projects', '6': 'certifications', '7': 'contact' };
    if (viewMap[e.key] && !e.ctrlKey && !e.altKey && !e.metaKey) {
        switchView(viewMap[e.key]);
    }

    if (e.key === 'd' && !e.ctrlKey && !e.altKey && !e.metaKey) {
        if (typeof toggleDarkMode === 'function') toggleDarkMode();
    }

    if (e.key === 's' && !e.ctrlKey && !e.altKey && !e.metaKey) {
        sharePortfolio();
    }
});

let matrixWord = '';
document.addEventListener('keypress', (e) => {
    if (cmdPaletteOpen) return;
    matrixWord += e.key.toLowerCase();
    if (matrixWord.length > 6) matrixWord = matrixWord.slice(-6);
    if (matrixWord === 'matrix') {
        toggleMatrix();
        matrixWord = '';
    }
});
