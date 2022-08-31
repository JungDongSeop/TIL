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



---

---

# Namespace

## url namespace

`폴더1/urls`의 path 함수 내 이름과 `폴더2/urls`의 path함수 내 이름이 같으면, namespace의 접근에 따라 폴더2의 urls에 접근이 불가능할 수 있음.

이 때 urls의 리스트 위에 `app_name = 'articles'`처럼 앱 네임을 추가하면, 이후 extend 쓸 때 `{% url 'articles:index' %}` 처럼 해서 구분 가능



## template namespace

요청 보내는 건 url namespace로 구분 완료. 그런데 정보를 받을 때 자꾸 articles/template/index로만 간다..?

- articles/template/...
- pages/template/...

django는 어디에 있든 template 폴더 뒤를 찾기 때문에, seetings.py의 INSTALLED_APPS 순서에 따라서 위에 있는 articles/template만 계속 접근함

이를 막기 위해서는, 

- articles/template/aaa/index.html
- pages/template/bbb/index.html

이런 식으로 주소 구분이 가능하게 해줘야함. 이후 가져올 때는 aaa/index.html, bbb/index.html 으로 구분



# Model

(model.py에서 class로 설계도(테이블) 기초 작성 => makemigrations를 통해 설계도 청사진 제작(아직 DB에 테이블은 안만듦) =>)

정보를 저장하고 DB를 조작할 때 사용

(게시판에 글 제목과 작성자를 올릴 때 등)

### DB 간략 설명

- 체계화된 데이터의 모임
- 구조
  - 스키마 : 뼈대, DB에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
  - 테이블 : 관계라고도 부름, 필드(속성, 컬럼) + 레코드(튜플, 행) 으로 구성
- PK : 기본 키, 각 레코드의 고유값 (식별자로 사용)
- 쿼리 : 데이터를 조회하기 위한 명령어를 일컬음, '쿼리를 날린다' : DB를 조작, 수정한다

##### 다시 model 설명

## model 작성하기

- 새 프로젝트 crud, 앱 articles 작성 및 앱 등록

  `django-admin startproject crud .`

  `python manage.py startapp articles`

- models.py 작성

  - 모델 클래스 작성은 DB 테이블의 스키마를 정의하는 것

    모델 클래스 == 테이블 스키마

  - 자동으로 import되는 `from django.db import models`에서의 Model 클래스를 상속받아 사용

    클래스 상속 기반 형태의 Django 프레임워크 개발

    ```python
    class My_board(models.Model):
        title = models.CharFiels(max_length=10)
        content = models.TextField()
    ```

    1. 클래스 변수(title, content) : DB 필드의 이름
    2. 클래스 변수 값 : DB 필드의 데이터 타입
       - `DataField()` 
       - `CharField()` : 길이 제한 있는 문자열 넣을 때
       - `TextField()` : 글자 수가 많을 때 사용
       - `IntegerField()` 

  - 개인키 (PK)는 django가 자동으로 만들어줌

---

## Migrations

스키마 정보가 저장됨, 파이썬으로 작성된 설계도 (알아서 개인키를 넣는다던가, 내가 만든 필드르를 저장한다던가)

model 클래스로 만든 기초 골조를 테이블 청사진으로 만들기 위해, makemigrations 사용

- migration 만들 때

  `python manage.py makemigrations`

- 만든 설계도를 실제 db.sqlite3 DB 파일에 반영하는 과정 (model과 DB의 동기화)

  `python manage.py migrate`

- 기타 명령어

  - `python manage.py showmigrations` 			(migrate됐는지 확인)

  - `python manage.py sqlmigrate articles 0001`  (해당 migrations 파일이 SQL문으로 어떻게 해석 될 지 미리 확인)


그런데, 설계도는 누가 어떻게 해석하지?? DB는 SQL만 알아듣는데? => ORM이 번역

## ORM

- object-relational-mapping

- 객체 지향 프로그래밍 언어와 DB를 연동할 때, 둘 사이의 호환되지 않는 데이터를 변환

- django는 내장 django ORM을 사용

- 뛰어난 생산성, 쉬운 DB 조작, but ORM만으로는 완전한 서비스 제공이 어려움

---

# 추가 필드 정의

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- 추가 모델 필드 작성 후, 다시 한번 makemigrations 진행

- 이 때 이미 데이터가 있는 상태에서 추가필드를 정의하면, 기존 데이터에 대한 추가필드 값이 존재하지 않으니 오류가 남 (무결성 원칙)
  - 이를 방지하기 위해 cmd창에서 해결방법 1번을 선택한 후, 지시에 따르면 디폴트 값 추가 완료 (아니면 대회창 나간 후, 코드에 직접 default값 선언)

- 반드시 기억해야 할 migration 3단계
  1. models.py에서 변경사항이 발생하면
  2. migrations 파일 생성 (makemigrations)
  3. DB 반영 (migrate)

- DateTimeGield()
  - python의 datetime.datetime 인스턴스로 표시되는 날짜ㅏ 및 시간을 값으로 상요하는 필드
  - 선택인자
    - auto_now_add
    - auto_now

---

# QuerySet API

​	사전 준비

- 외부 라이브러리 설치 및 설정
  - `pip install ipython`
  - `pip install django_extensions`
  - settings.py => installed_apps에 'django_extensions' 추가
  - `pip freeze > requirements.txt` (패키지 목록 업데이트)

- Shell
  - 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램
  - python shell
    - 파이썬 코드를 실행해주는 인터프리터, python 명령어를 실행하여 그 결과를 바로 제공
  - Django shell
    - ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용
    - `python manage.py shell_plus`를 입력해서 사용

### Database API

- Django가 기본적으로 ORM을 제공하여, DB 조작을 편하게 도움

- Model을 만들면 Django는 DB API (객체들을 만들고 읽고 수정하고 지움)

- 구문

  `Article.objects.all() ` (각각 Model class, Manager, Queryset API)

### objects manager

- Django 모델이 DB 쿼리 작업을 가능하게 하는 인터페이스
- DB를 python class로 조작할 수 있도록 여러 메서드를 제공하는 manager

### Query

- Db에 특정 데이터를 보여달라는 요청
- 이 때 python으로 작성한 코드가 ORM에 의해 SQL로 변환되어 DB에 전달, 그 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달
- QuerySet
  - DB에게 전달 받은 객체 목록(데이터 모음)
  - objects manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 ㅏ때 반환되는 객체
  - 단, DB가 단일 객체를 반환할 때는 QuerySet이 아닌 class의 인스턴스로 반환됨

## QuerySet API 사용

- CRUD

  - Create, Read, Update, Delete 를 묶어서 이르는 말

- CREATE

  - 2개의 view 함수 필요 (사용자의 입력을 받을 페이지를 렌더링하는 함수 + 입력한 데이터를 전송받아 DB에 저장하는 함수)

  - 데이터 객체를 만드는 3가지 방법

  - 첫번째

    - article = Article()

      클래스를 통한 인스턴스 생성

    - article.title

      클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당

      `article.title = 'first'` , `artticle.content = 'django!'`식으로 사용

    - article.save()

      인스턴스로 save 메서드 호출

    이후 Article.objects.all() 을 사용해서 확인 가능

  2. 두번째

     - 인스턴스 생성 시 초기 값을 함께 작성하여 생성

       `article = Article(title='second', content='django!')`

  3. 세번째

     - QuerySet API 중 create() 메서드 활용

       `Article.objects.create(title='third', content='django!')`

- READ

  - 데이터를 조회하기

  - QuerySet API method는 2가지로 분류

    - return new querysets 하는 메서드
    - do not return querysets 하는 메서드

  - all() : return 하는 메서드, 전체 데이터 조회

  - get() : 단일 데이터 조회, 객체를 찾을 수 없거나 둘 이상 찾으면 예외 발생

    ​			=> 고유성을 보장하는 조회(PK 등)에서 사용해야함

  - filter() : 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet 반환
  - Field lookups : 특정 레코드에 대한 조건을 설정하는 방법

- Update

  - 과정
    1. 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
    2. article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
    3. save() 인스터늣 메서드 호출

- Delete

  - 과정
    1. 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
    2. delete() 인스턴스 메서드 호출
  - 이 때 표준 파이썬 메서드인 str()을 정의하여, 각각의 object가 문자들을 반환하도록 할 수 있음

## CRUD with view functions

- 이전에 익힌 QuerySet API를 통해, view 함수에서 직접 CRUD 구현하기
