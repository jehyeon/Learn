class TODOList extends Component {
    render() {
        const { todos, onClick } = this.props;
        return (
            <ul>
                {todos.map(todo => 
                    <Todo
                        key={todo.id}
                        onClick={onClick}
                        {...todo}
                    />
                )}
            </ul>
        );
    }
}

// 컨테이너 컴포넌트에서 프레젠테이션 컴포넌트로 전달하는 state
const todolistStateToProps = (state) => {
    return {
        todos: state.todos
    }
}

// 컨테이너 컴포넌트에서 프레젠테이션 컴포넌트로 액션을 보내는 함수
const todolistDispatchToProps = (dispatch) => {
    return {
        onClick(data) {
            dispatch(complete(data))        // 액션 메서드
        }
    }
}


// 연결
export default connect(todolistStateToProps, todolistDispatchToProps)(TODOList);