브라우저에서의 js :

- 웹 페이지에서 복잡한 기능을 구현하는 스크립트 언어
- 주기적으로 갱신되거나, 사용자와의 상호 작용, 애니매이션 적용 등



## DOM

Browser APIs

- 웹 브라우저에 내장된 API
- 여러 유용하고 복잡한 일 수행
- 종류 : DOM, Geolocation API, WebGL



DOM

- 문서 객체 모델 (Document Object Model)
- 문서의 구조화된 표현을 제공하며, **프로그래밍 언어(js) 가 DOM 구조에 접근할 수 있는 방법**을 제공
  - HTML 문서를 구조화하여 각 요소를 객체로 취급
  - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등
- 
- DOM 은 문서를 논리 트리로 표현
- DOM 메서드를 사용하면 트리에 접근할 수 있고, 이를 통해 문서 변경 가능

- DOM의 주요 객체들을 활용하여 문서를 조작



DOM 주요 객체

- window object
  - DOM을 표현하는 창
  - 가장 최상의 객체 (작성 시 생략 가능),  (웹 페이지 전체를 의미)
  - 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄
  - 메서드 (크롬 개발자 도구의 콘솔에서 사용 가능)
    - window.open() 			새 탭 열기
    - window.print()             프린터창 열기
    - window.alert()              인쇄 대화 상자 표시
- document object
  - 브라우저가 불러온 웹 페이지
  - 페이지 컨텐츠의 시작점
  - window 객체의 하위 컨텐츠 (window.document 로 사용하는 게 정확하지만, window는 생략 가능)
  - 메서드
    - document.title() = '싸피' 		현재 탭의 이름 변경

파싱

- 구문 분석, 해석
- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
- 조작 순서
  1. 선택



선택 관련 메서드

- 선택
  - document.querySelector(selector)
    - 객체 하나 찾기 (selector에 만족하는 첫 번째 객체 반환)
  - document.querySelectorAll(selector)
    - 여러 element 선택
- 조작
  - NodeList
    - 인덱스로만 각 항목에 접근 가능
    - forEach 메서드 및 다양한 배열 메서드 사용 가능
    - querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음
  - document.createElement()
    - 작성한 tagName의 HTML 요소를 생산하여 반환
  - Model.innerText
    - Node 객체와 그 자손의 텍스트 컨텐츠를 표현
    - 사람이 읽을 수 있는 요소만 남김
  - Mode.appendChild()
    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    - 한번에 하나의 Node만 추가할 수 있음
    - html 의 body에 넣고 싶은 경우 `document.body.appendChild(aTag)` 같은 식으로
  - Mode.removeChild()
    - DOM에서 자식 Node 제거
    - 제거된 Node 반환
- 속성에 관한 메서드
  - Element.getAttribute(attributeName)
    - 해당 요소의 지정된 값(문자열) 반환
    - 인자는 값을 얻고자 하는 속성의 이름
  - Element.setAttribute(name, value)
    - 지정된 요소의 값을 설정
    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성 추가



- 이를 활용해 js로 html 처리

  - 태그 생성 후 글 쓰기

  - ```html
    document.createElement('h1')
    const h1Tag = document.createElement('h1')
    h1Tag.innerText = 'DOM 조작
    ```

  - 기존 태그에 글 쓰기, 삭제

  - ```html
    divTag = document.querySelector('div')
    divTag.appendChild(h1Tag)
    divTag.removeChild(h1Tag)
    ```

  - a 태그에 글 쓰기

  - ```html
    const aTag = document.createElement('a')
    aTag.setAttribute('href', 'https://google.com')
    aTag.innerText='구글'
    const divTag = document.querySelector('div')
    divTag.appendChild(aTag)
    ```

  - 새로운 속성 추가

  - ```html
    h1Tag.classList
    h1Tag.classList.toggle('blue')
    
    ```

    add, remove 도 사용 가능

  - 



## Event

Event 란 프로그래밍하고 있는 시스템에서 일어나는 사건 (클릭 or 마우스 오버 등)

우리가 원한다면 그것들에 어떠한 방식으로 응답할 수 있도록 시스템이 말해주는 것

종류 : 키보드 키 입력, 브라우저 닫기, 텍스트 복사 등...



Event object

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 순서
  1. DOM 요소는 Event를 받고 (수신)
  2. 받은 Event를 (처리)
     - Event 처리는 주로 addEventListener() 라는 이벤트 처리기를 다양한 html 요소에 부착해서 처리함
     - EventTarget.addEventListener(type, listener)
- 메서드
  - EventTarget.addEventListener(type, listener[, options])
    - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
    - 이벤트를 지원하는 모든 객체를 대상으로 지정 가능
    - type : input, click, submit, ... (모질라 docs/Web/Events 에서 확인 가능)
    - listener : 지정된 이벤트를 수신할 객체 (js function 객체, 콜백 함수임, Event 기반 객체를 유일한 매개변수로 받음)



#### event 폴더의 실습 연습

버튼을 누르면 페이지 변환 없이 숫자가 1씩 증가하는 웹 화면 구현 (01_button)

```html
  <button id="btn">버튼</button>
  <p id="counter">0</p>
  
  <script>
    // 버튼을 누를 때마다 숫자가 1씩 증가
    const btn = document.querySelector('#btn')    // 버튼 클래스를 누르면
    let countNum = 0

    // 이벤트 핸들러 작성
        // 버튼이 클릭 될 때마다 function 을 실행
    btn.addEventListener('click', function (event) {
      const pTag = document.querySelector('#counter')
      countNum += 1
      pTag.innerText = countNum
    })
  </script>
```

input 에 입력된 값을 그대로 출력 (02_input)

```html
  <input type="text" id="text-input">
  <p></p>
  <script>
    // input 에 입력된 값을 실시간으로 출력

    // 1. input 선택
    const inputTag = document.querySelector('#text-input')

    // 2. 이벤트 핸들러 부착
    inputTag.addEventListener('input', function (event) {
      // console.log(event)
      // console.log(event.target)
      // console.log(event.target.value)

      const pTag = document.querySelector('p')
      pTag.innerText = event.target.value
    })
```

input 입력 값을 실시간으로 출력하고, 버튼을 클릭하면 출력된 값의 클래스를 토글하기 (03_button_input)

```html
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text">

  <script>
    const btn = document.querySelector('#btn')
    btn.addEventListener('click', function (event) {
      const h1Tag = document.querySelector('h1')
      h1Tag.classList.toggle('blue')
    })

    const inputTag = document.querySelector('input')
    inputTag.addEventListener('input', function (event) {
      const h1Tag = document.querySelector('h1')
      h1Tag.innerText = event.target.value
    })
   
  </script>
```



## Event 취소

- event.preventDefault()
  - 현재 Event의 기본 동작을 중단
  - HTML 요소의 기본 동작을 작동하지 않게 막음
  - HTML 요소의 기본 동작 예시 : a 태그 (클릭 시 특정 주소로 이동), form 태그 (form 데이터 전송)

복사를 막고 경고창을 띄우기 (04_prevent)

```html
  <div>
    <h1>정말 중요한 내용</h1>
  </div>
  
  <script>
    // 복사가 불가능하도록, 복사 시도 시 경고창 띄우기
    const h1Tag = document.querySelector('h1')
    h1Tag.addEventListener('copy', function (event) {
      // 복사 이벤트를 막음
      event.preventDefault()
      alert('복사 할 수 없습니다!!!')
    })
  </script>
```



### 종합 실습

05_lotto.html

버튼을 클릭하면 랜덤 로또 번호 6개 출력

```html
  <h1>로또 추천 번호</h1>
  <button id="lotto-btn">행운 번호 받기</button>
  <div id="result"></div>

  <!-- js의 라이브러리 -->
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    const btn = document.querySelector('#lotto-btn')
    btn.addEventListener('click', function (event) {
      
      // 공이 들어갈 컨테이너 생성
      const ballContainer = document.createElement('div')
      ballContainer.classList.add('ball-container')

      // 랜덤한 숫자 6개 만들기
      const numbers = _.sampleSize(_.range(1, 46), 6)
      console.log(numbers)

      // 공 만들기
      numbers.forEach((number) => {
        const ball = document.createElement('div')
        ball.innerText = number
        ball.classList.add('ball')
        ball.style.backgroundColor = 'crimson'
        ballContainer.appendChild(ball)
      });

      // 공 컨테이너는 결과 영역의 자식으로 넣기
      const resultDiv = document.querySelector('#result')
      resultDiv.appendChild(ballContainer)
      
    })
```



06_todo (form 태그를 사용한 Create, Read 기능을 충족하는 todo app 만들기)

(form 제출을 막아야함. 안막으면 form 데이터 전송 뒤 새로고침)

```html
  <form action="#">
    <input type="text" class="inputData">
    <input type="submit" value="Add">
  </form>
  <ul></ul>

  <script>
    const formTag = document.querySelector('form')

    formTag.addEventListener('submit', function (event) {
      // form 태그 제출을 막음
      event.preventDefault()

      const inputTag = document.querySelector('.inputData')
      const data = inputTag.value

      // 데이터에 공백이 아닌 값이 있으면
      if (data.trim()) {   
        const liTag = document.createElement('li')
        liTag.innerText = data
        
        const ulTag = document.querySelector('ul')
        ulTag.appendChild(liTag)

        event.target.reset()
      }
      // 공백만 있으면 
      else {
        alert('내용을 입력하세요!')
      }  
    })
  </script>
```



### lodash

모듈성, 성능 및 추가 기능을 제공하는 js 라이브러리

array, object 등 자료구조를 다룰 때 사용하는 함수들을 제공 (reverse, sortBy, range, random, ...)



## this

- 어떤 object를 가리키는 키워드 (함수 호출될 때 this를 암묵적으로 전달받음)
- js의 this 는 일반적인 프로그래밍 언어의 this와 다르게 동작
- js는 해당 함수 호출 방식에 따라 this가 가리키는 객체가 달라짐 (동적으로 결정)



1. 전역 문맥에서의 this

   항상 window를 의미

2. 함수 문맥에서의 this

   - 단순 호출

     - 전역 객체를 가리킴 (브라우저에서는 window, Node.js에서는 global)

   - Method 호출

     - 객체의 메서드이므로, 해당 객체(본인을 호출하는 객체)가 바인딩
     - 이럴 경우 해당 객체의 다른 변수들 사용이 가능하다.

   - Nested (콜백 함수)

     - 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴

     - 메서드에 의한 호출이 아니라 콜백 함수에서의 단순 호출 (this 가 미리 정해져있지 않기 때문에)

     - 이를 해결하기 위해 화살표 함수 사용 

       - (화살표 함수에서 this를 사용하면 본인을 호출하는 객체가 바인딩)
       - 자동으로 한 단계 상위의 scope의 context를 바인딩

     - but, addEventListener 에서의 콜백 함수는 function 키워드의 경우 addEventListener를 호출한 대상 (event.target)을 뜻함.

       반면 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩 됨

       결론 : addEventListener 의 콜백 함수는 function 키워드를 사용하기
