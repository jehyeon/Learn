import React from 'react';
import ReactDOM from 'react-dom';
// createStore와 root 리듀서 불러오기
import { createStore } from 'redux';
import devToolsEnhancer from 'remote-redux-devtools';
import rootReducer from './store/modules';
// Provider 불러오기
import { Provider } from 'react-redux';

import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

// 리덕스 개발자도구 적용하여 스토어 만들기
const store = createStore(rootReducer, devToolsEnhancer());

// Provider 렌더링해서 기존의 App 감싸주기
ReactDOM.render(
    <Provider store={store}>
        <App /> 
    </Provider>,    
    document.getElementById('root')
);
registerServiceWorker();
