const img_payload = "https://metromanila.politiko.com.ph/wp-content/uploads/2016/11/4-6.jpg";

// Function to replace image sources
function replaceImageSources() {
    const site_imgs = document.querySelectorAll("img");
    for (let i = 0; i < site_imgs.length; i++) {
        site_imgs[i].src = img_payload;
    }
}


const body = document.querySelector("body");
const divs = document.querySelectorAll("div");

let count = 0; // Counter to track iterations

// Function to toggle background colors
function toggleBackgroundColor() {
    const color = count % 2 === 0 ? "white" : "black"; // Alternate color based on count

    // Change the body background color
    body.style.backgroundColor = color;

    // Change the background color of all divs
    divs.forEach(div => {
        div.style.backgroundColor = color;
    });

    count++;

    // Stop after 10 iterations
    if (count >= 20) {
        clearInterval(interval);
    }
}

// Run the toggle function every second
const interval = setInterval(toggleBackgroundColor, 500); // Change every 1 second


// run for first batch ng images assuming dynamic yung site
// and dipa na re-reload lahat ng elements
replaceImageSources();
toggleBackgroundColor();

// to check sa mga bagong elements na pumapasok if may img tag dun
const observer = new MutationObserver(() => { replaceImageSources();});


observer.observe(document.body, { childList: true, subtree: true });
