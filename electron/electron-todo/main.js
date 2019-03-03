'use strict'

const path = require('path')
const { app, ipcMain } = require('electron')

// our constructors
const Window = require('./Window')
const DataStore = require('./DataStore')

// create a new todo store name "Todos Main"
const todosData = new DataStore({name: 'Todos Main'})

function main () {
    // todo list window
    let mainWindow = new Window({
        file: path.join('renderer', 'index.html')
    })

    // add todo window ( initially does not exist )
    let addTodoWin

    // TODO: put these events into their own file
    mainWindow.once('show', () => {
        mainWindow.webContents.send('todos', todosData.todos)
    })

    // add-todo from add todo window
    ipcMain.on('add-todo', (event, todo) => {
        const updatedTodos = todosData.addTodo(todo).todos

        mainWindow.send('todos', updatedTodos)
    })

    // delete-todo from todo list window
    ipcMain.on('delete-todo', (event, todo) => {
        const updatedTodos = todosData.deleteTodo(todo).todos
        
        mainWindow.send('todos', updatedTodos)
    })
}

// Need to update for mac
app.on('ready', main)

app.on('window-all-closed', function () {
    app.quit()
})