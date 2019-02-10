import React, { Component } from 'react';
import './App.css';
import { type, values } from './seoul_grid.json';
import Grid from './Grid';

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Grid in Seoul</h1>
        <form>
          <button>아파트</button>
          <button>오피스텔</button>
        </form>
        <Grid type={ type } values={ values } />
      </div>
    );
  }
}

export default App;
