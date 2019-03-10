// action type(명령어)
export const COMPLETE_TODO = 'COMPLETE_TODO'

// actions create(액션 메서드)
export function complete({complete, id}) {
    return { type: COMPLETE_TODO, complete, id}
}