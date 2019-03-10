import { combineReducers } from 'redux';
import counter from './counter';

// redux의 내장 함수인 combineReducers를 사용하여 리듀서를 하나로 합치는 작업을 한다.
export default combineReducers({
    counter,
    // 다른 리듀서를 만들게되면 추가
});