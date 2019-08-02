// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.
const { ipcRenderer } = require('electron');

document.getElementById('todoForm').addEventListener('submit', evt => {
    // Prevent default refresh functionality of forms
    evt.preventDefault();

    // Input on the form
    const input = evt.target[0];

    // Send todo to main process
    ipcRenderer.send('add-todo', input.value);

    // Reset input
    input.value = '';
});


// Functions

// Delete todo by its text value
const deleteTodo = e => {
    ipcRenderer.send('delete-todo', e.target.textContent);
};

ipcRenderer.on('todos', (event, todos) => {
    const todoList = document.getElementById('todoList');

    // Create todos html
    const todoItems = todos.reduce((html, todo) => {
       html += `<li class="todo-item">${todo}</li>`;

       return html;
    }, '');

    //  Set list html to the todo items
    todoList.innerHTML = todoItems;

    todoList.querySelectorAll('.todo-item').forEach(item => {
        item.addEventListener('click', deleteTodo);
    });
});