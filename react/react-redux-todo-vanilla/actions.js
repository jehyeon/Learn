// 액션 타입
export const ADD_TODO = 'ADD_TODO';
export const COMPLETE_TODO = 'COMPLETE_TODO';
export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER';

// 다른 상수
export const VisibilityFilters = {
    SHOW_ALL: 'SHOW_ALL',
    SHOW_COMPLETED: 'SHOW_COMPLETED',
    SHOW_ACTIVE: 'SHOW_ACTIVE'
}

// 액션 생산자
export function addTodo(todo) {
    return { type: ADD_TODO, todo }
}

export function completeTodo(todo_index) {
    return { type: COMPLETE_TODO, todo_index}
}

export function setVisibilityFilter(filter) {
    return { type: SET_VISIBILITY_FILTER, filter}
}