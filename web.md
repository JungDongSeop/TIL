## html

hypertext markup language, 웹 페이지를 구조화하기 위한 언어

속성 예시

```html
id : 문서 전체에서 유일한 고유 식별자
class : 공백으로 구분된 해당 요소의 클래스 목록
data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
style : inline 스타일
title : 요소에 대한 추가 정보 지정
tabindex : 요소의 탭 순서
```

시맨틱 태그 (의미론적 마크업을 위해 필요)

```html
header : 문서 전체나 섹션의 헤더
nav : 내비게이션
aside : 사이드 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
section : 문서의 일반적인 부분
article : 문서, 페이지 안에서 독립적으로 구분되는 영역
footer : 마지막 부
```

DOM 트리 (document object model)

    HTML 텍스트를 브라우저에서 렌더링 하기 위한 구조

태그    

```html
<a></a> : href 속성 사용, 하이퍼링크 생성, 본
  <a class="page-link" href="#">
<b></b> : 굵은 글씨
<i></i> : 기울임체
<br> : 텍스트 내 줄바꿈
<img> : src 속성 사용, 이미지 표현
<span></span> : 의미 없는 inline 컨테이너
<p></p> : 하나의 문단
<hr> : 문단 레벨 요소에서의 주제의 분리
<ol></ol> : 순서 있는 리스트
<ul></ul> : 순서 없는 리스트
<pre></pre> : html에 작성한 내용 그대로 표현
<blockquote></blockquote> : 텍스트가 긴 인용문, 들여쓰기한 것으로 표현
<div></div> : 의미 없는 block 레벨 컨테이너
```

그 외 태그

`<form>` : 데이터를 서버에 제출할 때 사용

                action, method, enctype 속성 (각자 서버 url, 사용할 HTTP 메서드, 데이터 유형)

`<input>` : 입력 데이터 유형, 로그인 화면 or 체크박스 등

                name, value, 기타 여러 속성 (form control에 적용되는 이름, 값)

`<label>` : input과 연동, <label> 부분 눌러도 input 활성화

                input에 id 속성, label에 for 속성 적어서 서로 연동

# CSS

스타일을 지정하기 위한 언어

선택자, 선언, 속성 값으로 구성

css 정의 방법 : 인라인, 내부참조(`<style>`), 외부 참조(외부 css 파일)

선택자

- 기본 선택자
  
  - 전체 선택자, 요소 선택자
  
  - 클래스 선택자, 아이디 선택자, 속성 선택자

- 결합자
  
  - 자손 결합자, 자식 결합자
  
  - 일반 형제 결합자, 인접 형제 결합자

- 의사 클래스/요소(Pseudo Class)
  
  - 링크, 동적 의사 클래스
  
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

```
요소 선택자 : html 태그 직접 선택
클래스 선택자 : .class
아이디 선택자 : #id
```

css 적용 우선순위

    `!important` => 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element

=> css 파일 로딩 순서

css 상속

부모 요소의 속성을 자식에게 상속

- 상속 가능 : text 관련 요소, opacity, visibility 등

- 상속 불가능 : box model 관련 요소(width, margin, box-sizing, ..), position 관련

자손 결합자 (A B) : A 하위의 모든 B

자식 결합자 (A>B) : A 바로 아래의 B

일반 형제 결합자 (A~B) : A 형제 요소 중 뒤에 있는 모든 B

인접 형제 결합자 (A+B) : A 형제 요소 중 바로 뒤에 있는 B

#### css 기본 스타일

크기 : px, %, em, rem, viewport(vw, vh, vmin, vmax)

색상 : 색상 키워드, RGB 색상, HSL 색상

텍스트 : 서체(font-family), 서테 스타일(font-style, font-weight), 자간(letter-spacing), 배경(background-image, background-color), 기타 등등

#### Box model

css 원칙 

1. 모든 요소는 box model이고, 위에서부터, 왼쪽에서부터 쌓인다.
   
   (세로는 block, 가로는 inline)

2. display에 따라 크기와 배치가 달라진다.

3. position으로 위치의 기준을 변경 (relative : 본인의 원래 위치, absolute : 특정 부모의 위치, fixed : 화면의 위치)

box 구성 요소

- margin : 바깥 여백, 색 지정 불가능

- border : 테두리 영역. 선, 점선 등으로 표시 가능

- padding : 테두리 안쪽의 내부 여백. 배경색, 이미지는 padding 까지 적용

- content : 글, 이미지 등 실제 내용

box-sizing : 기본적으로 모든 요소의 box-sizing은 content 부분

Display

- display: block (`div, ul, ol, p, hr, form 등`)
  
  - 줄바꿈이 일어남(세로), 화면 크기만큼의 가로 폭 차지

- display: inline (`span, a, img, input, b, em, i, strong 등`)
  
  - 행의 일부 요소(가로), content 너비만큼 가로 폭 차지
  
  - width, height, margin-top, margin-bottom 지정 x
  
  - 상하 여백은 line-height로 지정

- display: inline-block
  
  - inline처럼 한 줄에 표시 + block처럼 width, height, margin 등 사용 가능

- display: none
  
  - 해당 요소를 표시하지 않음, 공간조차 부여되지 않음
  
  - 공간은 차지하려면 visibility: hidden 사용

Position

- relative : 자기 자신의 static 위치를 기준으로 이동 (normal flow 따름)

- absolute : static 위치 제거 후 사용 (normal flow 벗어남, 공중에 뜬다 생각)

- fixed, sticky : 스크롤 해도 항상 같은 위치

Float

- 박스를 왼쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping하도록 함 (none, left, right)

- 요소가 normal flow를 벗어남

Flexbox (`display : flex or inline-flex` 로 사용)

- 행과 열 형태로 아이템들을 배치

- main axis, cross axis가 존재
  
  - 배치 설정 : flex-direction (row, column 등), flex-wrap (nowrap, wrap)
  
  - 공간 나누기 : justify-content, align-content
  
  - 정렬 : align-items(모든 아이템을 cross axis 기준으로, stretch, flex-start 등), align-self(개별 요소에 적용)
  
  - 기타 : flex-grow, order

- flex container(부모 요소), flex item(자식 요소)

## Bootstrap

CDN : content delivery network, 컨텐츠를 네트워크로 전달 제공하는 시스템

spacing

`{property}{sides}-{size}`, (예시 : `mx-auto`는 수평 중앙정렬)

- property
  
  - m, p

- sides
  
  - t, b, s (start), e (end), x (s+e), y (t+b), blank

color

`class="bg-primary"`, `class="text-success"`

text

`class="text-start"`, `class="fw-bold"`

display

`class="d-inline" "d-block" "box" 등등`

position

`class="box fixed-top"`

#### Bootstrap 컴포넌트

buttons

`<button type="button" class="btn btn-primary">`

dropdowns

forms

Navbar

Carosel

Modal

Flexbox

`<div class="d-flex">`

card > grid card

##### Grid system

12개의 칼럼 + 6개의 grid breakpoints

column : 실제 컨텐츠 부분

gutter : 칼럼 사이 공간

container : 칼럼들을 담는 공간

##### 연습

flexboxdefense.com

userinyerface.com

수요일 강의 마지막 실습 다시 한 번 보기

---

하이퍼링크 태그 `<a>`는 한줄로만 쓰기

bootstrap 덕지덕지 할 바에는 그냥 css로 깔끔하게 적기(class 하나로 표현)

상단 이동 버튼 : `<a href="#banner" class="pageup-btn"></a>`, css에 

`.pageup-btn{background: url(버튼 사진 위치); 등등 서식 적기}`

p, span 차이 : span은 inline 형태?
