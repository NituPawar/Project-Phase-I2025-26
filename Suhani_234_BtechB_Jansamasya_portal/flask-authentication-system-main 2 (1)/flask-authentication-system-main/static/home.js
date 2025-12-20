document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map
    initMap();
    
    // Animate stats counting
    animateStats();
    
    // Add smooth scroll to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Add hover effects to cards
    const cards = document.querySelectorAll('.feature-card, .issue-card, .stat-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = card.classList.contains('feature-card') ? 'translateY(-10px)' : 'translateY(-5px)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
    
    // Add intersection observer for animations
    const observerOptions = {
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.feature-card, .stat-card, .issue-card, .section-header').forEach(el => {
        observer.observe(el);
    });
});

function initMap() {
    // Check if map container exists
    if (!document.getElementById('issuesMap')) return;
    
    // Load Leaflet only when needed
    const script = document.createElement('script');
    script.src = 'https://unpkg.com/leaflet@1.9.3/dist/leaflet.js';
    script.onload = function() {
        // Create map centered on a default location (you should replace with your city's coordinates)
        const map = L.map('issuesMap').setView([28.6139, 77.2090], 12); // Default to New Delhi
        
        // Add tile layer (OpenStreetMap)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
        
        // Sample issue data (in a real app, this would come from your backend)
        const issues = [
            {
                lat: 28.6139,
                lng: 77.2090,
                title: "Pothole on Main Road",
                category: "Road & Infrastructure",
                priority: "high",
                status: "pending"
            },
            {
                lat: 28.6239,
                lng: 77.2190,
                title: "Garbage Not Collected",
                category: "Sanitation & Waste",
                priority: "medium",
                status: "in-progress"
            },
            {
                lat: 28.6039,
                lng: 77.1990,
                title: "Broken Streetlight",
                category: "Public Utilities",
                priority: "low",
                status: "resolved"
            }
        ];
        
        // Define custom icons
        const highPriorityIcon = L.divIcon({
            className: 'custom-icon high-priority',
            html: '<i class="fas fa-exclamation-circle"></i>',
            iconSize: [30, 30]
        });
        
        const mediumPriorityIcon = L.divIcon({
            className: 'custom-icon medium-priority',
            html: '<i class="fas fa-exclamation-triangle"></i>',
            iconSize: [30, 30]
        });
        
        const lowPriorityIcon = L.divIcon({
            className: 'custom-icon low-priority',
            html: '<i class="fas fa-info-circle"></i>',
            iconSize: [30, 30]
        });
        
        const resolvedIcon = L.divIcon({
            className: 'custom-icon resolved',
            html: '<i class="fas fa-check-circle"></i>',
            iconSize: [30, 30]
        });
        
        // Add markers for each issue
        issues.forEach(issue => {
            let icon;
            if (issue.status === "resolved") {
                icon = resolvedIcon;
            } else {
                switch(issue.priority) {
                    case "high":
                        icon = highPriorityIcon;
                        break;
                    case "medium":
                        icon = mediumPriorityIcon;
                        break;
                    default:
                        icon = lowPriorityIcon;
                }
            }
            
            const marker = L.marker([issue.lat, issue.lng], { icon }).addTo(map);
            marker.bindPopup(`
                <div class="map-popup">
                    <h4>${issue.title}</h4>
                    <p><strong>Category:</strong> ${issue.category}</p>
                    <p><strong>Status:</strong> ${issue.status.replace('-', ' ')}</p>
                    <p><strong>Priority:</strong> ${issue.priority}</p>
                    <a href="#" class="popup-link">View Details</a>
                </div>
            `);
        });
        
        // Add custom CSS for icons
        const style = document.createElement('style');
        style.textContent = `
            .custom-icon {
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                border-radius: 50%;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }
            .high-priority {
                background-color: #F44336;
            }
            .medium-priority {
                background-color: #FFC107;
            }
            .low-priority {
                background-color: #4CAF50;
            }
            .resolved {
                background-color: #2196F3;
            }
            .map-popup {
                min-width: 200px;
            }
            .map-popup h4 {
                margin: 0 0 10px;
                color: var(--primary-dark);
            }
            .map-popup p {
                margin: 5px 0;
                font-size: 0.9rem;
            }
            .popup-link {
                display: inline-block;
                margin-top: 10px;
                color: var(--primary-color);
                font-weight: bold;
                font-size: 0.9rem;
            }
        `;
        document.head.appendChild(style);
    };
    document.head.appendChild(script);
}

function animateStats() {
    const statCards = document.querySelectorAll('.stat-card');
    if (!statCards.length) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statNumber = entry.target.querySelector('.stat-number');
                const target = parseInt(statNumber.textContent.replace(/[^0-9]/g, ''));
                const duration = 2000;
                const start = 0;
                const increment = target / (duration / 16);
                
                let current = start;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        clearInterval(timer);
                        current = target;
                    }
                    statNumber.textContent = Math.floor(current) + (statNumber.textContent.includes('%') ? '%' : '+');
                }, 16);
                
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    statCards.forEach(card => {
        observer.observe(card);
    });
}