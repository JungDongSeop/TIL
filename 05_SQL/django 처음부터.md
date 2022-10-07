목표 

1. 로그인 기능 구현
2. 게시글과 유저 연결
3. 댓글을 게시글, 유저와 연결

# 가상환경 만들기

터미널 켜서 

- `python -m venv venv`

- 가상환경 활성화  `source venv/Scripts/activate`

- 원하는 package 설치  `pip install django==3.2.13`

- 장고 설치 `pip install dajngo==3.2.13`

- requirements.txt 만들기 `pip freeze > requirements.txt`

  

# 장고 프로젝트 생성

장고에게 명령

- 프로젝트 생성`django-admin startproject crud .`
- 이후 서버 켜서 settings.py 106번째 줄 ko-kr , 언어는 Asia/Seoul 로 바꾸기



앱 생성

- 앱 만들기  `$ python manage.py startapp articles`
- settings.py 에 앱 등록  (installed_apps 에 `articles` 추가)



명령 요청, 응답 해줄 시스템 만들기 (url, view, templates)

- 프로젝트 crud - urls.py 안에 `path('articles/', include('articles.urls')),` 등록 (이 때 import path, include 하기)

- 앱 aricles에 `urls.py` 파일 만들기

- ```python
  from django.urls import path
  from . import views
  
  
  app_name = 'articles'
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```

- 이제 views.py 에 index 함수 만들러 가기

- ```python
  from django.shortcuts import render
  
  # Create your views here.
  def index(request):
      # request 에는 모든 요청 정보들이 들어있다.
      # path 함수에 views.index 함수 정보 넘겨 주면서
      # path 함수 내부에서 호출할 때 첫번째 인자 넘겨준다.
      return render(request, 'articles/index.html')
  ```

- 이후 templates/articles 만들어서 안에 index.html 만들기

- base.html 만들기

  - settings.py 의 TEMPLATES 에 `'DIRS': [BASE_DIR / 'templates'],` 로 수정, 이러면 base.html 을 찾으러 갈 때 templates/article 만 찾는 게 아닌, 전체 폴더에 있는 templates 도 찾아감
  - 이후 전체 폴더에 templates 만들고 base.html 만들기
  - 서식 만들고, 우리가 작업할 공간을 만들기 위해 `{% block content %}  {% endblock content %}`

# 모델 만들기

장고의 models.Model 을 상속받아서, CRUD 구현 (테이블 만들기) (DB의 청사진)

- articles/models.py 에 Article 클래스 만들기

- ```python
  class Article(models.Model):
      title = models.CharField(max_length=50)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  ```



### 테이블 설계도 만들기

- `python manage.py makemigrations` 
- `python manage.py migrate`



### views.py 에서 다양한 기능 구현하기

views.py 에서 `from .models import Article` 불러오기. 이후 Article 클래스 활용해서 기능 구현

- index.html 에서 모든 게시물 보여주기

- ```python
  def index(request):
      # request 에는 모든 요청 정보들이 들어있다.
      # path 함수에 views.index 함수 정보 넘겨 주면서
      # path 함수 내부에서 호출할 때 첫번째 인자 넘겨준다.
  
      # 모든 게시물 보여주기
      # Model.Manager.Query Set API
      # SELECT * FROM articles_article
      # <Query SET [<Article object(1)>, ]>
      articles = Article.objects.all()
      context = {
          'articles': articles
      }
  
      return render(request, 'articles/index.html', context)
  ```

- 



# 게시글 작성 기능 구현

urls.py 에 create 로 가는 길 만들고, views.py 에 create 함수 만들고, create.html 에 페이지 만들기

- forms.py  만들고, 그 안에 django 의 ModelForm 상속받아서 우리가 원하는 ArticleForm 클래스 만들기

- ```python
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
  
      # ArticleForm class 가 어떻게 정의되는지
      # 그 정보는 Meta class 에 넣는다
      class Meta:
          model = Article
          # fields = '__all__'
          exclude = ('user', )
  ```

- 

- 이후 class Meta 에 우리가 직접 만든 Article 클래스를 입력해서 받아올 스키마? 를 선언

- ```python
  from django import forms
  from .models import Article
  
  
  class ArticleForm(forms.ModelForm):
  
      # ArticleForm class 가 어떻게 정의되는지
      # 그 정보는 Meta class 에 넣는다
      class Meta:
          model = Article
          fields = '__all__'
  ```

- 이후 views.py 에  ArticleForm 받아서 활용

- ```python
  def create(request):
      # 제목, 내용 등은 전부 ArticleForm 안에 있음
      form = ArticleForm()
      context = {
          'form': form
      }
      return render(request, 'articles/create.html', context)
  ```

- create.html 에 POST 형식으로 보내기

- ```html
      <form action="{% url 'articles:create' %}" methon="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit" value="글 생성">
  ```

- views.py create 함수에 POST로 온 것만 처리

- ```python
  def create(request):
      # 제목, 내용 만들기
  
      # 사용자가 POST 요청을 보냈다면,
      # 게시글을 생성 해 줄 것이다.
      if request.method == 'POST':
          # 사용자가 POST 요청을 보낼 때 같이 보낸 정보들..
          # model에 대한 정보와 form에 대한 정보 모두 가지고있는
          # ArticleForm 에게 사용자의 요청 정보를 같이 넘겨줘서
          form = ArticleForm(request.POST)
          # 사용자가 보낸 정보가 정상적인 데이터인지 확인
          if form.is_valid():
              # 올바른 데이터면 저장
              form.save()
              return redirect('articles:index')
      else:
          form = ArticleForm()
      context = {
          'form': form
      }
      return render(request, 'articles/create.html', context)
  ```



### 게시글 번호에 따라 다른 페이지 만들기 (게시글 별 상세 페이지)

variable routing 기능 사용, 게시글에 따른 상세 페이지 만들기

- urls.py 에 

- ```python
      path('<int:article_pk>/', views.detail, name='detail'),
  ```

- views.py 에

- ```python
  def detail(request, article_pk):
      # <Article object(article_pk)>
      # article.pk, article.title, article.content
      article = Article.objects.get(pk=article_pk)
      context = {
          'article': article
      }
      return render(request, 'articles/detail.html', context)
  ```

- detail.html 만들고

- ```python
  {% extends 'base.html' %}
  
  {% block content %}
      <h1>DETAIL PAGE</h1>
  
      <p>{{ article.pk }}번째 글</p>
      <hr>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성 시간 : {{ article.created_at }}</p>
      <p>수정 시간 : {{ article.updated_at }}</p>
      <hr>
      <a href="{% url 'articles:index' %}">[BACK]</a>
  {% endblock content %}
  ```

- 이제 index.html 에서 게시글 클릭하면 상세페이지로 가도록

- ```html
      {% for article in articles %}
      {% comment %} url 에 article.pk 넣어서 detail 함수로 갈 때의 인자를 제공 {% endcomment %}
  
      <a href="{% url 'articles:detail' article.pk %}">
          <p>{{ article.pk }} 번 째 글</p>
          <p>제목 : {{ article.title }}</p>
      </a>
          <hr>
      {% empty %}
          <p>게시글이 없습니다.</p>
      {% endfor %}
  ```





# 게시글에 대해 댓글을 저장

N:1 관계 시작. 1번 게시글에 단 댓글을 Comment 클래스로 생성, 이 때 해당 Article(게시글) 의 pk를 같이 저장해서 N:1 관계를 유지

- models.py 에 새로운 클래스 Comment 만들기

- ```python
  class Comment(models.Model):
      # 외래 키
      # 컬럼명 : 내가 참조하고있는 대상의 이름을 소문자로 만들면 
      # table에서는 '컬럼명_id'으로 생성
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
  
      def __str__(self):
          return self.content
  ```

  models.py를 바꿨으니 makemigrations, migrate 해서 새로운 테이블 스키마(청사진) 만들기

- detail.html에서 아래 기능 추가

- ```html
      <p>--댓글--</p>
      <form action="" method='POST'>
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit" value="댓글 생성">
      </form>
  ```

- 이제 모델폼 만들어야하니, forms.py에서 

- ```python
  class CommentForm(forms.ModelForm):
      
      class Meta:
          model = Comment
          # fields = '__all__'        # 이처럼 하면, 댓글 달 때 게시글 종류를 선택 가능함
                                      # 이는 우리가 원하는 기능이 아님
          # article 은 제외하고 나오도록 하자.
          # 튜플이니 쉼표 반드시 넣어야함
          exclude = ('article', )
  ```

- views.py에서 detail 함수에 추가

- ```python
  def detail(request, article_pk):
      # <Article object(article_pk)>
      # article.pk, article.title, article.content
      article = Article.objects.get(pk=article_pk)
      form = CommentForm()
      context = {
          'article': article,
          'form': form
      }
      return render(request, 'articles/detail.html', context)
  ```

### 이제 댓글을 생성하는 경로를 만들자.

comment 를 create

- urls.py

- ```python
      path('<int:article_pk>/comments/create/', views.comment_create, name='comment_create'),
  
  ```

- views.py

- ```python
  def comment_create(request, article_pk):
      if request.method == 'POST':
          form = CommentForm(request.POST)
          if form.is_valid():
              form.save()
  
      return redirect('articles:detail', article_pk)
  ```

  - 이렇게 하면 문제 발생 (IntegrityError, 무결성 에러)

    사용자 편의를 위해 exclude('article', )를 했더니 comment_create 의 pk 가 누락됨

  - 이를 views.py에서 수정

  - ```python
    def comment_create(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                # comment 객체 생성
                # 저장해서 생성하는데, db에 반영은 안되도록
                comment = form.save(commit=False)
                comment.article = article       # 삭제했던 comment-article 을 추가로 만들어줌
                comment.save()
    
        return redirect('articles:detail', article_pk)
    ```

- detail.html 

- ```html
      <p>--댓글--</p>
      <form action="{% url 'articles:comment_create' article.pk %}" method='POST'>
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit" value="댓글 생성">
      </form>
  ```

  - form action 에 url 추가

### 댓글을 페이지에 출력

방법 1

- detail.html  에서

- ```html
      {% comment %} 댓글 표시 {% endcomment %}
      {% for comment in article.comment_set.all %}	여기에서 article 의 댓글들을 불러옴
          <p>{{ comment.content }} - {{ comment.created_at }}</p>
      {% endfor %}
      <hr>
  ```

- 이 때 `article.comment_set.all` 은 `context의 변수명 . 클래스 이름을 소문자로 . all`

views.py  의 detail 함수에서 처리하기



# 로그인 기능 구현

- accounts 앱 생성 `$ python manage.py startapp accounts`
- crud 폴더의 settings.py, ursl.py 에 앱 등록

이후 models.py 에 User 상속받아서 사용

- settings.py 맨 마지막 줄에 `AUTH_USER_MODEL = 'accounts.User'` 써서 덮어씌우기

- 이러면 앞으로 accounts 앱의 User 를 찾아서 사용하게 됨

- 이후 forms.py 에 

- ```python
  from urllib.parse import uses_relative
  from django.contrib.auth.forms import UserCreationForm
  from django.contrib.auth import get_user_model
  
  class CustomUserCreationForm(UserCreationForm):
  
      class Meta(UserCreationForm.Meta):
          model = get_user_model()
          fields = UserCreationForm.Meta.fields
  ```

  UserCreationForm 상속받아서 내멋대로 바꾸기

- 이후 views.py 에

- ``` python
  from django.shortcuts import redirect, render
  # from django.contrib.auth.forms import UserCreationForm
  from .forms import CustomUserCreationForm
  # Create your views here.
  def signup(request):
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = CustomUserCreationForm()
      context = {
          'form': form
      }
      
      return render(request, 'accounts/signup.html', context)
  ```

### 로그인 됐는지 확인

회원가입하면 바로 로그인시키고 메인화면으로 이동

- views.py에

- ```python 
  from django.contrib.auth import login as auth_login
  ```

  불러오기, 이후 signup 함수 약간 수정

  ```python
  def signup(request):
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()				#
              auth_login(request, user)		# 여기 달라짐
              return redirect('articles:index')
      else:
          form = CustomUserCreationForm()
      context = {
          'form': form
      }
      
      return render(request, 'accounts/signup.html', context)
  ```

  

- base.html 에 로그인된 경우 아이디 출력, 아니면 signup 하이퍼링크 출력

- ```python
      {% if request.user.is_authenticated %}
          <p>{{ user.username }}</p>
      {% else %}
          <a href="{% url 'accounts:signup' %}">[SIGN UP]</a>
      {% endif %}
  ```

### 로그아웃

- urls.py

  - 

    ```py
        path('logout/', views.logout, name='logout'),
    ```

- views.py

  - 

    ```python
    from django.contrib.auth import logout as auth_logout
    
    def logout(request):
        if request.user.is_authenticated:
            auth_logout(request)
        return redirect('articles:index')
    ```

- base.html

  - 

    ```html
           {% comment %} 로그아웃 버튼 {% endcomment %}
            <form action="{% url 'accounts:logout' %}" method='POST'>
                {% csrf_token %}
                <input type="submit" value='LOGOUT'>
            </form>
    ```

- 

이제 로그아웃을 POST 요청일 때만 처리하자

- views.py 에

- ```python
  from django.views.decorators.http import require_POST
  
  @require_POST					# 이거 추가
  def logout(request):
      if request.user.is_authenticated:
          auth_logout(request)
      return redirect('articles:index')
  ```



### 로그인 기능 구현

여태까진 회원가입 시 자동 로그인, 로그아웃 기능을 만들었다. 

이제 항상 로그인 할 수 있는 기능 구현

- urls.py

  - ```python
        path('login/', views.login, name='login'),
    ```

- views.py

  - ```python
    from django.contrib.auth.forms import AuthenticationForm
    
    def login(request):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)
    ```

- base.html 에 추가

  - ```python
            <a href="{% url 'accounts:login' %}">[LOGIN]</a>
    ```

- views.py 추가

  - ```python
    def login(request):
        # POST 요청일 때 (로그인 정보 입력하고 submit)
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                # form.save() 아님. db에 저장할 거 아니니까
                auth_login(request, form.get_user())    # 로그인 기능 구현
                return redirect('articles:index')
    
        # GET 요청일 때 (로그인 하려고 로그인화면 들어온 경우)
        else:
            form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)
    ```

  - 이전 views.py login 함수는 그냥 로그인 하고 싶을 때 그 화면으로 가는 것만 구현.

    이후 추가된 내용은, 로그인 정보 입력하고 submit 했을 때 실제로 로그인되는 과정 구현



# 로그인 된 유저가 댓글 작성

- articles 폴더의 models.py 에 

  ```python
  from django.conf import settings
  
  # Create your models here.
  class Article(models.Model):
      # user = models.ForeignKey(User)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # 로그인 한 계정으로 댓글 달기 기능 (N:1)
  
      title = models.CharField(max_length=50)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  ```

  입력, 이후 makemigrations. 

- 이러면 이전에 만들어둔 정보에 user 정보 값이 없기 때문에 오류가 남, 이 때 NULL 인 컬럼에 어떤 값을 입력할지 정하라고 말함
- 그냥 1번 사용자가 쓴 글이라고 하고 넘어가자.

이후 게시글 생성 창(create)으로 들어가면, 댓글 때와 마찬가지로 이미 로그인돼 있는 경우에도 글을 작성할 사용자를 고를 수 있게 되어버림.

- 위에서 했듯이 forms.py 에

- ```python
  class ArticleForm(forms.ModelForm):
  
      # ArticleForm class 가 어떻게 정의되는지
      # 그 정보는 Meta class 에 넣는다
      class Meta:
          model = Article
          # fields = '__all__'		# 여기
          exclude = ('user', )
  ```

- views.py 에

  로그인 안한 사람이 클릭하면, 바로 로그인 화면으로 이동하도록 하는 데코레이터 `@login_required`

- ```python
  from django.contrib.auth.decorators import login_required
  
  @login_required    						 		# 로그인 해야 글 생성을 할 수 있게
  def create(request):
      # 제목, 내용 만들기
  
      # 사용자가 POST 요청을 보냈다면,
      # 게시글을 생성 해 줄 것이다.
      if request.method == 'POST':
          # 사용자가 POST 요청을 보낼 때 같이 보낸 정보들..
          # model에 대한 정보와 form에 대한 정보 모두 가지고있는
          # ArticleForm 에게 사용자의 요청 정보를 같이 넘겨줘서
          form = ArticleForm(request.POST)
          # 사용자가 보낸 정보가 정상적인 데이터인지 확인
          if form.is_valid():
              # 올바른 데이터면 저장
              article = form.save(commit=False)		#
              article.user = request.user				#
              article.save()							# 여기 달라짐
              return redirect('articles:index')
      else:
          form = ArticleForm()
      context = {
          'form': form
      }
      return render(request, 'articles/create.html', context)
  ```

- index.html 에

- ```html
  
      {% for article in articles %}
      {% comment %} url 에 article.pk 넣어서 detail 함수로 갈 때의 인자를 제공 {% endcomment %}
      <a href="{% url 'articles:detail' article.pk %}">
          <p>작성자 : {{ article.user }}</p>			# 여기 달라짐
          <p>{{ article.pk }} 번 째 글</p>
          <p>제목 : {{ article.title }}</p>
      </a>
          <hr>
      {% empty %}
          <p>게시글이 없습니다.</p>
      {% endfor %}
  ```

### 로그인 안하고 글 썼을 때, 로그인 창으로 이동

게다가 이전에 쓰던 글도 유지되도록

- accounts - views.py - login 함수에서

- ```python
  def login(request):
      # POST 요청일 때 (로그인 정보 입력하고 submit)
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              # form.save() 아님. db에 저장할 거 아니니까
              auth_login(request, form.get_user())    # 로그인 기능 구현
              return redirect(request.GET.get('next') or 'articles:index')	# 여기 달라짐
              # return redirect('articles:index')
  ```



# 게시글 삭제

- urls.py

- ```python
      path('<int:article_pk>/delete/', views.delete, name='delete'),
  ```

- views.py

- ```python
  from django.views.decorators.http import require_POST
  
  @require_POST
  def delete(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      article.delete()
      return redirect('articles:index')
  ```

이렇게 하면 아무나 글을 삭제할 수 있다.

- 로그인 한 사람만 삭제 구현

  - delete 함수 위에 `@require_POST`  데코레이터 붙이기

  - 이러면 로그인 화면으로 넘어가고, 로그인 시 GET 요청으로 받은 실행 (delete 실행하라는 명령) 계속 진행

  - 이러면 오류 남(require_POST인데 GET으로 요청 보냈으니). 그러므로 조건 분기

  - ```python
    @require_POST
    def delete(request, article_pk):
        if request.user.is_authenticated:
            article = Article.objects.get(pk=article_pk)
            article.delete()
            return redirect('articles:index')
        return redirect('accounts:login')
    ```

- 작성자 아닌 사람이 삭제하는 것 막기

  - 조건 분기. 작성자와 같은 유저일때만 삭제하도록

  - ```python
    @require_POST
    def delete(request, article_pk):
        if request.user.is_authenticated:
            article = Article.objects.get(pk=article_pk)
            if article.user == request.user:				# 여기 달라짐
                article.delete()
            return redirect('articles:index')
        return redirect('accounts:login')
    ```

  - 
