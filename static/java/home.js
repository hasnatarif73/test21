let currentIndex = 0;
const slides = document.querySelectorAll('.slider-image');
const totalSlides = slides.length;

function moveSlide(step) {
    console.log("Moving slide by step:", step);
    // Check if the step is valid
    currentIndex += step;

    if (currentIndex < 0) {
        currentIndex = totalSlides - 1;
    } else if (currentIndex >= totalSlides) {
        currentIndex = 0;
    }

    updateSlider();
}

function updateSlider() {
    const sliderContainer = document.querySelector('.slider-container');
    const slideWidth = window.innerWidth;  // Get the current viewport width
    sliderContainer.style.transform = `translateX(${-currentIndex * slideWidth}px)`;
}

// Initial call to set the first slide
updateSlider();

// Optionally, listen for window resize to adjust slider on resize
window.addEventListener('resize', updateSlider);
