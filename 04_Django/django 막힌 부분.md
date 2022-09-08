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
