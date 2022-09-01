"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 앞에 작성하는 경로는 우리가 직접 지정하는 것이기 때문에
    # articles app으로 이동하기 위해서
    # 반드시 articles라는 경로를 만들어 줘야 하는 것은 아니다ㅏ
    # path('', include('articles.urls))
    # 그래도 안헷갈리기 위해서 적자
    path('articles/', include('articles.urls'))
]
