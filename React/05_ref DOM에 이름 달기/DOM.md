ref

- HTML에서는 DOM을 구분하기 위해 id 를 사용한다 `<div id='name'> </div>`
- 리액트 프로젝트 내부에서 DOM에 이름을 다는 방법 : ref 태그 사용
- DOM을 꼭 직접적으로 건드려야 할 때 사용



DOM 을 사용해야 하는 상황

- 특정 input에 포커스 주기
- 스크롤 박스 조작하기 
- Canvas 요소에 그림 그리기 등

이와 같은 경우에는 DOM에 직접적으로 접근해야 한다. 이 상황에서 ref를 사용한다.



ref 사용 방법

- 콜백 함수를 통한 ref 설정

  - ```react
    <input ref={(ref) => {this.input=ref}} />
    ```

  - 콜백 함수를 props로 전달.

  - 이렇게 하면 `this.input` 은 input 요소의 DOM을 가리킴

- createRef를 통한 ref 설정

  - 리액트에 내장되어 있는 createRef 함수 사용

  - ```react
    inport {Component } from 'react'
    
    class RefSample extends Component {
        input = React.createRef();
        
        handleFocus = () => {
            this.input.current.focus();			// 클릭하면 포커스 적용
        }
        
        render() {
            return (
            <div>
                <input ref={this.input}>
            </div>
            )
        }
    }
    ```

  - ref props로 넣어줌

  - 이후 해당 DOM에 접근하려면 `this.input.current`를 조회