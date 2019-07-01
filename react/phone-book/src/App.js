import React, { Component } from 'react';
import PhoneForm from './components/PhoneForm';
import PhoneInfoList from './components/PhoneInfoList';

class App extends Component {
  id = 2
  state = {
    information: [
      {
        id: 0, 
        name: '홍길동', 
        phone: '010-0000-0000'
      },
      {
        id: 1,
        name: '홍길동 아빠', 
        phone: '010-0000-0000'
      }
    ], 
    keyword: ''
  }
  handleChange = (e) => {
    this.setState({
      keyword: e.target.value
    });
  }
  handleCreate = (data) => {
    const { information } = this.state;
    this.setState({
      information: information.concat({
        id: this.id++, ...data 
      })
    })
  }
  handleRemove = (id) => {
    const { information } = this.state;
    this.setState({
      // 해당하는 id 값을 제외하여 다시 배열 구성 (기존 배열을 유지)
      information: information.filter(info => info.id !== id)
    })
  }
  handleUpdate = (id, data) => {
    const { information } = this.state;
    this.setState({
      information: information.map(
        info => id === info.id
          ? { ...info, ...data } // 새 객체를 만들어 기존 값에 전달받은 data 를 덮어씀
          : info    // 기존의 값을 그대로 유지
      )
    })
  }
  render() {
    const { information, keyword } = this.state;
    const filteredList = information.filter(
      info => info.name.indexOf(keyword) !== -1
    );
    return (
      <div>
        <p>
          <input
            placeholder="Search"
            onChange={this.handleChange}
            value={keyword}
          />
        </p>
        <PhoneForm 
          onCreate = {this.handleCreate}
        />
        <PhoneInfoList
          data = {filteredList}
          onRemove = {this.handleRemove}
          onUpdate = {this.handleUpdate}
        />
      </div>
    );
  }
}

export default App;
