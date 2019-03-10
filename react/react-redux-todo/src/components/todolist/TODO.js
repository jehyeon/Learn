class TODO extends Component {
    render() {
        const { id, todo, complete, onClick } = this.props;     // 컨테이너 컴포넌트에서 받은 prop
        return (
            <li id={id}
                onClick={() => onClick({
                    id: id,
                    complete: !complete
                })}
                className={!!complete ? 'completed': ''}
            >{todo}</li>
        );
    }
}