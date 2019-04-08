# vanilla todo app using reduxer

### 1. 액션 / 액션 생산자

#### 액션은 애플리케이션에서 스토어로 보내는 데이터 묶음 (스토어의 유일한 정보원)
sotre.dispatch()를 통해 이들을 보낼 수 있다.

    const ADD_TODO = 'ADD_TODO';

    {
        type: ADD_TODO,
        text: 'Build my first Redux app'
    }

액션은 평범한 자바스크립트 객체다. 
액션은 반드시 어떤 형태의 액션이 실행될 지 나타내는 type 속성을 가져야 한다.
타입은 일반적으로 문자열 상수로 정의된다. 


    import { ADD_TODO, REMOVE_TODO } from '../actionTypes'

이와 같이 별도의 모듈로 분리할 수도 있다.


사용자가 할일을 완료했다고 체크하는 액션 하나를 추가해보자.
할일은 배열 안에 저장되기 때문에 특정한 할일을 index를 통해 참조할 수 있다.

    {
        type: COMPLETE_TODO,
        index: 5
    }

각 액션에는 가능한 적은 데이터를 전달하는 것이 좋다.

---
#### 액션 생산자는 액션을 만드는 함수이다.

Redux의 액션 생산자는 단지 액션을 반환한다.

    function addTodo(text) {
        return {
            type: ADD_TODO,
            text
        }
    }

이는 액션 생산자를 더 이식하기 좋고 테스트하기 쉽게 한다.
실제로 액션을 보내려면 결과값을 dispatch() 함수에 넘긴다.

    dispatch(addTodo(text));
    dispatch(completeTodo(index));

혹은 자동으로 액션을 보내주는 바인드된 액션 생산자를 만든다.

    const boundAddTodo = (text) => dispatch(addTodo(text));
    const boundCompleteTodo = (index) => dispatch(complete(index));

dispatch() 함수를 스토어에서 store.dispatch()로 바로 접근할 수 있지만,
보통 react-redux의 connect()와 같은 헬퍼를 통해 접근한다.

여러 액션 생상자를 dispatch()에 바인드하기 위해 bindActionCreators()를 사용할 수도 있다.

*완성된 소스 ./actions.js*
