// 액션 타입 정의
// Ducks 패턴을 사용할 땐 문자열의 앞부분에 모듈 이름을 넣는다.
const CHANGE_COLOR = 'counter/CHANGE_COLOR';
const INCREMENT = 'counter/INCREMENT';
const DECREMENT = 'counter/DECREMENT';

// 액션 생성함수 정의 
export const changeColor = color => ({ type: CHANGE_COLOR, color });
export const increment = () => ({ type: INCREMENT });
export const decrement = () => ({ type: DECREMENT });

// 초기상태 정의
const initialStore = {
    color: 'red',
    number: 0,
};

// 리듀서 작성
export default function counter(state = initialStore, action) {
    switch (action.type) {
        case CHANGE_COLOR:
            return {
                ...state,
                color: action.color,
            };
        case INCREMENT:
            return {
                ...state,
                number: state.number + 1,
            };
        case DECREMENT:
            if (state.number > 0) {
                return {
                    ...state,
                    number: state.number - 1,
                };
            } else {
                return state;
            }
        default:
            return state;
    }
}