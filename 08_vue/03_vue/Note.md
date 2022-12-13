vue 확장자를 사용하는 파일을 단독으로 사용하는 법 배우기

# Vue CLI



### Node.js

- JS는 브라우저를 조작하는 유일한 언어 (브라우저 엔진을 사용)
- but, 브라우저 밖에서는 구동 x
- 브라우저 밖에서도 구동하기 위해, Node.js가 나타남

### NPM

- Node Package Manager
- Node.js의 기본 패키지 관리자 (python의 pip와 같은 역할)
- 기본적으로 같이 설치됨



## Vue CLI

- vue 개발을 위한 표준 도구
- 프로젝트 구성을 도와주는 역할



실습

- 설치
  - `npm install -g @vue/cli`
- 프로젝트 생성 (vscode 터미널에서 진행)
  - `vue create vue-cli`



구조

- node_modules

  - 파이썬의 가상환경 venv 역할도 함. 각 패키지간의 의존성이 매우 높음. 용량도 큼 (100mb 넘음)

- node_modules - Babel

  - JS의 컴파일러 역할

  - ES6+ 코드를 구버전으로 변역해주는 도구 (Js의 다양한 스펙트럼에 대해 적용 가능)

- node_modules-Webpckk

  - static modult bundle 
  - 모듈 간의 의존성 문제를 해결하기 위한 도구
  - 필요한 모든 모듈 매핑, 내부적으로 종속성 그래프를 빌드
  - 모듈이란?
    - app 크기가 커지면 파일 하나에 모든 기능을 담기 어려워짐
    - 결국 파일들을 분리하여 관리하게 되었고, 각 파일을 모듈이라 부름
    - 어려 모듈 시스템 : ESM, AMD, CommonJS, UMD
    - 모듈 의존성 문제
      - 모듈 수가 많아지고 의존성이 깊어지면서, 문제 발생 시 어느 모듈에서 문제가 발생했는지 모름
      - => Webpack 등장 (의존성 문제를 해결해주는 도구 Bundler 중 하나)
      - Node.js 개발자도 이를 해결하기 위해 별도의 Deno라는 용어를 만듬 

- package-lock.json

  - python의 requirements.txt 역할
  - node_modules 에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
  - 목록에 있는 라이브러리들은 알아서 업데이트됨 (별도 업데이트 x)

- public/index.html

  - vue 앱의 뼈대가 되는 html (SPA 방식에서 처음 받는 html 페이지)
  - vue 앱과 연결될 요소 있음 (body 태그 안의 div 안에 연결된 데이터 표시)

- src/

  - src/assets
    - 정적 파일을 저장하는 디렉토리
  - src/components
    - 하위 컴포넌트들
  - src/App.vue
    - 최상위 컴포넌트 (index.html과 연결)
  - src/main.js
    - webpack이 빌드를 시작할 때 제일 먼저 부르는 파일



주의

- TIL 폴더 안에 vue 실습 프로젝트를 만든 경우, vue 폴더 안에서 만들어지는 .git 파일을 삭제해야 올바르게 push pull 가능

# SFC

## component

- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
- 하나의 app 구성 시에는 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적
- 유지보수, 재사용성에 좋음, 캡슐화 등등 

vue의 컴포넌트란? 

- 이름이 있는 재사용 가능한 Vue 인스턴스 (`new Vue()`로 만든 것)

### SFC

- Single File Component
- 하나의 `.vue` 파일이 하나의 vue instance이고, 하나의 컴포넌트 (SFC)이다.
- 이 vue 인스턴스를 하나의 기능 단위로 작성하는 것이 권장됨

## Vue component

- 템플릿 (HTML)
  - HTML의 body 부분
- 스크립트 (JS)
  - JS 코드가 작성됨
  - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 코드가 작성됨
- 스타일 (CSS)
  - 컴포넌트의 스타일을 작성

구조

- 컴포넌트들이 tree 구조를 만들어 하나의 페이지 구성
- root 에 해당하는 최상단 컴포넌트가 App.vue
- 이 App.vue를 index.html과 연결
- 이 index.html 하나만을 렌더링 (SPA)



### 실습

- 현재 구조
  - Vue CLI 실행 시 HelloWorld.vue 컴포넌트가 생성되고, index.html에 표현되어있음
- 하위 컴포넌트 (MyComponent.vue) 생성
  1. src/components/ 안에 생성 
     - 주의. templates 안에는 반드시 하나의 요소만 추가 (0개, 2개 이상 안됨. 아무 태그나 템플릿 안에 넣기)
  2. script에 이름 등록
  3. template에 요소 추가
- 하위 컴포넌트 등록
  1. 불러오기 (app.view에서 불러오기 선언)
     - `import {instance name} from {위치}`
  2. 등록하기 
     - `export default` 안에 컴포넌트 명 넣기
  3. 보여주기
     - 템플릿에 작성



# Pass Props & Emit Events

하위 컴포넌트와 상위 컴포넌트 사이의 데이터 교환은 어떻게 되나? 우리는 동적 웹페이지를 만들고 싶고, 한 페이지 내에서 데이터를 공유해야하는데...

필요한 컴포넌트들끼리 데이터를 주고받으면 안되나? 그러면 데이터의 흐름을 파악하기 힘듦, 교환하는 컴포넌트 쌍이 너무 많아짐, 유지보수가 힘들어짐

컴포넌트는 부모-자식 관계를 가지고 있으니, 부모-자식 관계만 데이터를 주고받게 하자! 

- pass props
  - 부모 => 자식 뱡향으로의 데이터 흐름	
- emit event
  - 자식 => 부모 방향으로의 데이터 흐름



## pass props

- 요소의 속성을 사용하여 데이터 전달 (`<HelloWorld msg='welcome ~'>` 에서 하위 컴포넌트인 HelloWorld 는 자신의 msg 속성을 template에서 `{{ msg }}` 형태로 사용)
- props는 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식 컴포넌트는 props 옵션을 사용하여 데이터를 받은 props를 명시해 줘야 함
- 요소에 속성을 작성하듯이 사용 가능하여, `prop-data-name="value"` 형태로 데이터를 전달
  - 이 때 속성의 키 값은 kebab-case 사용 (html에서의 속성은 대소문자를 구분하지 못하니)
- prop 명시
  - 데이터를 받는 하위 컴포넌트에서도 props를 type과 함께 정리



정리

- 부모에서 넘겨주는 props
  - kebab-case (HTML 속성명은 대소문자 구분 x)
- 자식에서 받는 props
  - camelCase



Dynamic props

- 변수를 props로 전달할 수 있음
  - v-bind 사용. `static-props` 앞에 `:` 붙여줌으로써 데이터를 동적으로 바인딩
- 컴포넌트의 data 함수
  - 각 vue 인스턴스는 같은 data 객체를 공유하므로, 새로운 data 객체를 반환하여 사용해야 함
  - 부모 컴포넌트에서의 `:dynamic-props="dynamicProps"`는 앞의 key값이란 이름으로 뒤의 " " 안에 오는 데이터를 전달하겠다는 뜻. 즉, 앞의 key 값과 자식 컴포넌트의 props 안의 값이 일치해야 한다.
  - 숫자를 전달 시 v-model 처럼 `:num="1"` 방식으로 전달
- 단방향 데이터 흐름
  - 모든 props는 부모에서 자식으로만 갈 수 있음 (단방향 바인딩)
  - 부모 속성이 업데이트되면 자식으로 흐르지만, 반대 방향은 아님
    - 하위 컴포넌트가 실수로 상위 컴포넌트를 변경하면 데이터 흐름이 매우 복잡해짐
    - 하위 컴포넌트에서 prop 변경을 시도하면 vue가 경고를 출력함
  - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침



그럼 하위에서 어떻게 올리나? => emit event



## emit event

자식 컴포넌트에서 부모 컴포넌트로 데이터 전달 시 이벤트를 발생시켜 데이터를 전달

방법

1. 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
2. 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음



### $emit

- 자식

  - 메서드 설정

    ```vue
      methods: {
        childToParent: function () {
          this.$emit('show-me-the-money', '나는 자식이 보낸 데이터이다')
        }
      },
    ```

    show-me-the-money 는 제목, 뒷부분은 같이 포함된 데이터

- 부모

  - 위의 자식 컴포넌트 선언

    ```vue
        <MyComponentItem 
        @show-me-the-money="parentGetEvent"
        />
    ```

    show-me-the-money 라는 외침이 발생되면, 메서드 parentGetEvent라는 메서드를 실행한다.

  - 아래의 methods

    ```vue
      methods: {
        parentGetEvent: function (childData) {
          console.log('용돈 없어!!')
          console.log(childData)
        }
      }
    ```



- `emit('event-name')` 형식으로 사용하며, 부모 컴포넌트에 `event-name`이라는 이벤트가 발생했음을 알림
- 직접 데이터를 받을 수는 없으니, 아래쪽에서 emit 이벤트가 발생한 경우 같이 전송된 emit 이벤트의 인자를 데이터로 받아 사용하는 메서드를 실행



emit with data 흐름 정리

1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수 ChildToParent 호출
2. 호출된 $emit을 통해 부모 컴포넌트에 이벤트 child-input 를 발생. 이벤트에 v-model로 바인딩 된 입력받으 ㄴ데이터를 전달
3. 상위 컴포넌트는 자식 컴포넌트의 이벤트 child-input을 청취하여 연결된 핸들러 함수 getDynamicData 호출, 함수의 인잘 전달된 데이터가 포함되어 있음
4. 호출된 함수 실행  



언제 kebab-case고 언제 camelCase냐?

- HTML 요소에서 사용 : kebeb-case
- JS에서 사용 : camelCase

- props
  - 상위 => 하위 에서는 HTML 요소로 내려줌 : kebab-case
  - 하위에서 받을 때 JS에서 받음 : camelCase
- emit
  - emit 이벤트 발생시키면 HTML 요소가 이벤트를 청취함 (이벤트는 받는 쪽이 중요) : kebab-case
  - 메서드, 변수명 등은 JS에서 사용 : camelCase



