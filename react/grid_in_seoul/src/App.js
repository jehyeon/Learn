import React, { Component } from 'react';
import './App.css';

import { type, values } from './json/seoul_grid.json';
import area_id from './json/seoul_id.json';
import { data } from './json/seoul_price.json';

import Grid from './Grid';

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Grid in Seoul</h1>
        {/* <form>
          <button>아파트</button>
          <button>오피스텔</button>
        </form> */}
        <Grid type={ type } areas={ values } prices={data.prices}/>
      </div>
    );
  }
}

export default App;
