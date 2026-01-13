
/* Mascot Interaction Logic */
// Helper to change emotion on a specific mascot element
function setMascotEmotion(element, emotion) {
    if (!element) return;
    // Remove all state classes from THIS element
    element.classList.remove('happy', 'surprised', 'cheeky', 'blink', 'angry');

    // Add new state if not neutral
    if (emotion !== 'neutral') {
        element.classList.add(emotion);
    }
}

// Initialize interactions for all mascots
function initMascotInteractions() {
    const mascots = document.querySelectorAll('.view-mascot, .mascot-face');

    mascots.forEach(m => {
        // Avoid double binding if run multiple times
        if (m.dataset.hasInteractions) return;
        m.dataset.hasInteractions = "true";

        m.addEventListener('mouseenter', () => {
            // Experience -> Angry
            if (m.id === 'mascot-experience') {
                setMascotEmotion(m, 'angry');
            }
            // Education -> Anxious/Shy
            else if (m.id === 'mascot-education') {
                setMascotEmotion(m, 'anxious');
            }
            else {
                setMascotEmotion(m, 'cheeky');
            }
        });
        m.addEventListener('mouseleave', () => setMascotEmotion(m, 'neutral'));

        m.addEventListener('click', () => {
            setMascotEmotion(m, 'surprised');
        });

        // Scroll (Wheel) Logic
        m.addEventListener('wheel', () => {
            // Define reaction based on ID
            let reaction = 'angry'; // Default reaction
            if (m.id === 'mascot-education') reaction = 'anxious'; // Education gets anxious

            setMascotEmotion(m, reaction);

            clearTimeout(m.angryTimer);
            m.angryTimer = setTimeout(() => {
                // If mouse still hovering...
                if (m.matches(':hover')) {
                    // Check specific ID again to persist correct emotion
                    if (m.id === 'mascot-experience') setMascotEmotion(m, 'angry');
                    else if (m.id === 'mascot-education') setMascotEmotion(m, 'anxious');
                    else setMascotEmotion(m, 'neutral'); // Default return
                } else {
                    setMascotEmotion(m, 'neutral');
                }
            }, 800);
        }, { passive: true });

        // Touch Support
        m.addEventListener('touchstart', (e) => {
            // e.preventDefault(); // removed to allow scrolling unless critical
            setMascotEmotion(m, 'surprised');
        }, { passive: true });

        m.addEventListener('touchend', () => {
            setTimeout(() => setMascotEmotion(m, 'neutral'), 500);
        });
    });
}

// Run init
initMascotInteractions();
// Re-run on view switch (in case of re-render) - Hook into global switchView if possible or Observer
setInterval(initMascotInteractions, 1000); // Polling for simplicity in Streamlit env


// Eye Tracking Logic
document.addEventListener('mousemove', (e) => {
    // Only track if neutral/surprised (not happy/blink which alter eye shape)
    if (mascot && (mascot.classList.contains('happy') || mascot.classList.contains('blink'))) return;

    const pupils = document.querySelectorAll('.pupil');
    const mascotFace = document.querySelector('.mascot-face');

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

    if (mascotFace) {
        // Multiplier 60 -> Higher number = Less movement
        const x = (window.innerWidth / 2 - e.clientX) / 60;
        const y = (window.innerHeight / 2 - e.clientY) / 60;
        mascotFace.style.transform = `translate(${x}px, ${y}px)`;
    }
});

/* ===========================
   3D TILT EFFECT LOGIC
   =========================== */
function initTilt() {
    const cards = document.querySelectorAll('.project-tilt-card');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            // Calculate mouse position relative to card center
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            // Rotation Multipliers (Adjust for sensitivity)
            // Divide by larger number = less rotation
            const rotateX = (y / -20).toFixed(2); // Invert Y axis for natural tilt
            const rotateY = (x / 20).toFixed(2);

            // Apply Transform
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        });

        card.addEventListener('mouseleave', () => {
            // Reset on leave
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
        });
    });
}

// Initialize Tilt on Load and View Switch
setTimeout(initTilt, 500);

// View Switching Logic (Global Scope)
const originalSwitch = window.switchView || function (v) { }; // Define ref if not exists

window.switchView = function (viewName) {
    document.querySelectorAll('.view-section').forEach(el => {
        el.style.display = 'none';
        el.classList.remove('active-view');
    });
    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));

    const target = document.getElementById('view-' + viewName);
    if (target) {
        target.style.display = 'block';
        setTimeout(() => target.classList.add('active-view'), 10);
        const link = document.getElementById('link-' + viewName);
        if (link) link.classList.add('active');

        // Re-init tilt if switching to projects
        if (viewName === 'projects') {
            setTimeout(initTilt, 100);
        }
    }
};

// Random Blinking
setInterval(() => {
    if (mascot && mascot.classList.length === 1) { // 1 class means just 'mascot-face' (neutral)
        changeEmotion('blink');
        setTimeout(() => changeEmotion('neutral'), 200);
    }
}, 4000);
