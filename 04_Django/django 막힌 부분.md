- 시작할 때 이왕이면 admin 계정 만들기
- render 안에는 "articles:index" 이런 식으로 표현 X
- form 태그 안에 textarea 사용할 때는, <input> 사용하지 않고 바로 <textarea> 사용
- 에러 뜨면 장고의 구조 (url에서 요청 받아서, views 갔다가, model 가서 DB에 접근하고, ...) 생각해보기
- =======
## TemplateDoesNotExist

- settings.py에 TEMPLATES 리스트 안 'DIRS'를 [BASE_DIR / 'templates']로 수정
- settings.py에 INSTALLED_APPS 에 앱 이름(articles) 추가
- templates 폴더 이름 추가
- 경로 확인







### Form

데이터를 생성 및 변경 시, django의 프레임워크를 사용하여 손쉽게 구현 가능

(데이터 조회, 삭제 등은 그냥 models.py의 Article 클래스 사용)

원래는 models.py에 클래스를 직접 만들어서 사용

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

django form을 사용하면

```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    
# articles/views.py 에서 .models Article 클래스 쓰지 말고, .forms ArticleForm 사용
# 그러면 다양한 기능들 사용 가능
# ex. html에서 {{ form.as_p }}로 표현 가능
#	  표현방법 1.Form fields  2. Widgets
```

Django ModelForm을 사용하면 form class 작성 시 중복되는 부분 안써도 됨

```python
# articles/forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        
# Meta 클래스에 ModelForm의 정보 작성
# model은 ModelForm이 참조할 모델
# fields는 참조하는 모델에 정의된 field 정보를 Form에 적용함
# 배제하고픈 필드가 있으면, fields 대신 exclude = ('title', ) 입력
```

이후 view 함수에 articles/forms.py의 `ArticleForm` 사용

- 앱 폴더에 forms.py 생성 후, `from django import forms`를 상속받은 `ArticleForm`이라는 별도의 class 선언
- (TextField) 가 존재하지 않음
- {{ form.as_p }} 처럼 사용
- widget 사용해서 꾸미기 (https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#built-in-widgets)
- 이후 views.py에서 `save()`, `is_valid()`, `form.errors` 사용 가능
- 이후 html에서 `{{ form.as_p}}`, 



# django authentication system

- custom user model 사용을 강력히 권장 (기본 User 모델과 동일하게 작동하면서도 이후 수정 가능. 단, 첫 migrate 실행 전에 수정하기)

  ```python
  # accounts - models.py
  
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      pass
  ```

  ```python
  # accounts - forms.py
  from django.contrib.auth.forms import UserCreationForm
  from django.contrib.auth import get_user_model
  
  
  class CustomUserCreationForm(UserCreationForm):
  
      class Meta(UserCreationForm):
          model = get_user_model()
          fields = UserCreationForm.fields
  ```

  

  이후 M:N 기능 등을 사용할 때 자유롭게 유저 모델을 사용하기 위해, 상속받은 CustomUserModel을 사용

  

- login

  - AuthenticationForm

    username과 password가 유효한지 검증

- logout

  - 세션을 delete하는 과정



## 1013



- html 태그에서 헷갈리는 게 있으면 mdn 문서 보기

- 장고에서 미디어파일 사용하려면 인코딩 타입 수정, 파일이 가는 경로(urls.py) 확인

- ModelForm 에서 특정 pk를 갖는 데이터 찾기

  ```python
  a = Article.objects.get(pk=article_pk)
  form = ArticleForm(instance=a)
  ```

- model 은 사용할 표 (테이블), ModelForm 은 model을 그대로 상속받으면서 편리한 기능(유효성 검사 등)을 사용할 수 있는 클래스.

  즉, model 에서 데이터를 삭제하면 ModelForm 도 당연히 사라짐

- 로그인 기능 구현 시, `accounts - models.py` 에서 새로 상속받은 User 클래스 생성

  `accounts - forms.py` 에 CustomUserCreationForm 만들어서 사용

  이후 `class Meta`에서 `model = get_user_model()`  해서 현재 새로 정의한 유저 모델 사용하도록 하기

- 로그인 views 함수 작성 시, `from django.contrib.auth.forms import AuthenticationForm` 받아서 사용

  AuthenticationForm : 유저가 존재하는지를 검증하는 Django 내장 모델 폼. 사용자가 로그인 폼에 작성한 정보가 유효한지를 검증함

- auth_login 에서 

  1. ```python
     user = form.save()
     auth_login(request, user)
     ```

  2. ```python
     auth_login(request, form.get_user())
     ```

     둘 다 되는 이유는, save() 가 `self.instanc`를 반환하기 때문

- 로그인 관련 기능 사용 시, `request.user` 하면 사용자 정보에 접근 가능

- 로그인 한 뒤 글 쓸 때, 자동으로 user_id 를 할당하는 법 (글 쓸 때 user 도 선택하지 않도록 하기)

  ```python
  article = form.save(commit=False)
  article.user = request.user
  ```

  하면 글 쓸 대 user 입력하지 않아도 자동으로 로그인된 유저 저장
