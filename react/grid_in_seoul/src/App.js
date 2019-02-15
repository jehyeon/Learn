import React, { Component } from 'react'
import './App.css'

import { type, values } from './json/seoul_grid.json'
import area_id from './json/seoul_id.json'
import { data } from './json/seoul_price.json'

import Grid from './Grid'
import Ranking from './Ranking'

class App extends Component {
  state = {
    mode: '0',
    prices: []
  }

  handleTypeChange = (e, mode) => {
    e.preventDefault();
    const house_type = e.target.getAttribute('house_type');
    const want = e.target.getAttribute('mode');
    if (want == '0') {
      this.setState({mode: want, prices:[]})
    }
    else {
      this.setState({
        mode: want,
        prices: data[e.target.getAttribute('house_type')].purchage.period.prices
      });
    }
  }
  render() {

    return (
      <div className="App">
        {/* 헤더 컴포넌트로 수정 예정 */}
        <h1>Grid in Seoul</h1>
        
        <Grid type={ type } areas={ values } prices={this.state.prices} mode={this.state.mode}/>

        {/* 지역 리스트 뷰 (우측 fixed 리스트) */}
        <Ranking prices={this.state.prices}/>
        {/*  */}

        {/* 기간 및 하우스 타입 설정가능한 form 컴포넌트로 수정 예정 */}
        {/* Select 된 버튼 보여주기 */}
        <form>
          <button mode='0' onClick={this.handleTypeChange}>지역</button>
          <button mode='1' house_type='office' onClick={this.handleTypeChange}>오피스텔</button>
          <button mode='2' house_type='appartment' onClick={this.handleTypeChange}>아파트</button>
        </form>
      </div>
    );
  }
}

export default App;
