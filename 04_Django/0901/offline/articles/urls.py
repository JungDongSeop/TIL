# 경로 관리하는 파일
from django.urls import path
# django는 항상 경로를 명시적으로 표기할 것을 권장
from . import views


# app 이름 등록
# app_name 변수명은 반드시 지켜야 한다.
# 왜? url tag 사용할 때, 변수명 app_name을 찾아가도록 설정되어 있어서
app_name = 'articles'

urlpatterns = [
    # 경로 이름 설정을 통해서
    # 추후에 경로가 바뀌게 되더라도 경로 이름으로 호출할 것이기 때문에
    # 불필요한 작업을 줄일 수 있다.
    path('index/', views.index, name='index'),
    # 게시글 생성 페이지
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # 게시글의 제목을 클릭하면, 그 글의 상세 내용으로 이동하는 법
    # pk == id == INT
    # 15번 게시글을 보여달라는 요청을
    # articles/15/라는 경로로 요청을 보내도록 만들 것이다.
    # 15라는 숫자는 article_pk 라는 변수에 담겨서, detail view 함수에 인자로 넘겨질 것이다.
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete', views.delete, name='delete'),
    path('<int:article_pk>/edit', views.edit, name='edit'),
    path('<int:article_pk>/update', views.update, name='update'),

]
