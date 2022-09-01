import imp
from operator import imod
from django.contrib import admin
from .models import Article

# Register your models here.
# 관리자 계정으로 Article 클래스의 자료를 수정 가능하도록

# 내용도 같이 표시되도록 하는 클래스
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')


# 관리자 계정으로 CRUD 가능
# 관리자.사이트.등록(모델)
admin.site.register(Article, ArticleAdmin)
