# Vue 인스턴스

## Vue 인스턴스 만들기
`Vue` 함수로 새 Vue 인스턴스를 만드는 것부터 시작합니다.
```
// vm: ViewModel의 약자
var vm = new Vue({
  // options
})
```

Vue 인스턴스를 인스턴스화 할 때는 데이터, 템플릿, 마운트할 엘리먼트, 메소드, 라이프사이클 콜백 등의 옵션을 포함할 수 있는 option 객체를 전달해야 합니다.
전체 옵션 목록은 [API reference](https://kr.vuejs.org/v2/api/)에서 확인할 수 있습니다.

`Vue` 생성자는 미리 정의된 옵션으로 재사용 가능한 컴포넌트 생성자를 생성하도록 확장 될 수 있습니다. 자세한 컴포넌트 시스템은 [Component guide](https://kr.vuejs.org/v2/guide/instance.html)에서 확인할 수 있습니다.

## 속성과 메소드
각 Vue 인스턴스는 `data` 객체에 있는 모든 속성을 프록시 처리합니다.

```
// 데이터 객체
var data = { a: 1 }

// Vue 인스턴스에 데이터 객체를 추가
var vm = new Vue({
  data: data
})

// 같은 객체를 참조한다.
vm.a === data.a // true

// 속성 설정은 원본 데이터에도 영향을 준다
vm.a = 2
data.a // 2
```
데이터가 변경되면 화면은 다시 렌더링 됩니다. 유념할 점은, `data`에 있는 속성들은 인스턴스가 생성될 때 존재한 것들만 반응형이라는 것입니다. 따라서, **새 속성을 추가하면 화면에 갱신되지 않습니다.**

그렇기 때문에, 어떤 속성이 나중에 필요하거나, 빈 값 혹은 존재하지 않은 상태로 시작하는 경우에는 초기값을 지정할 필요가 있습니다.
```
data: {
  newTodoText: '',
  visitCount: 0,
  hideCompletedTodos: false,
  todos: [],
  error: null
}
```

여기에서 유일한 예외는 `Object.freeze()`를 사용하는 경우입니다. 이는 기존 속성이 변경되는 것을 막습니다.
```
var obj =  {
  foo: 'bar'
}

Object.freeze(obj)

new Vue({
  el: '#app',
  data: obj
})
```
```
<div id="app">
  <p>{{ foo }}</p>
  <!-- obj.foo는 변하지 않는다 -->
  <button v-on:click="foo='baz'">Change it</button>
</div>
```

Vue 인스턴스는 데이터 속성 이외에도 유용한 인스턴스 속성 및 메소드를 제공합니다. 다른 사용자 정의 속성과 구분하기 위해 `$` 접두어를 붙였습니다.
```
var data = { a: 1 }
var vm = new Vue({
  el: '#example',
  data: data
})

vm.$data === data // true
vm.$el === document.getElementById('example') // true

// $watch는 인스턴스 메소드 입니다.
vm.$watch('a', function (newVal, olVal) {
  // vm.a가 변경되면 호출 됩니다.
})
```

## 인스턴스 라이프사이클 훅
각 Vue 인스턴스는 생성될 때 일련의 초기화 단계를 거칩니다. 예를 들어, `created` 훅은 인스턴스가 생성된 후에 호출됩니다.

```
new Vue({
  data: {
    a: 1
  },
  created: function () {
    // `this`는 vm 인스턴스를 가리킵니다.
    console.log('a is: ' + this.a)
  }
})
```
>option 속성이나 콜백에 **화살표 함수** 사용을 지양해야 합니다.
>
>화살표 함수들은 부모 컨텍스트에 바인딩되기때문에, `this`를 호출할 때 `Uncaught TypeError: this.myMethod is not a function`와 같은 오류가 발생하게 됩니다.

## 라이프사이클 다이어그램
<img src="./lifecycle.png" />

---
[출처](https://kr.vuejs.org/v2/guide/instance.html)