// Initialize the map when the page loads
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the issues map
    initIssuesMap();
    
    // Add smooth scrolling for anchor links
    setupSmoothScrolling();
    
    // Add animation effects
    setupAnimations();
    
    // Set up any event listeners
    setupEventListeners();
});

// Initialize the Leaflet map with reported issues
function initIssuesMap() {
    // Check if the map container exists
    if (!document.getElementById('issuesMap')) return;

    // Initialize the map centered on a default location (you can adjust these coordinates)
    const map = L.map('issuesMap').setView([27.7172, 85.3240], 12); // Default to Kathmandu coordinates

    // Add the OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Sample issue data - in a real app, this would come from your backend API
    const issues = [
        {
            id: 1,
            title: "Large Pothole on Main Road",
            category: "Road & Infrastructure",
            status: "in_progress",
            priority: "high",
            lat: 27.7172,
            lng: 85.3240,
            description: "A large pothole causing traffic issues",
            date: "2023-05-15",
            image: "https://images.unsplash.com/photo-1561484930-974554019ade?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
        },
        {
            id: 2,
            title: "Garbage Not Collected",
            category: "Sanitation & Waste",
            status: "pending",
            priority: "medium",
            lat: 27.7200,
            lng: 85.3300,
            description: "Garbage accumulation for 5 days",
            date: "2023-05-18",
            image: "https://images.unsplash.com/photo-1581578731548-c64695cc6952?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
        },
        {
            id: 3,
            title: "Streetlight Not Working",
            category: "Electricity",
            status: "resolved",
            priority: "low",
            lat: 27.7150,
            lng: 85.3200,
            description: "Streetlight pole #45 non-functional",
            date: "2023-05-10",
            image: "https://images.unsplash.com/photo-1517649763962-0c623066013b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
        }
    ];

    // Define icon colors based on priority
    const priorityColors = {
        high: '#F44336',
        medium: '#FFC107',
        low: '#4CAF50',
        resolved: '#2196F3'
    };

    // Add markers for each issue
    issues.forEach(issue => {
        const markerColor = priorityColors[issue.priority] || '#9b59b6';
        
        const marker = L.marker([issue.lat, issue.lng], {
            icon: L.divIcon({
                className: 'custom-marker',
                html: `<div style="background-color: ${markerColor}"></div>`,
                iconSize: [25, 41],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34]
            })
        }).addTo(map);
        
        // Add popup with issue information
        marker.bindPopup(`
            <div class="map-popup">
                <h3>${issue.title}</h3>
                <p><strong>Category:</strong> ${issue.category}</p>
                <p><strong>Status:</strong> ${issue.status.replace('_', ' ')}</p>
                <p><strong>Date:</strong> ${issue.date}</p>
                <img src="${issue.image}" alt="${issue.title}" style="max-width: 100%; height: auto; margin-top: 10px;">
                <div style="margin-top: 10px;">
                    <a href="/issue/${issue.id}" class="btn btn-primary btn-sm">View Details</a>
                </div>
            </div>
        `);
    });

    // Try to get the user's location and center the map there
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const { latitude, longitude } = position.coords;
                map.setView([latitude, longitude], 14);
                
                // Add a marker for the user's location
                L.marker([latitude, longitude], {
                    icon: L.divIcon({
                        className: 'user-location-marker',
                        html: '<i class="fas fa-user"></i>',
                        iconSize: [30, 30],
                        iconAnchor: [15, 15]
                    })
                }).addTo(map)
                .bindPopup('Your Location').openPopup();
            },
            (error) => {
                console.log('Geolocation error:', error);
                // Use default location if geolocation fails
            }
        );
    }
}

// Set up smooth scrolling for anchor links
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Add animation effects to elements
function setupAnimations() {
    // Animate stats counters
    const statCards = document.querySelectorAll('.stat-card');
    if (statCards.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target.querySelector('.stat-number'));
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        statCards.forEach(card => observer.observe(card));
    }
    
    // Add fade-in animation to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    });
}

// Animate counter numbers
function animateCounter(element) {
    if (!element) return;
    
    const target = parseInt(element.textContent.replace(/[^0-9]/g, ''));
    const duration = 2000; // Animation duration in ms
    const start = 0;
    const increment = target / (duration / 16); // 60fps
    
    let current = start;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            clearInterval(timer);
            current = target;
        }
        
        // Check if the original text had a + or other suffix
        const suffix = element.textContent.match(/[^0-9]+$/)?.[0] || '';
        element.textContent = Math.floor(current) + suffix;
    }, 16);
}

// Set up event listeners for interactive elements
function setupEventListeners() {
    // Make issue cards clickable
    document.querySelectorAll('.issue-card').forEach(card => {
        card.style.cursor = 'pointer';
        card.addEventListener('click', function(e) {
            // Don't navigate if the click was on a link inside the card
            if (e.target.tagName === 'A' || e.target.closest('a')) return;
            
            const link = this.querySelector('a.issue-link');
            if (link) {
                window.location.href = link.href;
            }
        });
    });
    
    // Add hover effects to feature cards
    document.querySelectorAll('.feature-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.querySelector('.feature-icon').style.transform = 'scale(1.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.querySelector('.feature-icon').style.transform = 'scale(1)';
        });
    });
}

// Utility function to load Leaflet JS dynamically if not already loaded
function loadLeafletJS() {
    if (typeof L === 'undefined') {
        const script = document.createElement('script');
        script.src = 'https://unpkg.com/leaflet@1.9.3/dist/leaflet.js';
        script.onload = initIssuesMap;
        document.head.appendChild(script);
    } else {
        initIssuesMap();
    }
}

// Load Leaflet JS if the map is on the page
if (document.getElementById('issuesMap')) {
    loadLeafletJS();
}
// Initialize the location map when the page loads
document.addEventListener('DOMContentLoaded', function() {
    // Check if the location map container exists
    if (!document.getElementById('locationMap')) return;

    // Initialize the map
    initLocationMap();
});

function initLocationMap() {
    // Default coordinates (center of Nepal)
    const defaultLat = 28.3949;
    const defaultLng = 84.1240;
    const defaultZoom = 7;

    // Initialize the map
    const map = L.map('locationMap').setView([defaultLat, defaultLng], defaultZoom);

    // Add the OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Create a marker variable (we'll reuse this)
    let marker = null;

    // Try to get the user's current location
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                const userLat = position.coords.latitude;
                const userLng = position.coords.longitude;
                
                // Center map on user's location
                map.setView([userLat, userLng], 15);
                
                // Add marker at user's location
                placeMarker(userLat, userLng);
            },
            function(error) {
                console.log('Geolocation error:', error);
                // Use default location if geolocation fails
                placeMarker(defaultLat, defaultLng);
            },
            {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0
            }
        );
    } else {
        // Browser doesn't support geolocation
        placeMarker(defaultLat, defaultLng);
    }

    // Add click event to place/update marker
    map.on('click', function(e) {
        placeMarker(e.latlng.lat, e.latlng.lng);
    });

    // Function to place or update the marker
    function placeMarker(lat, lng) {
        // Update the hidden input fields
        document.getElementById('latitude').value = lat;
        document.getElementById('longitude').value = lng;

        // Remove existing marker if it exists
        if (marker) {
            map.removeLayer(marker);
        }

        // Add new marker
        marker = L.marker([lat, lng], {
            draggable: true,
            icon: L.divIcon({
                className: 'location-marker',
                html: '<i class="fas fa-map-marker-alt"></i>',
                iconSize: [30, 30],
                iconAnchor: [15, 30]
            })
        }).addTo(map);

        // Update position when marker is dragged
        marker.on('dragend', function(e) {
            const newLatLng = e.target.getLatLng();
            document.getElementById('latitude').value = newLatLng.lat;
            document.getElementById('longitude').value = newLatLng.lng;
        });
    }

    // Add search control
    const searchControl = L.control.search({
        position: 'topright',
        layer: L.layerGroup(),
        initial: false,
        zoom: 15,
        marker: false,
        autoType: false,
        autoCollapse: true,
        textPlaceholder: 'Search location...'
    });

    searchControl.on('search:locationfound', function(e) {
        placeMarker(e.latlng.lat, e.latlng.lng);
    }).on('search:collapsed', function() {
        // Handle search collapse if needed
    });

    map.addControl(searchControl);

    // Add button to geolocate user
    const locateControl = L.control.locate({
        position: 'topright',
        drawCircle: false,
        flyTo: true,
        keepCurrentZoomLevel: false,
        markerStyle: {
            weight: 1,
            opacity: 0.8,
            fillOpacity: 0.8
        },
        onLocationError: function(err) {
            console.log('Location error:', err.message);
        },
        onLocationFound: function(e) {
            placeMarker(e.latlng.lat, e.latlng.lng);
        }
    }).addTo(map);
}

// Load Leaflet JS if not already loaded
function loadLeafletJS() {
    if (typeof L === 'undefined') {
        const script = document.createElement('script');
        script.src = 'https://unpkg.com/leaflet@1.9.3/dist/leaflet.js';
        script.onload = initLocationMap;
        document.head.appendChild(script);
    } else {
        initLocationMap();
    }
}

// Load Leaflet JS if the map is on the page
if (document.getElementById('locationMap')) {
    loadLeafletJS();
}
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the location map
    initLocationMap();
    
    // Set up file upload preview
    setupFileUploadPreview();
    
    // Form validation
    setupFormValidation();
    
    // Add animations
    setupAnimations();
});

// Initialize the location map with Leaflet
function initLocationMap() {
    if (!document.getElementById('locationMap')) return;

    // Default coordinates (center of Nepal)
    const defaultLat = 28.3949;
    const defaultLng = 84.1240;
    const defaultZoom = 7;

    // Initialize the map
    const map = L.map('locationMap').setView([defaultLat, defaultLng], defaultZoom);

    // Add the OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Create a marker variable
    let marker = null;

    // Try to get the user's current location
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                const userLat = position.coords.latitude;
                const userLng = position.coords.longitude;
                
                // Center map on user's location
                map.setView([userLat, userLng], 15);
                
                // Add marker at user's location
                placeMarker(userLat, userLng);
            },
            function(error) {
                console.log('Geolocation error:', error);
                // Use default location if geolocation fails
                placeMarker(defaultLat, defaultLng);
            },
            {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0
            }
        );
    } else {
        // Browser doesn't support geolocation
        placeMarker(defaultLat, defaultLng);
    }

    // Add click event to place/update marker
    map.on('click', function(e) {
        placeMarker(e.latlng.lat, e.latlng.lng);
    });

    // Function to place or update the marker
    function placeMarker(lat, lng) {
        // Update the hidden input fields
        document.getElementById('latitude').value = lat;
        document.getElementById('longitude').value = lng;

        // Remove existing marker if it exists
        if (marker) {
            map.removeLayer(marker);
        }

        // Add new marker
        marker = L.marker([lat, lng], {
            draggable: true,
            icon: L.divIcon({
                className: 'location-marker',
                html: '<i class="fas fa-map-marker-alt"></i>',
                iconSize: [30, 30],
                iconAnchor: [15, 30]
            })
        }).addTo(map);

        // Update position when marker is dragged
        marker.on('dragend', function(e) {
            const newLatLng = e.target.getLatLng();
            document.getElementById('latitude').value = newLatLng.lat;
            document.getElementById('longitude').value = newLatLng.lng;
        });
    }

    // Add search control
    const searchControl = L.control.search({
        position: 'topright',
        layer: L.layerGroup(),
        initial: false,
        zoom: 15,
        marker: false,
        autoType: false,
        autoCollapse: true,
        textPlaceholder: 'Search location...'
    });

    searchControl.on('search:locationfound', function(e) {
        placeMarker(e.latlng.lat, e.latlng.lng);
    }).on('search:collapsed', function() {
        // Handle search collapse if needed
    });

    map.addControl(searchControl);

    // Add button to geolocate user
    const locateControl = L.control.locate({
        position: 'topright',
        drawCircle: false,
        flyTo: true,
        keepCurrentZoomLevel: false,
        markerStyle: {
            weight: 1,
            opacity: 0.8,
            fillOpacity: 0.8
        },
        onLocationError: function(err) {
            console.log('Location error:', err.message);
        },
        onLocationFound: function(e) {
            placeMarker(e.latlng.lat, e.latlng.lng);
        }
    }).addTo(map);
}

// Set up file upload preview functionality
function setupFileUploadPreview() {
    const fileInput = document.getElementById('photos');
    const previewContainer = document.getElementById('photoPreview');
    
    if (!fileInput || !previewContainer) return;
    
    fileInput.addEventListener('change', function(e) {
        // Clear previous previews
        previewContainer.innerHTML = '';
        
        // Get selected files
        const files = e.target.files;
        
        // Check if files were selected
        if (files.length === 0) return;
        
        // Check each file
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            
            // Check file type
            if (!file.type.match('image.*')) {
                alert('Only image files are allowed');
                continue;
            }
            
            // Check file size (5MB max)
            if (file.size > 5 * 1024 * 1024) {
                alert('File ' + file.name + ' is too large (max 5MB)');
                continue;
            }
            
            // Create preview element
            const reader = new FileReader();
            reader.onload = function(e) {
                const previewDiv = document.createElement('div');
                previewDiv.className = 'preview-image';
                
                const img = document.createElement('img');
                img.src = e.target.result;
                
                const removeBtn = document.createElement('span');
                removeBtn.className = 'remove-image';
                removeBtn.innerHTML = '&times;';
                removeBtn.addEventListener('click', function() {
                    previewDiv.remove();
                    updateFileInput();
                });
                
                previewDiv.appendChild(img);
                previewDiv.appendChild(removeBtn);
                previewContainer.appendChild(previewDiv);
            };
            reader.readAsDataURL(file);
        }
    });
    
    // Function to update the file input after removing a preview
    function updateFileInput() {
        const dataTransfer = new DataTransfer();
        const previews = document.querySelectorAll('.preview-image');
        
        previews.forEach(preview => {
            // This would need more complex handling to maintain the actual files
            // For a complete solution, you might need to store files in an array
        });
        
        // For a complete solution, consider using FormData or storing files in an array
    }
}

// Set up form validation
function setupFormValidation() {
    const form = document.getElementById('issueForm');
    if (!form) return;
    
    form.addEventListener('submit', function(e) {
        let isValid = true;
        
        // Validate required fields
        const requiredFields = form.querySelectorAll('[required]');
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                isValid = false;
                field.classList.add('error');
                
                // Add error message if not exists
                if (!field.nextElementSibling || !field.nextElementSibling.classList.contains('error-message')) {
                    const errorMsg = document.createElement('span');
                    errorMsg.className = 'error-message';
                    errorMsg.textContent = 'This field is required';
                    field.parentNode.insertBefore(errorMsg, field.nextSibling);
                }
            } else {
                field.classList.remove('error');
                const errorMsg = field.nextElementSibling;
                if (errorMsg && errorMsg.classList.contains('error-message')) {
                    errorMsg.remove();
                }
            }
        });
        
        // Validate at least one photo is uploaded
        const fileInput = document.getElementById('photos');
        if (fileInput.files.length === 0) {
            isValid = false;
            const uploadBox = document.querySelector('.file-upload-box');
            uploadBox.classList.add('error');
            
            // Add error message if not exists
            if (!uploadBox.nextElementSibling || !uploadBox.nextElementSibling.classList.contains('error-message')) {
                const errorMsg = document.createElement('span');
                errorMsg.className = 'error-message';
                errorMsg.textContent = 'Please upload at least one photo';
                uploadBox.parentNode.insertBefore(errorMsg, uploadBox.nextSibling);
            }
        } else {
            const uploadBox = document.querySelector('.file-upload-box');
            uploadBox.classList.remove('error');
            const errorMsg = uploadBox.nextElementSibling;
            if (errorMsg && errorMsg.classList.contains('error-message')) {
                errorMsg.remove();
            }
        }
        
        // Validate location is selected
        const latitude = document.getElementById('latitude').value;
        const longitude = document.getElementById('longitude').value;
        if (!latitude || !longitude) {
            isValid = false;
            const mapContainer = document.querySelector('.map-container');
            mapContainer.classList.add('error');
            
            // Add error message if not exists
            if (!mapContainer.nextElementSibling || !mapContainer.nextElementSibling.classList.contains('error-message')) {
                const errorMsg = document.createElement('span');
                errorMsg.className = 'error-message';
                errorMsg.textContent = 'Please select a location on the map';
                mapContainer.parentNode.insertBefore(errorMsg, mapContainer.nextSibling);
            }
        } else {
            const mapContainer = document.querySelector('.map-container');
            mapContainer.classList.remove('error');
            const errorMsg = mapContainer.nextElementSibling;
            if (errorMsg && errorMsg.classList.contains('error-message')) {
                errorMsg.remove();
            }
        }
        
        if (!isValid) {
            e.preventDefault();
            
            // Scroll to first error
            const firstError = form.querySelector('.error');
            if (firstError) {
                firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }
    });
}

// Set up animations
function setupAnimations() {
    // Animate form groups with staggered delay
    const formGroups = document.querySelectorAll('.form-group');
    formGroups.forEach((group, index) => {
        group.style.opacity = '0';
        group.style.transform = 'translateY(20px)';
        group.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;
        
        setTimeout(() => {
            group.style.opacity = '1';
            group.style.transform = 'translateY(0)';
        }, 100);
    });
    
    // Animate tip cards
    const tipCards = document.querySelectorAll('.tip-card');
    tipCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.5s ease ${index * 0.2}s, transform 0.5s ease ${index * 0.2}s`;
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    });
    
    // Add hover effects to tip cards
    tipCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.querySelector('.tip-icon').style.transform = 'rotate(5deg) scale(1.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.querySelector('.tip-icon').style.transform = 'rotate(0) scale(1)';
        });
    });
}

// Load Leaflet JS if not already loaded
function loadLeafletJS() {
    if (typeof L === 'undefined') {
        const script = document.createElement('script');
        script.src = 'https://unpkg.com/leaflet@1.9.3/dist/leaflet.js';
        script.onload = initLocationMap;
        document.head.appendChild(script);
    } else {
        initLocationMap();
    }
}

// Initialize if the map element exists
if (document.getElementById('locationMap')) {
    loadLeafletJS();
}
