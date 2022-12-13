# vue 처음부터

1. 터미널에서 `$ vue create {프로젝트명}` 입력해서 프로젝트 생성
2. 해당 프로젝트로 이동 `cd {프로젝트명/}`
3. `npm run serve`



lodash 쓰는 법

- 터미널에서 `npm install lodash` 하면 CDN 붙여넣을 필요 없이 사용 가능
- 임포트 해오기
  - `import _ from 'lodash'`





## 배운거

v-model, v-on, v-bind

v-bind 를 해야 JS 형태로 변수, 함수 등을 사용할 수 있다.

- v-model

  - 양방향 바인딩

  - v-on 과 v-bind 기능을 합침

  - 변화가 일어나는 즉시 해당 변화를 반영

  - 사용법

    - `v-model="{변수 명}"`

  - but, 영어 외의 문자에 대해서는 한 박자 늦게 반영되는 문제가 있음. 그래서 한글 쓸때는 v-bind, v-on 합쳐서 구현

  - 사용법

    - ```vue
      <input
        :value="myData"
        @input="event => myData = event.target.value">
      ```

    - 공식 문서 참조 https://vuejs.org/guide/essentials/forms.html#Basic-Usage

    - 만약 `@input `에 다른 함수도 사용해야 한다면, arrow function 뒷부분을 `{}`로 묶은 뒤 JS 함수 쓰듯이 사용 (이것도 굳이 기록해야하나?)

- v-bind

  - 뷰 인스턴스의 데이터 속성을 해당 HTML 요소에 연결할 때 사용
  - 말 그대로, 속성을 바꾸는 데 사용
    - 위의 코드에서 `:value="myData"`  같은 경우, input 안의 값(속성 value)을 myData로 사용하겠다는 뜻? 잘 모르겠다

- v-on

  - 해당 HTML 요소의 이벤트를 뷰 인스턴스의 로직과 연결할 때 사용 (어떤 함수가 발생했을 시 작동한다고 생각)



폰트 가져오기

- google fonts 사이트에서 'selected families'에 원하는 것들 추가
- `@import ~~~ 하기`
- 이후 ` font-family: 'Noto Sans KR', sans-serif;` 적어서 사용. 구글 폰트에서 시키는대로 하자.

클래스 조건문으로 나누기

- ```vue
  	 <button 
          :class="{'light': 조건문1, 'blue': 조건문2}"
        > 반복 출력할 문자 </button>
  ```

  조건문1, 조건문2 는 결과가 boolean으로 나오는 식

  조건문 1이 true면 클래스의  'light' CSS 적용, 조건문 2가 true면 클래스의 'blue' 적용

- 



axios 사용

- https://herojoon-dev.tistory.com/131  참조
- `npm i axios` 해서 설치한 뒤, main.js 에 axios 임포트하기
- API 사용 시 헷갈리면 axios github 가서 찾아보기

  - ```js
    axios.get('/user', {
        params: {
          ID: 12345
        }
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      })
      .finally(function () {
        // always executed
      });
    ```

- 위 방식으로 하지 말고,




keyup.enter

1. 그 데이터로 emit 하기
2. 그 데이터를 childData에 넣기



emit 하는 법

1. 자식 컴포넌트에서 함수 만들고, emit 함수 실행

   `this.$emit('send-input-search-bar', this.inputSearchBar)`

2. 부모 컴포넌트에서 emit 받는 함수 만들기

3. 부모 컴포넌트에서 <div> 안의 자식 컴포넌트에 v-on으로 함수 연결

   `<{자식 컴포넌트} @{부모 컴포넌트의 함수 명}="{자식 컴포넌트에서의 emit 함수 명}"`



유튜브 API 활용

- https://developers.google.com/youtube/v3/docs/search/list?hl=ko 참조
- axios 사용 시, 그냥 url에 key, part, 그런거 전부 넣어버리기
- 
