import React, { Component } from 'react';

class PhoneInfo extends Component {
	// info라는 객체를 props로 받아와 렌더링 할 것이다.
	// 실수로 info 값을 전달하지 않는다면 Component가 깨지게 되므로, 기본값을 설정 한다.
	static defaultProps = {
		info: {
			id: 0,
			name: 'default_name',
			phone: '010-0000-0000'
		}
	}
	state = {
		editing: false,
		name: '',
		phone: ''
	}
	handleRemove = () => {
		const { info, onRemove } = this.props;
		onRemove(info.id);
	}
	// editing 값을 반전시키는 함수
	handleToggleEdit = () => {
		const { editing } = this.state;
		this.setState({ editing: !editing });
	}
	handleChange = (e) => {
		const { name, value } = e.target;
		this.setState({
			[name]: value
		});
	}

	// editing 값이 바뀔 때 처리하는 로직
	componentDidUpdate (prevProps, prevState) {
		const { info, onUpdate } = this.props;
		if (!prevState.editing && this.state.editing) {
			// editing이 false에서 true로 전환 될 때
			this.setState({
				name: info.name,
				phone: info.phone
			})
		}

		if (prevState.editing && !this.state.editing) {
			// editing이 true에서 false로 전환 될 때
			onUpdate(info.id, {
				name: this.state.name,
				phone: this.state.phone
			});
		}
	}

	shouldComponentUpdate (nextProps, nextState) {
		// 수정 모드가 아니고, info 값이 같다면 리 렌더링 안함
		if (!this.state.editing
				&& !nextState.editing
				&& nextProps.info === this.props.info) {
			return false;			
		}
		return true;
	}
	render() {
		const style = {
			border: '1px solid black',
			padding: '8px',
			margin: '8px'
		};

		const { editing } = this.state;

		// 수정 모드
		if (editing) {
			return (
				<div style = {style}>
					<div>
						<input
							value = {this.state.name}
							name = 'name'
							placeholder = 'name'
							onChange = {this.handleCahnge}
						/>
					</div>
					<div>
						<input
							value = {this.state.phone}
							name = 'phone'
							placeholder = 'phone'
							onChange = {this.handleChange}
						/>
					</div>
					<button onClick={this.handleToggleEdit}>Edit</button>
					<button onClick={this.handleRemove}>Delete</button>
				</div>
			);
		}

		// 일반 모드
		const {
			name, phone
		} = this.props.info;

		return (
			<div style = {style}>
				<div><b>{name}</b></div>
				<div>{phone}</div>
				<button onClick={this.handleToggleEdit}>Edit</button>
				<button onClick={this.handleRemove}>Delete</button>
			</div>
		)
	}
}

export default PhoneInfo;