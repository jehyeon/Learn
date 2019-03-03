'use strict'

const { ipcRenderer } = require('electron')

// listen for the form to be submitted
document.getElementById('todoForm').addEventListener('submit', (evt) => {
    // prevent default refresh funcionality of forms
    evt.preventDefault()

    // input on the form
    const input = evt.target[0]

    // send todo to main process
    ipcRenderer.send('add-todo', input.value)

    // reset input
    input.value = ''
})