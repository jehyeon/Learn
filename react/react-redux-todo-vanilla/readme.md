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

### 4. 데이터 흐름
Redux의 아키텍쳐는 엄격한 일방향 데이터 흐름에 따라 전개된다. 애플리케이션 내의 모든 데이터가 같은 생명주기 패턴을 따르기 때문에, 앱의 로직을 좀 더 예측 가능하게 하고 이해하기 쉽게 만든다.

#### 모든 Redux 앱에서의 데이터는 아래와 같이 4단계의 생명 주기를 따른다.
1. store.dispatch(action)을 호출
액션은 무엇이 일어날지 기술하는 보통의 오브젝트다. 
```
{ type: 'LIKE_ARTICLE', articleId: 42};
{ type: 'FETCH_USER_SUCCESS', response: { id: 3, name: 'Megan' } };
{ type: 'ADD_TODO', text: 'Read the Redux docs.' };
```
`store.dispatch(action)`은 앱 내의 어디서나 호출될 수 있다. (컴포넌트나 XHR 콜백, 심지어 일정한 간격으로도)

2. Redux 스토어가 리듀서 함수들을 호출
스토어는 리듀서에 현재의 상태와 실행되는 액션 두 가지 인수를 넘긴다.
```
// 애플리케이션의 현재 상태(할일 목록과 선택된 필터)
let previousState = {
    visibleTodoFilter: 'SHOW_ALL',
    todos: [{
        text: 'Read the docs.',
        complete: false
    }]
};

let action = {
    type: 'ADD_TODO',
    text: 'Understand the flow.'
};

// 리듀서가 다음 상태를 반환함
let nextState = todoApp(previousState, action);
```

3. 루트 리듀서로 각 리듀서의 출력을 합쳐서 하나의 상태 트리를 만듦
Redux는 루트 리듀서를 각각 상태 트리의 가지 하나씩 다룰 수 있도록 `combineReducers()` 헬퍼 함수를 제공한다.

`combineReducers()`의 작동 방식은 아래와 같다. 하나는 할일 목록을 위한 것이고, 하나는 선택된 필터 설정을 위한 것이다.

```
function todos(state = [], action) {
    // Somehow calculate it
    return nextState;
}

function visibleTodoFilter(state = 'SHOW_ALL', action) {
    // Somehow calculate it
    return nextState;
}

let todoApp = combineReducers({
    todos,
    visibleTodoFilter
});
```
`todoApp`을 호출 시 `combineReducers`가 아래 두 리듀서 호출한다.
```
let nextTodos = todos(state.todos, action);
let nextVisibleTodoFilter = visibleTodoFilter(state.visibleTodoFilter, action);
```
그리고 두 결과를 합펴서 하나의 상태 트리로 만들어진다. 
```
return {
    todos: nextTodos,
    visibleTodoFilter: nextVisibleTodoFilter
};
```
4. Redux 스토어가 루트 리듀서에 의해 반환된 상태 트리를 저장
새 트리가 앱의 다음 상태다. `store.subcribe(listener)`를 통해 등록된 모든 리스너가 불러지고 이들은 현재 상태를 얻기 위해 `store.getState()`를 호출한다.

이제 newState를 반영하여 UI 변경된다. React Redux로 바인딩을 했다면 이 시점에서 component.setState(newState)가 호출된다.

### 5. React와 함께 사용하기
#### Presentational 컴포넌트 설게하기
- AddTodo는 버튼이 달린 input 필드
    + onAddClick(text: string)
- TodoList는 표시 중인 할일 목록
    + todos: Array는 { text, completed } 형태의 할일 배열
    + onTodoClick(index: number)
- Todo는 할일 하나
    + text: strng, 보여줄 텍스트
    + completed: boolean, 할일이 완료되었는지에 대한 여부
    + onClick()
- Link
- Footer는 할일 필터를 사용자가 바꿀 수 있게끔 해주는 컴포넌트
- App은 다른 모든 컴포넌트를 렌더링하는 최상단 컴포넌트

이 컴포넌트들은 모두 *외양*을 담당하지만 데이터가 어디에서 오는 것인지, 또 어떻게 데이터를 변경해야 하는지는 알지 못한다. 그저 주어진 것을 표시하기만 한다. 만약 Redux가 아닌 다른 무언가를 쓰게 된다면 이 모든 컴포넌트들을 그대로 유지할 수 있다. Redux에 대한 의존성이 없기 때문이다.

#### Container 컴포넌트 설계하기
Presentational 컴포넌트를 Redux에 연결하기 위해서는 Container 컴포넌트가 필요하다. 에를 들어, `TodoList` presentational 컴포넌트는 `VisibleTodoList`와 같은 container 컴포넌트를 필요로 한다. `VisibleTodoList`는 Redux 스토어의 변경사항을 구독하고 현재 필터를 어떻게 적용해야 할 지를 아는 컴포넌트다. 필터를 변경하기 위해, `FilterLink` 컴포넌트를 만들어서 `Link` 컴포넌트를 렌더링하고 여기에 클릭이 일어날 때마다 적절한 액션을 파견해 줄 것이다.
- `VisibleTodoList` 컴포넌트는 현재 필터 상태에 따라 할일 목록을 필터링해서 `TodoList` 컴포넌트를 표시한다.
- `FilterLink` 컴포넌트는 현재 필터 상태를 가져와서 `Link` 컴포넌트를 표시한다.
    + filter: string 속성에는 이 컴포넌트가 어떤 필터를 나타내는지 저장

#### 그 밖의 컴포넌트 설계하기
어느 컴포넌트로 만들어야할 지 결정하기 어려운 경우가 있다. 예를 들어, 다음과 같이 폼과 기능이 밀접하게 결합되어 있는 경우이다.
- AddTodo 컴포넌트는 'Add' 버튼이 있는 입력 필드이다.

아주 작은 컴포넌트의 경우 외양과 논리구조가 섞여있어도 괜찮다. 컴포넌트가 커짐에 따라, 그것을 어떻게 쪼개야 할 지 더 명확해질 것이므로, 일단은 섞은 채로 만든다.

#### Presentational Component 구현하기
우리는 지역 상태나 생애주기(lifecycle) 메소드가 필요하지 않은 경우 항상 상태를 갖지 않는 함수형 컴포넌트를 만들 것이다. 만약 지역 상태나 생애주기 메소드, 혹은 성능 최적화가 필요할 때가 오면 클래스로 바꿔주면 된다.

component/Todo.js
```
import React from 'react';
import PropTypes from 'prop-types';

const Todo = ({ onClick, completed, text }) => (
    <li
        onClick={onClick}
        style={{
        textDecoration: completed ? 'line-through': 'none'
        }}
    >
        {text}
    </li>
);

Todo.propTypes = {
    onClick: PropTypes.func.isRequired,
    completed: PropTypes.bool.isRequired,
    text: PropTypes.string.isRequired
};

export default Todo;
```

components/TodoList.js
```
import React from 'react';
import PropTypes from 'prop-types';
import Todo from './Todo';

const TodoList = ({ todos, onTodoClick }) => {
    <ul>
        {todos.map((todo, index) => (
            <Todo key={index} {...todo} onClick={() => onTodoClick(index)} />
        ))}
    </ul>
}

TodoList.propTypes = {
    todos: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            completed: PropTypes.bool.isRequired,
            text: PropTypes.string.isRequired
        }).isRequired
    ).isRequired,
    onTodoClick: PropTypes.func.isRequired
};

export default TodoList;
```

component/Link.js
```
import React from 'react';
import PropTypes from 'prop-types';

const Link = ({ active, children, onClick }) => {
    if (active) {
        return <span>{children}</span>
    }

    return (
        <a
            href=''
            onClick={e => {
                e.preventDefault()
                onClick()
            }}
        >
            {children}
        </a>
    )
}

Link.propTypes = {
    active: PropTypes.bool.isRequired,
    children: PropType.node.isRequired,
    onClick: PropType.func.isRequired
};

export default Link;
```

component/Footer.js
```
import React from 'react';
import FilterLink from '../container/FilterLink';

const Footer = () => {
    <p>
        Show:
        {' '}
        <FilterLink filter='SHOW_ALL'>
            All
        </FilterLink>
        {', '}
        <FilterLink filter='SHOW_ACTIVE'>
            Active
        </FilterLink>
        {', '}
        <FilterLink filter='SHOW_COMPLETED'>
            Completed
        </FilterLink>
    </p>
}

export default Footer;
```

#### Component 컴포넌트 구현하기
~

[출처](https://deminoth.github.io/redux/basics/Reducers.html)
