document.addEventListener('DOMContentLoaded', function() {
    // Initialize the location map
    initLocationMap();
    
    // Set up file upload preview
    setupFileUploadPreview();
    
    // Form validation
    setupFormValidation();
    
    // Add animations to form elements
    setupFormAnimations();
    
    // Add hover effects to tip cards
    setupTipCardHover();
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
        if (files.length === 0) {
            document.querySelector('.file-upload-box').style.borderColor = '#ddd';
            return;
        }
        
        // Check each file
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            
            // Check file type
            if (!file.type.match('image.*')) {
                showAlert('Only image files are allowed (JPEG, PNG)', 'error');
                continue;
            }
            
            // Check file size (5MB max)
            if (file.size > 5 * 1024 * 1024) {
                showAlert(`File ${file.name} is too large (max 5MB)`, 'error');
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
    
    // Drag and drop functionality
    const uploadBox = document.querySelector('.file-upload-box');
    
    uploadBox.addEventListener('dragover', function(e) {
        e.preventDefault();
        this.style.borderColor = 'var(--primary-purple)';
        this.style.backgroundColor = 'rgba(106, 13, 173, 0.1)';
    });
    
    uploadBox.addEventListener('dragleave', function() {
        this.style.borderColor = '#ddd';
        this.style.backgroundColor = '';
    });
    
    uploadBox.addEventListener('drop', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
        this.style.backgroundColor = '';
        fileInput.files = e.dataTransfer.files;
        const event = new Event('change');
        fileInput.dispatchEvent(event);
    });
    
    // Function to update the file input after removing a preview
    function updateFileInput() {
        const dataTransfer = new DataTransfer();
        const previews = document.querySelectorAll('.preview-image');
        
        // In a real implementation, you would need to reconstruct the FileList
        // This is a simplified version - for production you might need to store files
        if (previews.length === 0) {
            fileInput.value = '';
        }
    }
}

// Set up form validation
function setupFormValidation() {
    const form = document.getElementById('issueForm');
    if (!form) return;
    
    form.addEventListener('submit', function(e) {
        let isValid = true;
        let firstErrorElement = null;
        
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
                
                // Track first error for scrolling
                if (!firstErrorElement) {
                    firstErrorElement = field;
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
            
            if (!firstErrorElement) {
                firstErrorElement = uploadBox;
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
            
            if (!firstErrorElement) {
                firstErrorElement = mapContainer;
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
            if (firstErrorElement) {
                firstErrorElement.scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'center' 
                });
            }
            
            showAlert('Please fill all required fields correctly', 'error');
        }
    });
}

// Add animations to form elements
function setupFormAnimations() {
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
}

// Add hover effects to tip cards
function setupTipCardHover() {
    const tipCards = document.querySelectorAll('.tip-card');
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

// Helper function to show alerts
function showAlert(message, type) {
    // Remove existing alerts
    const existingAlerts = document.querySelectorAll('.custom-alert');
    existingAlerts.forEach(alert => alert.remove());
    
    const alertDiv = document.createElement('div');
    alertDiv.className = `custom-alert alert-${type}`;
    alertDiv.textContent = message;
    
    document.body.appendChild(alertDiv);
    
    // Position the alert
    alertDiv.style.position = 'fixed';
    alertDiv.style.top = '20px';
    alertDiv.style.left = '50%';
    alertDiv.style.transform = 'translateX(-50%)';
    alertDiv.style.padding = '15px 25px';
    alertDiv.style.borderRadius = '8px';
    alertDiv.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
    alertDiv.style.zIndex = '1000';
    alertDiv.style.animation = 'fadeInDown 0.5s ease';
    
    if (type === 'error') {
        alertDiv.style.backgroundColor = '#F8D7DA';
        alertDiv.style.color = '#721C24';
        alertDiv.style.borderLeft = '4px solid #DC3545';
    } else {
        alertDiv.style.backgroundColor = '#D4EDDA';
        alertDiv.style.color = '#155724';
        alertDiv.style.borderLeft = '4px solid #28A745';
    }
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        alertDiv.style.animation = 'fadeOutUp 0.5s ease';
        setTimeout(() => alertDiv.remove(), 500);
    }, 5000);
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