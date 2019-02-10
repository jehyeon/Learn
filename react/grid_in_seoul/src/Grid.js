import React, { Component } from 'react';
import './Grid.css';

class Grid extends Component {
    state = {
        type: 'square',
        values: [],
    }
   
    handleClick = () => {
        const { values } = this.state;
        console.log(this.props);
        // this.setState({
        //     values: [...values[e.number]++]
        // });
        console.log({values});
    }

    render() {
        
        // <li> 새 컴포넌트 만드는게 좋을 듯??
        const { values } = this.props;
        let count = -1;
        const colors = [
            '#7CA57E','#ACC2B5','#BECED9','#86968D','#CBE4D5', '#aaa', '#DDD',
        ];
        const grid = values.map( line => (                    
            <ul>
                {line.map(block => { 
                    count++;
                    if (block > 0) {
                        return (<li number={count} style={{'background-color': colors[block%7]}}></li>)                        
                    }
                    else { return <li number={count} style={{'opacity': '0'}}>{count}</li>}
                })}
            </ul>
        ));


        return (
            <div className='grid-wrapper'>
                <ul className="grid">
                    { grid }
                </ul>
            </div>
        );
    }
}

export default Grid;