// The elements
const mainMenu = document.getElementById('main-menu');
const lessonScreen = document.getElementById('lesson-screen');
const menuButtons = document.querySelectorAll('.menu-btn');
const backBtn = document.getElementById('back-btn');
const lessonTitle = document.getElementById('lesson-title');
const lessonContent = document.getElementById('lesson-content');
const overlay = document.getElementById('transition-overlay');

let currentCategory = '';

// Displays a "Game Screen" and creates buttons for the options.
async function loadLesson(category) {
    // Fetch the data in the background
    const response = await fetch(`/api/lesson/${category}`);
    const data = await response.json();
    
    // Lesson UI
    const newContent = document.createElement('div');
    newContent.innerHTML = `
        <div class="visual-display">${data.visual}</div>
        <div class="options-grid"></div>
        <div id="feedback" style="margin-top:20px; font-size: 1.5rem;"></div>
    `;

    // Place content in buttons
    const grid = newContent.querySelector('.options-grid');
    const feedback = newContent.querySelector('#feedback');

    // Response to selection
    data.options.forEach(opt => {
        const btn = document.createElement('button');
        btn.textContent = opt;
        btn.className = 'option-btn';
        btn.onclick = () => {
            document.querySelectorAll('.option-btn').forEach(b => b.disabled = true);
            if (opt === data.correct) {
                feedback.textContent = "Correct! Great job! 🎉";
                btn.style.backgroundColor = "#B5EAD7";
            } else {
                feedback.textContent = "Nice try! The answer was " + data.correct;
                btn.style.backgroundColor = "#FFB7B2";
            }
            setTimeout(() => loadLesson(category), 2000);
        };
        grid.appendChild(btn);
    });

    lessonContent.innerHTML = ''; 
    lessonContent.appendChild(newContent);
}

function triggerTransition(targetScreen, categoryName = '', swipeColor = '#fdf6e3') {
    overlay.style.backgroundColor = swipeColor;
    overlay.classList.add('animate-swipe');
    overlay.classList.add('sweep-in');

    setTimeout(() => {
        if (targetScreen === 'lesson') {
            lessonTitle.textContent = `Let's Learn ${categoryName}!`;
            mainMenu.classList.remove('active');
            lessonScreen.classList.add('active');
            // Trigger the Python fetch!
            loadLesson(currentCategory);
        } else {
            lessonScreen.classList.remove('active');
            mainMenu.classList.add('active');
            lessonContent.innerHTML = ''; // Clear out the old lesson
        }

        overlay.classList.remove('sweep-in');
        overlay.classList.add('sweep-out');

        setTimeout(() => {
            overlay.classList.remove('animate-swipe');
            overlay.classList.remove('sweep-out');
        }, 600);
    }, 600);
}

// Waits for button click
menuButtons.forEach(button => {
    button.addEventListener('click', () => {
        currentCategory = button.getAttribute('data-category');
        const color = button.style.backgroundColor;
        triggerTransition('lesson', currentCategory, color);
    });
});

// Transition
backBtn.addEventListener('click', () => {
    triggerTransition('menu', '', '#E1D3B8'); 
});