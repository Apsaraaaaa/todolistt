document.addEventListener('DOMContentLoaded', function () {
    console.log('To-Do List loaded');

    // Add any interactive functionality here
    const taskItems = document.querySelectorAll('.task-item');

    taskItems.forEach(item => {
        item.addEventListener('click', function () {
            this.classList.toggle('completed');
        });
    });
});