"""firstpjt URL Configuration

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
    # index 페이지

    path('articles/', include('articles.urls')),
# articles 안에 있는 views를 아래가 아닌, 위와 같이 표현
    # path('index/', views.index),
    # path('greeting/', views.greeting),
    # path('dinner/', views.dinner),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('<str:name>/', views.profile),

    path('pages/', include('pages.urls')),
]
