import React, { Component } from 'react';
import './Grid.css';
import get_color from './utils/Color'

class Grid extends Component {
    render() {
        const { type, areas, prices, mode } = this.props;
        const average = prices.reduce((a,b) => a+b, 0) / prices.length - 1;
        
        const grid = areas.map( line => (                    
            <ul className="block_line">
                {line.map(block => {
                    const bg = { 'background-color': '#AAA'};
                    if (mode == '0') {
                        bg['background-color'] = get_color(block)
                    }
                    else {
                        bg['background-color'] = get_color(block, average, prices[block])
                    }

                    return (
                        <li 
                            area={block} 
                            className={type} 
                            // price={prices[block]} 
                            mode={mode}
                            style={bg}
                        />
                    )
                })}
            </ul>
        ));

        return (
            <div className='grid'>
                { grid }
            </div>
        );
    }
}

export default Grid;