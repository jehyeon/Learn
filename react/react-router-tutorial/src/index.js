import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route } from 'react-router';
import createBrowserHistory from 'history/createBrowserHistory'

import App from './App';
import Home from './containers/Home';
import About from './containers/About';
import Posts from './containers/Posts';

import './index.css';

const history = createBrowserHistory();

ReactDOM.render(
    <Router history={history}>
        {/* Route 내부의 Route가 서브 라우트로 인식이 안됨, 다른 방법 찾기 */}
        <Route path="/" component={App}>
            <Route exact path="/" component={Home}/>
            <Route path="about" component={About}/>
            <Route path="post" component={Posts}/>
        </Route>
    </Router>, 
    document.getElementById('root')
);