import React, { Component } from 'react';
import './App.css';
import { type, values } from './seoul_grid.json';
import Grid from './Grid';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Grid type={ type } values={ values } />
      </div>
    );
  }
}

export default App;
