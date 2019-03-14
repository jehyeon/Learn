import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import Counter from '../components/Counter';
import { increment, decrement } from '../store/modules/counter'

class CounterContainer extends Component {
    handleIncrement = () => {
        this.props.increment();
    }
    handleDecrement = () => {
        this.props.decrement();
    }

    render() {
        const { color, number } = this.props;
        return (
            <Counter
                color={color}
                value={number}
                onIncrement={this.handleIncrement}
                onDecrement={this.handleDecrement}
            />
        );
    }
}

const mapStateToProps = ({ counter }) => ({
    color: counter.color,
    number: counter.number,
});

const mapDispatchProps = dispatch =>
    bindActionCreators({ increment, decrement }, dispatch);

export default connect(
    mapStateToProps,
    mapDispatchProps
)(CounterContainer);