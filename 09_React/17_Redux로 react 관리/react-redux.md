순서

1. 모듈 작성하기
2. 폴더 최상단에 modules 폴더 만들고, 액션 타입, 액션 생성함수, 리듀서 함수를 기능별로 작성
   - 액션 타입 정의 - 액션 생성 함수 제작 - 초기 상태 및 리듀서 함수 제작 - 루트 리듀서 제작 순으로 진행
3. 리액트 앱에 리덕스 적용하기
   - 스토어 생성
   - Provider 컴포넌트를 사용하여 프로젝트에 리덕스 적용
     - 이후 크롬 확장프로그렘 redux devtools 설치,`npm install redux-devtools-extension`
4. 컴포넌트에서 리덕스 스토어에 접근
   - `connect` 함수 사용
   - `mapStateToProps` , `mapDispatchProps` 에서 반환하는 객체 내부의 값들은 컴포넌트의 props로 전달됨. `mapStateToProps` 는 `state`를 파라미터로 받아오고, `mapDispatchProps`는 `stroe`의 내장 함수 `dispatch`를 파라미터로 받아옴