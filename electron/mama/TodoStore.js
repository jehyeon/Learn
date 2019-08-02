const Store = require('electron-store');

class TodoStore extends Store {
    constructor (settings) {
        // Same as new Store (settings)
        super (settings);

        // Initialize with todos or empty array
        this.todos = this.get('todos') || [];
    }

    saveTodos () {
        // Save todos to JSON file
        this.set('todos', this.todos)

        // Returning 'this' allows method chaining
        return this;
    }

    getTodos () {
        // Set object's todos to todos in JSON file
        this.todos = this.get('todos') || [];

        return this;
    }

    addTodo (todo) {
        this.todos = [ ...this.todos, todo];

        return this.saveTodos();
    }

    deleteTodo (todo) {
        // Filter out the target todo
        this.todos = this.todos.filter(t => t !== todo)

        return this.saveTodos();
    }
}

module.exports = TodoStore;