const { ipcRender } = require('electron');

// Events
const addItem = e => {
  // ipcRender.send('addItem', )
  console.log(e);
};

const form = document.getElementById('add-item');

form.addEventListener('submit', e => {
  e.preventDefault();
  // console.log(e);
  console.log(form.name.value);
  console.log(form.color.value);
  console.log(form.price.value);
});