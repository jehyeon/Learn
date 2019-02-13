import React, { Component } from 'react';
import './Grid.css';
import get_color from './utils/Color'

class Grid extends Component {
    state = {
        mode: 1
    }
    render() {
        const { type, areas, prices } = this.props;
        
        const grid = areas.map( line => (                    
            <ul className="block_line">
                {line.map(block => {
                    const bg = { 'background-color': '#AAA'};
                    if (this.state.mode == 0) {
                        bg['background-color'] = get_color(block)
                    }
                    else {
                        bg['background-color'] = get_color(block, 622, prices[block])
                    }

                    return (
                        <li 
                            area={block} 
                            className={type} 
                            // price={prices[block]} 
                            mode={this.state.mode}
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