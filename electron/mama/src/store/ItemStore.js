const Store = require('electron-store');

class ItemStore extends Store {
  constructor (settings) {
    // Same as new Store (settings)
    super (settings);

    // Initialize with todos or empty array
    this.items = this.get('items') || [];
  }

  saveTodos () {
    // Save todos to JSON file
    this.set('items', this.items)

    // Returning 'this' allows method chaining
    return this;
  }

  getTodos () {
    // Set object's todos to todos in JSON file
    this.items = this.get('items') || [];

    return this;
  }

  addTodo (item) {
    this.items = [ ...this.items, item];

    return this.saveTodos();
  }

  deleteTodo (todo) {
    // ! to be update
    this.items = this.items.filter(i => i !== item);

    return this.saveTodos();
  }
}

module.exports = ItemStore;