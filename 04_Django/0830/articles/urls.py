from django.urls import path
from . import views                    # views와 같은 위치에 있음 (articles 안에)

app_name = 'articles'
urlpatterns = [
    # index 페이지
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('ping/', views.throw, name='throw'),
    path('pong/', views.catch, name='catch'),
    path('<str:name>/', views.profile, name='profile'),
]
