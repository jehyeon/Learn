# vanilla todo app using reduxer

### 1. 액션

#### 1-1. 액션은 애플리케이션에서 스토어로 보내는 데이터 묶음이다. (스토어의 유일한 정보원)
store.dispatch()를 통해 이들을 보낼 수 있다.
```
const ADD_TODO = 'ADD_TODO';

{
    type: ADD_TODO,
    text: 'Build my first Redux app'
}
```
액션은 평범한 자바스크립트 객체다. 
액션은 반드시 어떤 형태의 액션이 실행될 지 나타내는 type 속성을 가져야 한다.
타입은 일반적으로 문자열 상수로 정의된다. 

```
import { ADD_TODO, REMOVE_TODO } from '../actionTypes'
```
이와 같이 별도의 모듈로 분리할 수도 있다.


사용자가 할일을 완료했다고 체크하는 액션 하나를 추가해보자.
할일은 배열 안에 저장되기 때문에 특정한 할일을 index를 통해 참조할 수 있다.
```
{
    type: COMPLETE_TODO,
    index: 5
}
```
각 액션에는 가능한 적은 데이터를 전달하는 것이 좋다.

#### 1-2. 액션 생산자는 액션을 만드는 함수이다.

Redux의 액션 생산자는 단지 액션을 반환한다.
```
function addTodo(text) {
    return {
        type: ADD_TODO,
        text
    }
}
```
이는 액션 생산자를 더 이식하기 좋고 테스트하기 쉽게 한다.
실제로 액션을 보내려면 결과값을 dispatch() 함수에 넘긴다.
```
dispatch(addTodo(text));
dispatch(completeTodo(index));
```
혹은 자동으로 액션을 보내주는 바인드된 액션 생산자를 만든다.
```
const boundAddTodo = (text) => dispatch(addTodo(text));
const boundCompleteTodo = (index) => dispatch(complete(index));
```
dispatch() 함수를 스토어에서 store.dispatch()로 바로 접근할 수 있지만,
보통 react-redux의 connect()와 같은 헬퍼를 통해 접근한다.

여러 액션 생상자를 dispatch()에 바인드하기 위해 bindActionCreators()를 사용할 수도 있다.

*완성된 소스 ./actions.js*

### 2. 리듀서
액션은 "무언가 일어난다"라는 사실을 기술하고 리듀서는 애플리케이션의 상태가 어떻게 바뀌는 지는 특정한다.

#### 2-1. 상태 설계하기
Redux에서 애플리케이션의 모든 상태는 하나의 객체 저장된다.

todo 앱에 필요한 다음 두 가지만을 저장해보자

- 현재 선택된 필터
- 할일의 실제 목록

```
{
    visibilityFilter: 'SHOW_ALL',
    todos: [{
        text: 'Consider using Redux',
        completed: true,
    }, {
        text: 'Keep all state in a single tree',
        completed: false,
    }]
}
```

#### 2-2. 액션 다루기
리듀서는 이전 상태와 액션을 받아서 다음 상태를 반환하는 순수 함수이다.
```
(previousState, action) => newState
```
위 형태의 함수를 `Array.prototype.reduce(reducer, ?initialValue)`로 넘길 것이기 때문에 리듀서라고 부른다. 따라서 리듀서는 순수하게 유지하는 것이 매우 중요하다.

다음은 리듀서 내에서 하지 말아야 할 것들이다.
- 인수들을 변경(mutate) 하기
- API 호출이나 라우팅 전환같은 SideEffect를 일으키기
- Date.now()나 Math.random() 같이 순수(?)하지 않은 함수를 호출하기

앞서 정의한 actions의 리듀서를 작성해보자
```
import { VisibilityFilters } from './actions'

const initialState = {
    visibilityFilter: VisibilityFilters.SHOW_ALL,
    todos: []
}

// Redux는 처음에 리듀서를 undefined 상태로 호출한다. 
// 이 때 초기 상태를 반환한다.
function todoApp(state = initialState, action) {
    // 지금은 아무 액션도 다루지 않고 주어진 상태를 그대로 반환
    return State
}
```

`SET_VISIBILITY_FILTER`는 상태에서 `visibilityFilter`를 바꾸기만 한다.
```
function todoApp(state = initialState, action) {
    switch (action.type) {
        case SET_VISIBILITY_FILTER:
            // Object.assign() 을 통해 복사본을 만든다.
            // 반드시 첫번째 인수로 빈 객체를 전달해야 한다.
            // spread syntax를 사용하여,
            // { ...state, ...newState }로 작성할 수도 있다.
            return Object.assign({}, state, {
                visibilityFilter: action.filter
            });
        // 알 수 없는 액션에 대해서는,
        // 이전의 state를 반환하는 것이 중요하다.
        default:
            return state
    }
}
```

`ADD_TODO`를 추가
```
function todoApp(state = initialState, action) {
    switch (action.type) {
        case SET_VISIBILITY_FILTER:
            return Object.assign({}, state, {
                visibilityFilter: action.filter
            });
        case ADD_TODO:
            return Object.assign({}, state, {
                todos: [...state.todos, {
                    text: action.todo,
                    completed: false
                }]
            });
        default:
            return state;
    }
}
```
마지막으로 `COMPLETE_TODO` 핸들러를 구현
```
case COMPLETE_TODO:
    return Object.assign({}, state, {
        todos: [
            ...state.todos.slice(0, action.index),
            Object.assign({}, state.todos[action.index], {
                completed: true
            }),
            ...state.todos.slice(action.index + 1)
        ]
    });
```
#### 2-3. 리듀서 쪼개기
좀 더 이해하기 쉽게 만들기 위해 `todos`와 `visibilityFilter`를 별도의 함수로 분리하는 것이 좋아보인다.
```
function todos(state = [], action) {
    switch (aciton.type) {
        case ADD_TODO:
            return [...state, {
                text: action.todo
                complete: false
            }];
        case COMPLETE_TODO:
            return [
                ...state.slice(0, action.index),
                Object.assign({}, state[action.index], {
                    completed: true
                }),
                ...state.slice(action.index+1)
            ];
        default:
            return state;
    }
}

function todoApp(state = initialState, action) {
    switch (action.type) {
        case SET_VISIBILITY_FILTER:
            return Object.assign({}, state, {
                visibilityFilter: action.filter
            });
        case ADD_TODO:
        case COMPLETE_TODO:
            return Object.assign({}, state, {
                todos: todos(state.todos, action)
            });
        default:
            return state;
    }
}
```
`visibilityFilter` 만을 관리하는 리듀서로 나눠 보자
```
function visibilityFilter(state = SHOW_ALL, action) {
    switch (action.type) {
        case SET_VISIBILITY_FILTER:
            return action.filter;
        default:
            return state;
    }
}
```
이제 메인 리듀서를 state의 부분들을 관리하고 하나의 객체로 조합하는 함수로 재작성할 수 있다. 또한 완전한 초기 상태도 필요 없다. 처음에 undefined가 주어지면 자식 리듀서들이 각각의 초기 상태를 반환하면 된다.
```
function todos(state = [], action) {
    switch (action.type) {
        case ADD_TODO:
            return [...state, {
                text: action.todo,
                completed: false
            }];
        case COMPLETE_TODO:
            return [
                ...state.slice(0, action.index),
                Object.assign({}, state[action.index], {
                    completed: true
                }),
                ...state.slice(action.index + 1)
            ];
        default:
            return state;
    }
}

function visibilityFilter(state = SHOW_ALL, action) {
    switch (action.type) {
        case SET_VISIBILITY_FILTER:
            return action.filter;
        default:
            return state;
    }
}

function todosApp(state = {}, action) {
    return {
        visibilityFilter: visibilityFilter(state.visibilityFilter, action),
        todos: todos(state.todos, action)
    }
}
```
마지막으로, Redux는 todoApp이 위에서 했던 것과 동일한 보일러플레이트 로직을 지원하는 `combineReducers()라는 유틸리티를 제공한다. 이를 이용하면 다음과 같이 작성할 수 있다.
```
import { combineReducers } from 'redux';

const todoApp = combineReducers({
    visibilityFilter,
    todos
});

export default todoApp;
```
이는 아래와 완전히 의미가 같은 코드다.
```
export default function todoApp(state, action) {
    return {
        visibilityFilter: visibilityFilter(state.visibilityFilter, action),
        todos: todos(state.todos, action)
    };
}
```
이해하기 쉬운 예제로 확인해보자
```
const reducer = combineReducers({
    a: doSomethingWithA,
    b: processB,
    c: c
});
```
```
function reducer(state, action) {
    return {
        a: doSomethingWithA(state.a, action),
        b: processB(state.b, action),
        c: c(state.c, action)
    };
}
```

>`combineReducers`는 객체를 기대하기 때문에, 모든 최상위 리듀서들을 각기 다른 파일에 놓고 `export`한 다음 `import * as reducers`를 이용해 각각의 이름을 키로 가지는 객체를 얻을 수 있다.
>```
>import { combineReducers } from 'redux';
>import * as reducers from './reducers';
>
>const todoApp = combineReducers(reducers);
>```

*완성된 소스 ./reducers.js*

### 3. 스토어
"무엇이 일어날지"를 나타내는 `액션`과 액션에 따라 상태를 수정하는 `리듀서`까지 작성한 뒤에는 이들을 가져오는 `스토어`를 작성해야 한다.

스토어는 아래와 같은 일들을 한다.
- 애플리케이션의 상태를 저장
- getState()를 통해 상태에 접근
- dispatch(action)를 통해 상태를 수정
- subscribe(listener)를 통해 리스너를 등록

Redux 애플리케이션에는 단 하나의 스토어만 가질 수 있다. 만약 데이터를 다루는 로직을 쪼개고 싶다면, 여러 개의 스토어 대신 리듀서 조합을 사용하도록 하자

`combineReducers()`를 통해 여러 리듀서를 하나로 합쳤으니, 이것을 가져와 `createStore()`로 넘기면 된다.
```
import { createStore } from 'redux';
import todoApp from './reducers';

let store = createStore(todoApp);
```
`createStore()의 두번째 인수로 초기 상태를 지정해줄 수도 있다. 이는 서버에서 실행 중인 Redux 애플리케이션의 상태와 일치하도록 클라이언트의 상태를 채워줄 때 유용하다.
```
let store = createStore(todoApp, window.STATE_FROM_SERVER);
```

완성된 소스 ./index.js

[출처](https://deminoth.github.io/redux/basics/Reducers.html)
