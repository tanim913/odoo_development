function setupIntersectionObserver(classToObserve, classToAdd) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add(classToAdd);
            } else {
                entry.target.classList.remove(classToAdd);
            }
        });
    });

    const elements = document.querySelectorAll(classToObserve);
    elements.forEach((el) => observer.observe(el));
}

//left animation
setupIntersectionObserver('.hidden_animate_left', 'show_animate_left');

//right animation
setupIntersectionObserver('.hidden_animate_right', 'show_animate_right');
