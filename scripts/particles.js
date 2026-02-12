const canvas = document.getElementById('particles-js');

if (canvas) {
    const ctx = canvas.getContext('2d');
    let particlesArray = [];

    const numberOfParticles = 50;
    const connectDistance = 100;
    const mouseRadius = 120;

    const particleColors = [
        'rgba(179, 136, 235, 0.6)',
        'rgba(232, 160, 191, 0.6)',
        'rgba(168, 213, 186, 0.5)',
        'rgba(213, 180, 247, 0.5)',
        'rgba(251, 196, 171, 0.5)'
    ];

    let mouse = {
        x: null,
        y: null,
        radius: mouseRadius
    };

    window.addEventListener('mousemove', function (event) {
        mouse.x = event.x;
        mouse.y = event.y;
    });

    class Particle {
        constructor(x, y, directionX, directionY, size, color) {
            this.x = x;
            this.y = y;
            this.directionX = directionX;
            this.directionY = directionY;
            this.size = size;
            this.color = color;
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
            ctx.fillStyle = this.color;
            ctx.fill();
        }

        update() {
            if (this.x > canvas.width || this.x < 0) {
                this.directionX = -this.directionX;
            }
            if (this.y > canvas.height || this.y < 0) {
                this.directionY = -this.directionY;
            }

            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < mouse.radius + this.size) {
                if (mouse.x < this.x && this.x < canvas.width - this.size * 10) {
                    this.x += 1.5;
                }
                if (mouse.x > this.x && this.x > this.size * 10) {
                    this.x -= 1.5;
                }
                if (mouse.y < this.y && this.y < canvas.height - this.size * 10) {
                    this.y += 1.5;
                }
                if (mouse.y > this.y && this.y > this.size * 10) {
                    this.y -= 1.5;
                }
            }

            this.x += this.directionX;
            this.y += this.directionY;
            this.draw();
        }
    }

    function init() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        particlesArray = [];
        for (let i = 0; i < numberOfParticles; i++) {
            let size = (Math.random() * 2.5) + 1;
            let x = (Math.random() * ((innerWidth - size * 2) - (size * 2)) + size * 2);
            let y = (Math.random() * ((innerHeight - size * 2) - (size * 2)) + size * 2);
            let directionX = (Math.random() * 0.3) - 0.15;
            let directionY = (Math.random() * 0.3) - 0.15;
            let color = particleColors[Math.floor(Math.random() * particleColors.length)];

            particlesArray.push(new Particle(x, y, directionX, directionY, size, color));
        }
    }

    function connect() {
        let opacityValue = 1;
        for (let a = 0; a < particlesArray.length; a++) {
            for (let b = a; b < particlesArray.length; b++) {
                let distance = ((particlesArray[a].x - particlesArray[b].x) * (particlesArray[a].x - particlesArray[b].x))
                    + ((particlesArray[a].y - particlesArray[b].y) * (particlesArray[a].y - particlesArray[b].y));

                if (distance < (canvas.width / 7) * (canvas.height / 7)) {
                    opacityValue = 1 - (distance / 20000);
                    let distMouse = Math.sqrt(
                        (particlesArray[a].x - mouse.x) ** 2 +
                        (particlesArray[a].y - mouse.y) ** 2
                    );

                    if (distMouse < 200) {
                        ctx.strokeStyle = 'rgba(179, 136, 235,' + (opacityValue * 0.3) + ')';
                        ctx.lineWidth = 0.8;
                        ctx.beginPath();
                        ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                        ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
                        ctx.stroke();
                    }
                }
            }
        }
    }

    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, innerWidth, innerHeight);

        for (let i = 0; i < particlesArray.length; i++) {
            particlesArray[i].update();
        }
        connect();
    }

    window.addEventListener('resize', function () {
        canvas.width = innerWidth;
        canvas.height = innerHeight;
        init();
    });

    setTimeout(() => {
        init();
        animate();
    }, 500);
}
