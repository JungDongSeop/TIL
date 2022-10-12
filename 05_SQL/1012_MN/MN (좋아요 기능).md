## M:N (Articles-User)

좋아요 기능 등을 위한 M:N 관계 설정



계정의 models.py - User 클래스와 앱의 models.py - Article 클래스를 연결



실습

- 앱 models.py - Article 클래스에 `  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)` 추가
- 여기서 makemigrations 하면 기존에 만들어둔 N:1 관계와 충돌이 일어남 (user.article_set 을 선언했을 때 어떤 모델을 참조할지 결정이 불가능해짐 => M:N 관계의 설정을 바꾸자.)
- M:N 관계에서 user.article_set 을 user.like_articles_set으로 바꾸자 (related_name 사용)
- `  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')`
- 정리
  - article_user
    - 게시글을 작성한 유저 - N:1
  - user.article_set
    - 유저가 작성한 게시글(역참조) - N:1
  - article.like_users
    - 게시글을 좋아요한 유저 - M:N
  - user.like_articles
    - 유저가 좋아요한 게시글 (역참조) - M:N



- 이후 articles - urls.py 가서 경로 추가, views.py, html 작성

- views.py 

- ```python
  def likes(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      # 좋아요 추가할지 취소할지 무슨 기준으로 if문을 작성할까?
      # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지를 확인
      # article.like_users.filter(pk=request.user.pk)
      if request.user in article.like_users.all():
      # 이런 조건문도 가능
      # if article.like_users.filter(pk=request.user.pk).exists():
          # 좋아요 취소 (remove)
          article.like_users.remove(request.user)
      else:
          # 좋아요 추가 (add) (다대다 관계)
          article.like_users.add(request.user)
      return redirect('articles:index')
  
  ```

- index.html

- ```html
      <div>
        <form action="{% url 'articles:likes' article.pk %}" method='POST'>
          {% csrf_token %}
          {% if request.user in article.like_users.all %}
            <input type="submit" value='좋아요 취소'>
          {% else %}
            <input type="submit" value='좋아요'>
          {% endif %}  
          </form>
      </div>
  ```

- 



- QuerySet API의 메서드 exists()
  - QuerySet에 결과가 포함되어 있으면 True, 없으면 False
  - 큰 QuerySet 에 있는 특정 개체의 존재와 관련된 검색에 유용 (빠름)





## M:N (User-User)



#### 프로필 기능 구현

accounts 에 구현

- urls.py

- ```python
      path('profile/<str:username>/', views.profile, name='profile'),
  
  ```

- views.py

- ```python
  def profile(request, username):
      User = get_user_model()         # 현재 유저 모델들을 부르는 함수. 장고에서 이렇게 구현하기를 권장
      person = User.objects.get(username=username)
      context = {
          'person': person,
      }
      return render(request, 'accounts/profile.html', context)
  ```

- profile.html

- ```html
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>{{ person.username }}</h1>
  
  	<h2>{{ person.username }}이	작성한 게시글 목록</h2>
  	{% for article in person.article_set.all %}
  		<div>{{ article.title }}</div>
  	{% endfor %}
  	<hr>
  	<h2>{{ person.username }}이 작성한 댓글 목록</h2>
  	{% for comment in person.comment_set.all %}
  		<div>{{ comment.content }}</div>
  	{% endfor %}
  	<hr>
  	<h2>{{ person.username }}이 좋아요 한 모든 게시글</h2>
  	{% for article in person.like_articles.all %}
  		<div>{{ article.title }}</div>
  	{% endfor %}
  	<hr>
  
  	<a href="{% url 'articles:index' %}">back</a>
  
  {% endblock content %}
  ```



#### 팔로잉 기능 구현

accounts - models.py 가서 상속받은 User 모델을 드디어 수정해본다.

- models.py

- ```python
  class User(AbstractUser):
      followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
  ```

- urls.py

- ```python
      path('<int:user_pk>/follow/', views.follow, name='follow'),
  ```

- 

- views.py

- ```python
  def follow(request, user_pk):
      User = get_user_model()
      me = request.user
      you = User.objects.get(pk=user_pk)
      # 내가(request.user) 그 사람의 팔로워 목록에 있다면
      if me != you:
          if me in you.followers.all():
              # 언팔로우
              you.followers.remove(me)
          else:
              # 팔로우
              you.followers.add(me)
      return redirect('accounts:profile', you.username)
  ```

- profile.html 에 추가

- ```html
  	{% if request.user != person %}
  		<div>
  			<form action="{% url 'accounts:follow' person.pk %}" method='POST'>
  				{% csrf_token %}
  				{% if request.user in person.followers.all %}
  					<input type="submit" value='언팔로우'>
  				{% else %}
  					<input type="submit" value='팔로우'>
  				{% endif %}
  			</form>
  		</div>
  	{% endif %}
  ```

- 



## Fixtures

유저 A, B 가 협업할 때, gitignore 에 의해 db가 없는 빈 프로젝트를 받는다.

django 앱을 처음 설정할 때 동일하게 준비된 데이터로 DB를 미리 채우는 것이 필요한 순간이 있다.

django는 fixtures를 사용해 앱에 초기 데이터를 제공할 수 있다.

즉, migrations와 fixtures를 사용하여 data와 구조를 공유하게 된다.

#### 초기 데이터 제공

준비 : 유저, 게시글, 댓글, 좋아요 등 각 데이터 2개 이상 생성

fixtures

- django가 db로 가져오는 방법을 알고 있는 데이터 모음 (즉, 장고가 직접 만든다)
- 기본 경로
  - app_name/fixtures/
  - 앱의 디렉토리 안에 fixtures 디렉토리 생성
- 생성
  - dumpdata
  - `python manage.py dumpdata ... > {filename}.json`
  - ex) `$ python manage.py dumpdata --indent 4 accounts.user > users.json`
- 로드
  - loaddata
  - `$ python manage.py loaddata articles.json comments.json users.json`



## Improve Query

주석보다 주석 아닌 코드가 더 빠름

```python
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')
```

```python
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.select_related('user').order_by('-pk')
```

```python
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
```

위 3개 한번에 합치기

```python
    # articles = Article.objects.order_by('-pk')
    # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')
```

