## static/Media



### static files 관리

개발자가 서버에 미리 준비한 or 사용자가 업로드한 정적 파일을 클라이언트에게 제공하는 방법

- 정적 파일
  - 응답할 때 별도의 처리 없이 그대로 보여주는 파일
  - 파일 자체가 고정 (이미지, 자바 스크립트 등)
  - static file 이라 하고, `staticfiles` 앱을 통해 관련 기능제공
  - 이미 settings.py 에 기본으로 작성되어 있음
- Media file
  - 사용자가 웹에서 업로드하는 정적 파일
- load tag
  - 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드 (파이썬의 import 느낌)
  - `{% load static %}`
- static tag
  - STATIC_ROOT 에 저장된 정적 파일에 연결
  - `{% static '' %}`
- 코어 세팅
  - STATIC_ROOT
    - 기본값 None
    - django 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아 넣는 경로
    - 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로 (즉, 개발 단계에서는 중요성 적음)
    - 개발 과정에서 settings.py 의 DEBUG == True 면 적용 x (실제 배포에서는 False로 바꿈)
    - 클라이언트가 프로그램을 사용할 때, 장고 서버 경로로 정적 파일에 접근할 수는 없으니, 프로그램 및 애플리케이션을 설치해 제공하는 것
  - STATICFILES_DIRS
    - 기본값 [] (빈 리스트)
    - app/static/ 경로 외에 추가적인 정적 파일 경로 목록을 저장하는 리스트
  - STATIC_URL
    - 기본값 None
    - STATIC_ROOT 에 있는 정적 파일을 참조할 때 사용할 URL
    - 실제 파일이나 디렉토리가 아니며, URL로만 존재
    - 반드시 `/`로 끝나야 함
- 실습
  1. settings.py - INSTALLED_APPS 에 `django.contrib.staticfiles` 포함되어 있는지 확인
  2. settings.py에서 `STATIC_URL` 정의하기
  3. 앱의 static 폴더에 정적 파일 위치시키기
  4. 템플릿에서 static 템플릿 태그 사용, 지정된 경로에 있는 정적 파일의 URL 만들기

- 기본 경로에 있는 static file 가져오기
  - articles/static/articles 경로에 이미지 파일 배치
    1. articles 폴더에 static/articles 폴더 만들기
    2. 해당 폴더에 이미지 파일 저장하기
    3. html 에 `{% load static %}` 붙인 뒤, img 태그에 `<img src="{% static 'articles/sample_img_1.jpg' %}" alt="sample img">`

- 추가 경로에 있는 static file 가져오기
  1. settings.py 에 `STATICFILES_DIRS = [  BASE_DIR / 'static',]` 추가
  2. 최상단에 static  폴더 생성 (최상단 폴더가 바로 BASE_DIR)
  3. html 에 `<img src="{% static 'sample_img_2.jpg' %}" alt="sample img`">`

### Image Upload

django ImageField() 를 사용하여 미디어 관리

- 특징
  - FileField 를 상속받는 서브클래스
  - 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
    - ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB 에 저장, max_length를 바꿔 수정 가능
- FileField / ImageField를 사용하기 위한 단계
  1. setting.py 에 `MEDIA_ROOT, MEDIA_URL` 설정
  2. `upload_to` 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT 의 하위 경로를 지정 (선택 사항)
- MEDIA_ROOT
  - 기본값 ''
  - 사용자가 업로드한 파일(미디어)들을 보관할 디렉토리의 절대 경로
  - django는 성능을 위해 업로드 파일을 DB에 저장하지 않고, 파일 경로를 저장 (문자열)
  - MEDIA_ROOT 는 STATIC_ROOT와 반드시 다른 경로로 지정 `BASE_DIR / 'media'`
- MEDIA_URL
  - 기본값 ''
  - MEDIA_ROOT 에서 제공되는 미디어 파일을 처리하는 URL
  - 업로드된 파일의 주소 (URL)를 만들어 주는 역할
  - 반드시 `/`로 끝나야 함
  - `MEDIA_URL = '/media'`
  - 프로젝트의 urls.py 에 가서 추가 작성 필요 (https://docs.djangoproject.com/en/4.1/howto/static-files/ 의 serving files uploaded by a user ~~ 참조, 복붙)



#### CREATE

이후 앱의 models.py 에서 models.ImageField() 사용 가능

ImageField()

- 옵션

  - blank
    - 기본값 False
    - True인 경우 필드를 비워 둘 수 있음 (문자열 ' ')
    - 유효성 검사에서 사용됨
    - 보통 이것 사용
  - null
    - 기본값 False
    - True인 경우 필드를 NULL로 저장

- 특징

  - Pillow 라이브러리를 설치해야만 makemigrations 가능
  - 같은 이름의 파일 업로드 시, 임의의 난수 문자를 뒤에 덧붙임

- 실습

  - models.py 에 ImageField() 추가

    `image = imageField(blank=True)`

  - forms.py 에 해당 변수 나타내기

    `fields = (..... , 'image', )`

  - 이후 html 에서 작성 시, form 태그에 인코딩 타입 설정 

    ` enctype='multipart/form-data'`

    원래 enctyp 기본값은 문자마나 인코딩

    미디어 파일 업로드 (`<input type='file'>`) 시에 반드시 위 enctype 타입 사용

  - 파일 및 이미지는 POST 속성으로 넘어가지 않음 => views.py 에서의 함수 인자에 request.FILES 추가

  - 이미지 출력

    - `<img src="{{ article.image.url }}" alt="{{ article.image }}">`
    - 이미지가 없는 경우 오류가 나니, if 문으로 묶어서 사용
    - 파일이기 때문에 기본적으로 url 속성을 사용
    - article.image.url - 업로드 파일의 경로
    - article.image - 업로드 파일의 파일 이름

#### UPDATE

사진 파일 수정은 불가능하니, 새로운 사진 파일로 대체하도록 구현

- 실습
  - 똑같이 html 에 ` enctype='multipart/form-data'`, views.py 에 `request.FILES` 인자 추가

##### 사용자 지정 업로드 경로와 파일 이름 설정하기

ImageField 는 업로드 폴더, 파일 이름 설정하는 방법 2가지 제공

1. 문자열 값이나 경로 지정
   - models.py 에 `ImageField(blank=True, upload_to='images/')`
   - 이러면 media 폴더 안의 images 폴더에 사진이 저장됨
   - 시간에 따른 폴더면 작성은 `upload_to='%Y/%m/%d/'`
2. 함수 호출 방법
   - upload_to 를 models.py에서 함수처럼 호출이 가능, 인자 2개를 받음
   - 인자
     - instance
       - FileField가 정의된 모델의 인스턴스
       - DB에 저장되기 전의 객체이므로, PK값이 없을 수 있음
     - filename
       - 기존 파일 이름

##### 이미지 리사이징

실제 원본 이미지를 서버에 그대로 로드 하는 것은 부담이 큼

업로드 될 때 이미지 자체를 resizing 하는 것을 구현

django-imagekit 라이브러리 사용 (이미지 처리를 위한 django 앱, 썸네일 해상도 등을 조절 가능)

- 실습

  - `$ pip install django-imagekit`
  - settings.py - INSTALLED_APPS 에 `'imagekit'`추가

  1. 원본 이미지 저장 x 방식

     - models.py 에서 imagekit..... 뭐 임포트

     - 외우지 말고, 공식문서 보면서 하기

       

  2. 원본 이미지 저장 o 방식

     - ImageSpecField 임포트 해서 사용

##### 캐시

자주 사용할 이미지 (네이버 로고) 등을 최초 접속 시 캐시 등에 저장한 뒤, 필요할 때마다 부르는 기능



## QuerySet API 심화



