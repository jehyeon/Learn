import { createAction, handleActions } from 'redux-actions';

const CHANGE_INPUT = 'waiting/CHANGE_INPUT';    // 인풋 값 변경
const CREATE = 'waiting/CREATE';                // 명단에 이름 추가
const ENTER = 'waiting/ENTER';                  // 입장
const LEAVE = 'waiting/LEAVE';                  // 나감               

// 액션 생성 함수 정의 (FSA 규칙)
// export const changeInput = text => ({ type: CHANGE_INPUT, payload: text });
// export const create = text => ({ type: CREATE, payload: text });
// export const enter = id => ({ type: ENTER, payload: id });
// export const leave = id => ({ type: LEAVE, payload: id });

let id = 0;
// createAction 으로 액션 생성 함수 정의
export const changeInput = createAction(CHANGE_INPUT, text => text);
export const create = createAction(CREATE, text => ({ text, id: id++}));
export const enter = createAction(ENTER, id => id);
export const leave = createAction(LEAVE, id => id);

// 초기 상태 정의 
const initialState = {
    input: '',
    list: []
}

// handleActions 로 리듀서 함수 작성
// contact, map, filter 로 불변성 유지
export default handleActions(
    {
        [CHANGE_INPUT]: (state, action) => ({
            ...state,
            input: action.payload,
        }),
        [CREATE]: (state, action) => ({
            ...state,
            list: state.list.concat({
                id: action.payload.id,
                name: action.payload.text,
                entered: false,
            }),
        }),
        [ENTER]: (state, action) => ({
            state,
            list: state.list.map(
                item =>
                    item.id === action.payload
                        ? {...item, entered: !item.entered }
                        : item
            ),
        }),
        [LEAVE]: (state, action) => ({
            ...state,
            list: state.list.filter(item => item.id !== action.payload)
        }),
    },
    initialState
);