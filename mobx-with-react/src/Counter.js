import React, { Component } from 'react';
import { observer, inject } from 'mobx-react';

// **** 함수형태로 파라미터를 전달해주면 특정 값만 받아올 수 있음.
// @inject(stores => ({
//   number: stores.counter.number,
//   increase: stores.counter.increase,
//   decrease: stores.counter.decrease,
// }))
@inject('counter')  // ! check
@observer
class Counter extends Component {
  render() {
    const { counter } = this.props;
    return (
      <div>
        <h1>{counter.number}</h1>
        <button onClick={counter.increase}>+1</button>
        <button onClick={counter.decrease}>-1</button>
      </div>
    );
  }
}


export default Counter;