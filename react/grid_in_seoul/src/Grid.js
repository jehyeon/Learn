import React, { Component } from 'react';
import './Grid.css';

class Grid extends Component {
    state = {
        type: 'square',
        values: [],
    }
   

    render() {
        const { type, values } = this.props;
        const hiddenStyle = {
            'background-color': '#FFFFFF'
        };
        const grid = values.map( line => (                    
            <ul>
                {line.map(block => {
                    if (block === 1) { return (<li></li>)}
                    else { return <li style={hiddenStyle}></li>}
                })}
            </ul>
        ));


        return (
            <div className="grid">
                { grid }
            </div>
        );
    }
}

export default Grid;