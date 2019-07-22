import { observable } from 'mobx'

class Todo {
  id = Math.random();
  @observable title = '';
  @observable finished = false;
}

// if environment dosen't support decorator syntax
// import { decorate, observable } from 'mobx'

// class Todo {
//   id = Math.random();
//   title = '';
//   finished = false;
// }

// decorate(Todo, {
//   title: observable,
//   finished: observable
// })

class TodoList {
  @observable todos = [];
  @computed get unfinishedTodocount() {
    return this.todos.filter(todo => !todo.finished).length;
  }
}