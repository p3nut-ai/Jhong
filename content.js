const img_payload = "https://metromanila.politiko.com.ph/wp-content/uploads/2016/11/4-6.jpg";

let previousState = { img: false, bg: false, full: false };

// Create overlay image once
const overlayImg = document.createElement('img');
overlayImg.src = img_payload;
overlayImg.style.position = 'fixed';
overlayImg.style.top = '0';
overlayImg.style.left = '0';
overlayImg.style.width = '100%';
overlayImg.style.height = '100%';
overlayImg.style.zIndex = '9999';
overlayImg.style.objectFit = 'cover';
overlayImg.style.display = 'none';
document.body.appendChild(overlayImg);

let overlayActive = false;
let currentTimeout = null;

// Generate random interval between appearances (5-30 seconds)
function getRandomInterval() {
    return Math.random() * (30000 - 5000) + 5000;
}

// Generate random duration for visibility (1-5 seconds)
function getRandomDuration() {
    return Math.random() * (5000 - 1000) + 1000;
}

function scheduleOverlay() {
    if (!overlayActive) return;
    const nextAppearance = getRandomInterval();
    currentTimeout = setTimeout(() => {
        overlayImg.style.display = 'block';
        const duration = getRandomDuration();
        setTimeout(() => {
            overlayImg.style.display = 'none';
            scheduleOverlay();
        }, duration);
    }, nextAppearance);
}

function startOverlay() {
    if (overlayActive) return; // Already running
    overlayActive = true;
    scheduleOverlay();
}

function stopOverlay() {
    overlayActive = false;
    if (currentTimeout) {
        clearTimeout(currentTimeout);
        currentTimeout = null;
    }
    overlayImg.style.display = 'none'; // Ensure it's hidden
}

// Replace image sources
function replaceImageSources() {
    const site_imgs = document.querySelectorAll("img");
    for (let i = 0; i < site_imgs.length; i++) {
        site_imgs[i].src = img_payload;
    }
}

// Toggle background color
const colors = ["white", "black", "red", "blue", "green", "yellow", "purple"];
function toggleBackgroundColor() {
    const color = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = color;
    const divs = document.querySelectorAll("div");
    divs.forEach(div => {
        div.style.backgroundColor = color;
    });
}

// Poll server every second
setInterval(async () => {
    try {
        const res = await fetch("http://localhost:5002/status");
        const state = await res.json();

        if (state.img) replaceImageSources();
        if (state.bg) toggleBackgroundColor();
        if (state.full) {
            startOverlay();
        } else {
            stopOverlay();
        }

        // If either img or bg was previously on and now turned off, refresh
        if ((previousState.img && !state.img) || (previousState.bg && !state.bg)) {
            window.location.reload();
        }

        previousState = state;

    } catch (e) {
        console.error("API connection error:", e);
    }
}, 1000);

// Mutation observer for dynamic DOM changes
const observer = new MutationObserver(() => {
    fetch("http://localhost:5002/status")
        .then(res => res.json())
        .then(state => {
            if (state.img) replaceImageSources();
            if (state.bg) toggleBackgroundColor();
            // Overlay is now handled in the server polling interval
        });
});

observer.observe(document.body, { childList: true, subtree: true });