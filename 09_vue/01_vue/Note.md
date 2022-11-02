# Vue.js

# Vue Intro

프론트엔드 개발 도구

Web app을 만들 때 사용하는 도구

web app이란?

- 같은 화면을 디바이스로 볼 때 다르게 표현하여, 디바이스에 설치된 것처럼 표현하는 것

SPA (Single Page Application)

- 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
- 방법 
  - CSR (Client Side Renderting) 방식, 클라이언트가 바뀐 부분내용을 수정
  - 기존의 요청 방식 (이전까지 배운 것) : 서버가 모든 요청을 처리한 뒤 전송
- 각 요청에 대한 대응을 JS를 사용하여 필요한 부분만 다시 렌더링
  1. 필요한 페이지를 서버에 AJAX로 요청
  2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
  3. JSON 데이터를 JS로 처리, DOM 트리에 반영(렌더링)
- 장점
  - 트래픽 감소 == 응답 속도가 빨라진다
  - 필요한 부분만 고치므로 각 요청이 끊김없이 진행 (좋아요 누를 때마다 새로고침 x)
  - BE, FE의 작업 영역을 명확히 분리
- 단점
  - 첫 구동 시 필요한 데이터가 많을수록 최초 작동 시작까지 오랜 시간 소요
  - 네이버, 넷플릭스 등 모바일에 설치된 Web-App을 실행하게 되면 잠깐의 로딩 시간이 필요 (브랜드 로고 등을 띄워서)
  - 검색 엔진 최적화 (SEO, Search Engine Optimization)가 어려움
    - 서버가 제공하는 건 빈 HTML 뿐, 내용은 AJAX 요청으로 얻은 JSON 데이터이므로
    - but, 최근에는 CSR로 구성된 서비스 비중이 증가 (JS도 지원)



vue를 배우는 이유

- 쉬워서
- 이후 다른 FE 프레임워크 학습 시에도 빠르게 적응 가능





## style guide

1. v-for 는 항상 key와 함께 사용하기
2. v-for 쓴 엘리먼트에 절대 v-if 사용하지 않기  (v-if 가 먼저 계산되고, 해당 처리 시점에 반복 변수인 user가 존재하지 않기 때문에 에러 발생)

# Vue Instance



## Vue CDN

ppp html에 표시

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<!-- development version, includes helpful console warnings -->
```



## MVVM 패턴

- 소프트웨어 키텍처 패턴의 일종
- Model (실제 데이터 JSON) - view (눈에 보이는 부분) - ViewModel (vue가 담당, vue와 연결되어 액션을 주고받음, View Model의 데이터가 변경되고 바인딩된 다른 View도 변경)
- MVC 패턴에서 Controller를 제외하고 View Model을 넣으 ㄴ패턴
- DOM은 Data를 모르고, Data도 View를 모른다
- View, Model 은 완전히 분리.



생성자 함수

- 05_constructo_func.js 참조
- 동일한 형태의 객체를 만들기 위해 new 연산자로 사용하는 함수
- vue 객체 선언 시에도 생성자 함수를 사용

data

- vue 인스턴스의 데이터 객체 혹은 인스턴스 속성
- 데이터 객체는 반드시 기본 객체 {}여야 함 (그냥 문자열이 아닌, {}로 둘러싸인 문자열) 
- 정의된 속성은 보간법 `{{}}`을 통해 view에 렌더링 가능
- 추가된 객체의 각 값들은 this.message 형태로 접근 가능

실습

- 04_vue_start.html 참조

- 1. vue 인스턴스 생성

  2. vue 인스턴스와 DOM 연결

     - el 옵션 사용
     - Vue 인스턴스와 DOM을 연결하는 옵션
     - HTML id 혹은 class와 마운트 가능
     - Vue 인스턴스와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음

  3. data

  4. methods

     - js 함수에서 this 는 호출되는 것에 따라 다름
     - 여기서 this는 자신을 호출한 객체 Vue를 나타냄

     4-1. arrow function에서의 this 는 해당 객체의 상위 객체를 나타내게 됨

     ​	그래서 메서드를 정의할 때 arrow function을 쓰면 window르 ㄹ가리키게 됨

     ​	이 경우 this로 Vue의 data를 변경하지 목함

     ​	하면 어떻게 되는지 4-1에서 확인. 콘솔 창에서 app.arrowBye()를 하면 윈도우를 가리키게 됨



# Basic of Syntax

Vue 2 guide > template syntax 참고

렌더링 된 DOM을 기본 vue 인스턴스의 data에 선언적으로 바인딩할 수 있는 HTML 기반 template syntax를 사용

Directives

- v-접두사가 있는 특수 속성에는 값을 할당할 수 있음

- 값에는 JS 표현식을 작성할 수 있음

- 기본 구성

  - directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것

  - `v-on:submit.prevent="onSubmit"` : submit을 막고 (이벤트 리스터의 prevent와 같음) 

  - v-text

    - `{{ }}` 와 거의 같이 사용

  - v-html

    - RAW HTML을 표현할 수 있는 방법
    - 단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지 (XSS 공격 참고)

  - v-show

    - 표현식의 boolean 값에 따라 element를 보여줄지 말지 판단 
    - 개발자 도구로 보면 기본 속성 또는 none 형태로 toggle
    - 요소 자체는 항상 DOM에 렌더링 됨

  - v-if

    - v-show와 사용 방법은 동일
    - 단, 값이 false인 경우 DOM에서 사라짐
    - v-if, v-else-if, v-else 형태로 사용

  - v-show 와 v-if 차이

    - v-show 
      - 결과 상관없이 렌더링 되므로, 초기 렌더링 비용은 크지만 toggle 비용은 적음
      - false인 경우 렌더링조차 되지 않으니, 초기 렌더링 비용은 낮지만 매번 같은 내용을 새로 렌더링해야하니 toggle 비용은 큼

  - v-for

    - for ... in ... 형식으로 작성
    - index를 함께 출력하고자 한다면 (char, index) 형태로 출력

  - v-on

    - `:`을 통해 전달받은 인자를 확인
    - `:`을 통해 전달된 인자에 따라 특별한 modifiers 가 있을 수 있음
      - v-on:keyup.enter
    - `@` shortcut 제공
    - 값으로 JS 표현식 작성
    - addEventListener 의 첫번째 인자와 동일한 값들로 구성
    - 대기하고 있던 이벤트 발생 시 할당된 표현식 실행

  - v-bind

    - 뒤쪽에 오는 속성 값의 값을 JS의 표현식으로 바꿈

      - 이는 a 태그의 href 작성과 같은 역할

      ```html
          <a v-bind:href="url">Go To GOOGLE</a>
      ```

    - css 도 사용 가능

    - ```html
          <p v-bind:class="{ 'red-text': true }">빨간 글씨</p>					# 조건부 바인드
          <p v-bind:class="[redTextClass, borderBlack]">빨간 글씨, 검은 테두리</p>	 # 다중 바인드
      ```

    - `:` shortcut 제공

  - v-model

    - vue 인스턴스와 DOM의 양방향 바인딩
    - vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용

실습 

- 06_basic_of_syntax.html 참고

- ```html
    <div id="app">
      <p>메시지: {{ msg }}</p>   				 # 출력
      <p>HTML 메시지 : {{ rawHTML }}</p>
      <p>HTML 메시지 : <span v-html="rawHTML"></span></p>		# 표현식. 빨간 글씨 출력
      <p>{{ msg.split('').reverse().join('') }}</p>				# JS 표현식. 뒤에서부터 출력
    </div>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          msg: 'Text interpolation',
          rawHTML: '<span style="color:red"> 빨간 글씨</span>'
        }
      })
    </script>
    
  ```

- 07_basic_of_syntax.html_2 참고

- v-for 실습

  - index 는 `(item, index) in myArr2`
  - key 는 `(value, key) in myArr3`
  - 특수 속성 key
    - v-for 사용 시 반드시 key 속성을 각 요소에 작성
    - 주로 v-for directive 작성 시 사용
    - 순회하는 요소들의 순서를 확실히 정할 식별값이 필요x
    - `v-for="(value, key) in myObj"  :key="key"`



- 08_
- v-on 실습
- 09_
- v-model 실습



# Vue advanced

computed

- Vue 인스턴스가 가진 옵션 중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
- 계산 값이 변하기 전까지 (인자가 변하기 전까지) 함수를 재호출하는 것이 아닌, 계산된 값 반환
- 10_computed.html 에서 methods와의 차이 확인
- 메서드와 달리 계산된 결과이기에, 사용 시 뒤에 () 안붙임
- methods 와 computed 의 차이
  - methods : 호출될 때마다 함수 실행, 같은 결과여도 매번 새롭게 계산
  - computed : 종속 대상의 변화에 따라 계산 여부가 결정됨
  - 종속 대상이 변하지 않으면 항상 저장(캐싱)된 값을 반환



watch

- 11_computed.html 
- 특정 데이터의 변화를 감지하는 기능
  1. watch 객체 정의
  2. 감시할 대상 data 지정
  3. data가 변할 시 실행 할 함수를 정의
  4. 인자 2개 받음
     - 첫 번째 인자는 현재값
     - 두 번째 인자는 과거값
- 디버깅 용도로 자주 쓰임
- watch로 메서드 실행 시, `handler`를 사용해야함 (`handler: '{함수 이름}'`)
- 계산 후에는 computed 객체 자체에 결과값을 저장. 만약 인자가 그대로인 경우, 메서드가 다시 호출됐을 때 다시 연산하지 않고 결과만 그대로 출력



filter

- 12_filters.html

- ```html
    <div id="app">
      <p>{{ numbers | getOddNums | getUnderTenNums }}</p>
    </div>
    
    <script>
    	filters: {
          getOddNums: function (nums) {
            const oddNums = nums.filter((num) => {
              return num % 2
            })
            return oddNums
          },
          
          // getUnderTenNums: function (nums) {
          //   const underTen = nums.filter((num) => {
          //     return num < 10
          //   })
          //   return underTen
          // }
        }
    </script>
  ```

- `numbers | getOddNums` 로 할 경우, 아래 filters 함수의 nums 인자가 `numbers` 리스트를 뜻함

- filter는 체인이 가능하다.
