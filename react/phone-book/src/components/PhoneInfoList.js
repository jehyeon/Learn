import React, { Component } from 'react';
import PhoneInfo from './PhoneInfo';

class PhoneInfoList extends Component {
	static defaultProps = {
			data: [],
			onRemove: () => console.warn('onRemove not defined'),
			onUpdate: () => console.warn('onUpdate not definde')
	}

	// 재 랜더링이 필요없을 경우 호출하지 않음
	shouldComponentUpdate (nextProps, nextState) {
		return nextProps.data !== this.props.data;
	}
	
	render() {
		const { data, onRemove, onUpdate } = this.props;
		const list = data.map(
			info => (
				<PhoneInfo 
					key = {info.id}
					info = {info}
					onRemove = {onRemove}
					onUpdate = {onUpdate}
				/>
			)
		);

		return (
			<div>
				{list}
			</div>
		);
	}
}

export default PhoneInfoList;