# Django

---

## Intro

로그인, 로그아웃, 회원관리, 데이터베이스, 서버, 클라이언트, 보안 기능 등을 갖춘 강력한 프레임워크 (라이브러리와는 다름. bootstrap 같은 것이 프레임워크)

로그인, 로그아웃 등 회원관리에 굉장히 유용 (bootstrap의 외관 + Django의 기능)

#### 배워야 하는 이유

- python으로 작성된 프레임워크
- 수많은 기능들
- 검증된 웹 프레임워크

#### 클라이언트와 서버 구조

- 클라이언트의 request에 서버가 response

- 클라이언트
  - 웹 사용자의 인터넷에 연결된 장치
- 서버
  - 웹 페이지, 사이트 등을 저장하는 컴퓨터
  - 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시 (만들어둔 HTML 문서 등을 제공)

#### 웹 브라우저와 웹 페이지

- 웹 브라우저 

  - 웹 페이지를 찾아 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동하도록 하는 프로그램
  - 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는 렌더링 프로그램

- 종류

  - 정적 웹 페이지

    한 번 작성된 HTML 파일의 내용이 변하지 않고, 모든 사용자에게 동일한 모습으로 전달되는 것 (== 서버에 미리 저장된 HTML 파일 그대로 전달된 웹 페이지)

  - 동적 웹 페이지

    사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 전달되는 웹 페이지

---

## Django 구조

### 디자인 패턴

- 자주 사용되는 구조를 일반적인 구조화 해둔 것 (재사용성)
- 소프트웨어 디자인 패턴
  - 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책을 제시
  - 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙 (데이터를 주고받는 방식 등)
  - 디자인 패턴을 알고 통일하여, 효율성을 높임

### Django 디자인 패턴

- MTV 패턴 

  - MVC (Model-View-Controller) 디자인 패턴을 기반으로 조금 변형된 패턴

    - 목적 : 관심사 분리, 각 부분을 독립적으로 개발하여 효율성 및 유지 보수, 협업 등이 용이함
    - model : 데이터와 관련된 로직을 처리 (파이썬으로 할 예정)
    - view : 레이아웃과 화면을 처리
    - controller : 명령을 model과 view 부분으로 연결

  - view의 역할을 Template가 대체, MVC의 controller의 역할을 View가 대체

  - Model

    - MVC 패턴에서 model의 역할에 해당
    - 데이터와 관련된 로직을 관리
    - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
    - ORM : 파이썬과 SQL 사이의 번역기 역할 (SQL 몰라도 파이썬으로 데이터 관리 )

  - Template

    - MVC 패턴에서 view의 역할에 해당
    - 레이아웃과 화면을 처리
    - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의

  - View

    - MVC 패턴에서 controller의 역할에 해당
    - Model & Template과 관련한 로직을 처리해서 응답을 반환
    - 클라이언트의 요청에 대해 처리를 분기하는 역할

  - 요약 : 데이터가 필요하면 model에 접근해서 데이터를 가져오고, 가져온 데이터를 template로 보내 화면을 구성하고, 구성된 화면을 응답으로 만들어 클라이언트에게 반환

    URLs의 요청 => View => Model (데이터 가져옴) => View => Template (렌더링해서 HTML 문서 만듬) => View => 응답

## 시작하기

aritcles/views.py 에서 함수 만들 때는, 항상 request란 변수명 주기 (클래스 만들 때 self 주듯이)

폴더 만들면, settings.py => INSTALLED_APPS에 그 폴더 이름 추가

기억해야 할 것 

- urls.py : 경로 만들기, views로 이동

- views.py : view 함수 정의, 해당하는 html로 이동

- index.html : 웹 페이지를 꾸미는 코드

- **url 경로 하나 만들 때마다 view 함수 만들고, html 만들기**

  한꺼번에 하면 오류날 때 어디서 났는지 절대 모름

---

## Django Template

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입

#### Django Template Language (DTL)

- built-in template system, 파이썬처럼 생김

- 조건, 반복, 변수 치환, 필터 등의 기능을 제공

  python처럼 사용 가능, but 파이썬 코드로 실행되는 것은 아님

- 프로그래밍적 로직이 아니라, 프레젠테이션을 표현하기 위한 것 뿐

#### DTL Syntax

- variable
  - 변수명은 `{{variable}}` 식으로 중괄호 2개
  - dot(.) 사용해서 변수 속성에 접근 가능
  - render()의 세번째 인자로 {'key': value} 처럼 딕셔너리 형태로 넘겨줌, 여기서의 key가 template에서 사용 가능한 변수명이 됨
- filters
  - `{{variable|filter}}` 처럼 표시
  - ex) name을 전부 소문자로 : `{{name|lower}}` 형태로
- tags
  - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- comments
  - 주석

### template 상속

템플릿 상속을 활용해서, 보다 쉽게 모든 html에 bootstrap을 적용 가능 + 나만의 속성도 손쉽게 적용 가능

상위 폴더의 base.html을 상속하길 원할 때 : settings.py 에 가서 TEMPLATES 리스트의 DIRS에 'BASE_DIR / templates' 입력 (templates는 base.html을 저장한 상위 폴더), (BASE_DIR은 장고가 저장된 가장 최상단의 폴더로, 장고 설치? 시 자동으로 저런 변수명에 저장됨)

---

## Sending and Retrieving form data

데이터를 보내고 가져오기 (form 태그 사용)

## Django URLs

Trailing Slashes

- Django의 URL 끝에 / (trailing slash) 를 넣어서 표시
- 정규 URL을 명시한 후, trailing slash가 없는 요청에 대해 자동으로 slash를 추가하여 통합된 하나의 콘텐츠로 볼 수 있도록 한다.

Variable routing

- 탬플릿의 많은 부분이 중복되고, 일부분만 변경되는 상황에서 비슷한 URL과 템플릿을 계속 만들 필요는 없다.

- URL 주소를 변수로 사용하는 것을 의미

- 변수 값에 따라 하나의 path()에 여러 페이지를 연결시킬 수 있음

  ex) `path('<str:name>/', views.profile),`

---

## 기타

하다보면 urls.py의 path에서 url 일부를 바꿔야 할 수 있다. 그 때는 path에 name 인자를 추가해서, url을 마음대로 바꾸되 이미 연결된 html에서는 여전히 연결되도록 할 수 있다.
