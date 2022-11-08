# Vuex

상태 관리 시스템

상태

- 현재에 대한 정보.
- 현재 App이 가지고 있는 data 로 표현 가능
- 여러 컴포넌트가 독립적이지만, 같은 상태를 유지할 필요가 있음
  - 지금까지는 props와 event를 이용.
  - but, 컴포넌트가 깊어지면 and 넓어지면, 너무 복잡해짐
  - => 중앙 저장소에 데이터를 모아서 상태 관리

Centralized Store

- 각 컴포넌트가 중앙 저장소의 데이터를 사용
- 컴포넌트의 계층에 상관없이 중앙 저장소에 접근
- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트 관리에 효율적

Vuex

- 상태 관리 패턴 + 라이브러리
- 데이터가 예측 가능한 방식으로만 변경되도록 하는 규칙을 설정
- vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공
- 사용
  - 프로젝트 생성, 디렉토리 이동 이후 `vue add vuex` 입력

- src / store / index.js 안에 규칙에 대한 컨셉이 추가됨
- 핵심 컨셉
  1. state
     - 중앙 저장소에서 관리하는 모든 상태 정보
     - state의 데이터가 변화하면, 연결된 모든 컴포넌트들이 자동으로 다시 렌더링
     - `$store.state` 로 접근해서 사용 (따로 임포트할 필요 x)
  2. getters
     - 기존에 쓰던 computed
     - state를 기준으로 이미 계산된 값 저장
     - 종속된 state가 변경된 경우에만 재계산됨
     - 첫번째 인자로state, 두번째 인자로 getter를 받음
  3. mutations
     - 기존에 쓰던 함수들
     - state를 변경하는 유일한 방법
     - vue 인스턴스의 메서드에 해당하지만, mutations에서 호출되는 핸들러 함수는 반드시 동기적이어야 함
       - 비동기일 경우 state의 변화 시기를 특정할 수 없기 때문에
     - 첫 번째 인자로 state를 받으며, 컴포넌트 혹은 actions에서 commit() 메서드로 호출됨
  4. actions
     - 기존에 쓰던 함수들
     - 비동기 작업을 포함할 수 있음
     - state를 직접 변경하지 않고 commit() 메서드로 mutations를 호출해서 state를 변경함
     - context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근 가능
       - 즉, state도 변경할 수 있지만 하지 않아야 함
     - 컴포넌트에서 dispatch()로 호출

실습

- 이제부터는 객체 메서드 축약형을 사용할 것	

  - ```vue
    const obj = {
    	addValue(value) {
    		return value
    	}
    }
    }
    ```

    형태로

- state

  - 컴포넌트 안에서 바로 `{{ $store.state.message }}` 형태로 state의 변수 message 에 접근 가능
  - but 메서드 사용을 더 권장함

- actions

  - state를 변경할 수 있는 mutations 호출. 컴포넌트에서 `dispatch()`에 의해 호출됨
  - dispatch(A, B) 
    - A : 호출하고자 하는 actions 함수
      - A 안의 context 인자
        - 첫 번째 인자 context는 store의 전반적인 속성을 모두 가지므로, context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
        - 두 번째 인자  payload는 넘겨준 데이터를 받아서 사용
    - B : 넘겨주는 데이터
  - 

# Lifecycle Hooks

각 vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침 (생성, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM 업데이트 하는 경우 등).

이를 Lifecycle Hooks라 함

관련 사진은 공식문서에서 참조



created

- Vue instance가 생성된 수 호출됨
- data, coumputed 등의 설정이 완료된 상태
- 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 편함
- 단, mount되지 않아 (DOM에 연결 x) 요소에 접근할 수 없음
  - 변수.innerText 등에 접근이 불가능 (변수가 unidentied인 상태라서)

- Dog API 에서 created 함수에 강아지 사진 가져오는 함수를 추가해, 처음부터 강아지 사진이 뜨도록 처리



mounted

- 인스턴스가 요소에 mount된 후 호출됨
- mount된 요소 조작 가능
- 자식 컴포넌트가 먼저 mount되고, 이후 부모 컴포넌트가 mount



updated

- 데이터가 변경되어 DOM에 변화를 줄 때 호출됨 



lifecycle hook 폴더 안의 흐름

- App.vue 생성 => ChildComponent 생성 => ChildComponent 부착 => App.vue 부착 => ChildComponent 업데이트 순
- 부모 컴포넌트의 mounted hook이 실행되었다고 해서 자식이 mount 된 것이 아니고, 부모 컴포넌트의 updated hook이 실행되었다고 해서 자식이 updated된 것이 아님
- 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않음
  - 인스턴스마다 각각의 Lifecycle을 가지고 있어서  



# Todo with Vuex

구현 기능

- Todo CRUD
- Todo 개수 계산 (전체, 완료된, 미완성된)





- 새로고침해도 데이터 안사라지게
  - Local Storage
    - 브라우저에서 제공하는 저장공간 중 하나
    - Window.localStorage 로 접근
    - 메서드
      - setItem(key, value)   - 데이터 저장
      - getItem(key)   - 데이터 조회
  - vuex-persistedstate
    - local storage에 자동저장하는 라이브러리
    - Local Storage에 직접 접근하는 코드들 전부 주석 처리, 이후 라이브러리 사용한 코드 작성
