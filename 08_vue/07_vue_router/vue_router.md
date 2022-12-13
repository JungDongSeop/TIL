# UX & UI



UX

- User Experience
- 데이터를 기반으로 유저를 조사 분석
- 단순하고 대중화되어야 함

UI

- User Interface
- 유저에게 보여주는 화면을 디자인
- UX를 고려한 디자인 반영
  - 심미적인 부분만 고려하기보단, 편의성까지 고려
- 통일된 디자인을 위한 디자인 시스템, 프로토타입을 통한 소통 등이 필요
- UI 디자인에 있어 가장 중요한 것은 협업



Can't Unsee

- 더 나은 UI, UX를 고르는 게임 사이트



Prototyping

- Figma 라는 프로토타입 설계 툴을 자주사용
  - 협업에 중점을 두면서 UI/UX 설계에 초점
  - 장점
    - 웹 기반 시스템 (가벼운 환경에서 실행 가능, 작업 내역 웹에 저장됨)
    - 실시간을 팀원들이 협업 가능
    - 다양한 플러그인 존재 (vscode 확장 등)
    - 성능의 희생을 일부 감수하고, 웹 기반의 협업이 이루어지도록 함



# Vue Router



Routing

- 네트워크에서 경로를 선택하는 프로세스
- 웹 서버에서는, 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것



Routing in SPA / CSR

- 서버는 하나의 HTML (index.html) 만을 제공 (single page)
- 이후 동장은 JS 코드를 활용, 데이터가 필요하면 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터 처리
- 즉, 하나의 URL만 가질 수 있음
- but, 사용자의 관점에선 페이지가 바뀌었는데, url이 그대로다? => UX 감소
  - 새로고침 시 처음 페이지로 돌아감
  - 링크 공유 시 처음 페이지만 공유 가능
  - 브라우저의 뒤로 가기 기능 사용 불가능
- 이를 위해서, Vue Router를 사용



Vue Router

- Vue의 공식 라우터
- 라우트에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링할지 알려줌
  - SPA를 MAP처럼 URL을 이동하면서 사용 가능
  - SPA의 단점인 'URL이 변경되지 않는다'를 해결
- 사용
  - 프로젝트 생성 후 `vue add router` 입력



History mode

- 브라우저의 History API를 활용한 방식
  - 새로고침 없이 URL 이동 기록을 남길 수 있음 (뒤로 가기 가능)
  - 익숙한 URL 구조로 사용 가능 (index/articles/...) 처럼 `/`로 구분 가능
  - History 사용하지 않으면 디폴트인 `#`으로 구분됨

Vue Router

- router-link

  - a 태그와 비슷한 기능 (URL을 이동시킴)
    - routes에 등록된 컴포넌트와 매핑됨
    - 클릭 이벤트를 차단하여, a태그와 달리 페이지를 다시 로드하지 않음

  - 목표 경로는 'to' 속성으로 지정됨

- router-view

  - 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트
  - 실제 component가 DOM에 부착되어 보이는 자리를 의미
  - router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
    - django에서의 block tag와 비슷
      - App.vue 는 base.html 역할
      - router-view 는 block 역할

- src/views

  - router-view에 들어갈 component 작성
  - 기존 컴포넌트를 작성하던 곳은 components 폴더였지만, 이젠 역할에 따라 두 폴더로 나뉨
  - 아래 배치를 권장
    - views/
      - routes에 매핑되는 컴포넌트
      - 다른 컴포넌트 내부의 AboutView & HomeView 컴포넌트
    - components/
      - routes에 매핑되지 않은 컴포넌트를 모아두는 폴더
      - routes에 매핑된 컴포넌트의 하위 컴포넌트 등

- 실습

  - 주소를 이동하는 방법
    1. 선언적 방식 네비게이션
       - router-link의 `to` 속성으로 주소 전달
       - `<router-link :to="{name="{변수명}"}">` 처럼 사용
    2. 프로그래밍 방식 네비게이션
       - Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근할 수 있음
       - 다른 URL로 이동하려면 `this.$router.push` 사용
         - history stack에 기록이 남기 때문에, 브라우저의 뒤로 가기 버튼 사용 가능
       - 결국, router-link 와 $router 의 동작 원리는 같음
  - 동적 인자 전달
    - Dynamic Route Matching
    - URL의 특정 값을 변수처럼 사용 (django의 variable routing)
    - `$route.params`로 접근 가능
  - route에 컴포넌트를 등록하는 또다른 방법
    - lazy-loading
      - 모든 파일을 한번에 로드하려면 초기 시간이 매우 오래 걸림
      - 미리 로드하지 않고, 특정 라우트에 접근할 때 로딩을 시작 (지연 로딩)





# Navigation Guard



vue router를 통해 특정 URL에 접근할 때, 1. 다른 url로 redirect를 하거나 2. 해당 URL로의 접근을 막는 방법 (권한 없는 유저 차단 등)

종류

- 전역 가드
  - Grobal Before Guard
  - 애플리케이션 전역에서 동작
  - 다른 url 주소로 이동할 때 항상 실행
  - `router/index.js`에 `router.beforeEach()`를 사용하여 설정
  - 콜백 함수의 인자
    - to
    - from
    - next
      - 지정한 URL로 이동하기 위해  호출하는 함수. 콜백 함수 내에서 반드시 한 번만 호출되어야 함
      - to에 해당하는 URL로 이동.
      - next()가 호출되지 않으면 화면이 전환되지 않음
- 라우터 가드
  - 라우터 가드
  - 로그인 여부에 따른 처리 등
  - beforeEnter()
    - route에 진입했을 때 실행됨
    - 라우터를 등록한 위치에 추가
- 컴포넌트 가드
  - 라우터 컴포넌트 안에 정의
  - hello, jin 이 되도록 입력한 뒤, Hello 하이퍼링크를 누르면 url은 바뀌지만 화면은 바뀌지 않음
    - 컴포넌트가 재사용되었기 때문에
  - `beforeRouteUpdate()`를 사용해서 처리
    - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행
    - userName을 이동할 params에 있는 userName으로 재할당



404 Not Found

- 사용자가 요청한 리소스가 존재하지 않을 때 응답

- 직접 만들어보기

- 형식이 맞지 않는 경우

  - index.js 에서 routes 맨 밑에

  - ```js
      {
        path: '*',
        redirect: '/404',
      }
    ```

    

- 형식은 맞지만 해당 리소스를 찾을 수 없는 경우



# Articles App with Vue



`article?.title`

- Optional Chaining
-  article이 undefined나 null이면 에러가 발생하지 않고 undefined를 반환

