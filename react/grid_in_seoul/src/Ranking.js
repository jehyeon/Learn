import React, { Component } from 'react'
import './Ranking.css';

class Ranking extends Component {
    state = {
        prices: []
    }

    constructor (props) {
        super(props);
    }

    static getDerivedStateFromProps (nextProps, prevState) {
        if (nextProps.prices !== prevState.prices) {
            console.log(nextProps.prices);
            return { prices: nextProps.prices };
        }
        return null;
    }
    render() {
        const { prices } = this.state;
        const rank = prices.map(price => {
            if (price === 0) { return null; }
            return (
            <li>{price}</li>
            );
        });
        console.log(prices);
        return (
            <div className='ranking-box'>
                <ul className='ranking'>
                    { rank }
                </ul>
            </div>
        );
    }
}

export default Ranking;