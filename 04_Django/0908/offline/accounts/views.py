from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm



# user 객체
User = get_user_model()

# Create your views here.
def index(request):
    # 모든 유저 목록
    # Model.manager.querySet API
    # Article.objects.all()
    users = User.objects.all()      # <QuerySet <UserObject(1)>, >
    context = {
        'users': users
    }
    
    # 각 app/templates/accounts/ 폴더 경로 안쪽 탐색
    # html을 사용자에게 render해서 보내준다.
    return render(request, 'accounts/index.html', context)

def signup(request):
    # 회원가입이란....
    if request.method == "POST":
        # 생성  
        # 사용자가 보내온 요청에 따라서 (함께 보낸 정보들을 토대로)
        # 새 유저 생성
        form = CustomUserCreationForm(request.POST)
        # print(form)
        
        # 유효성 검사
        if form.is_valid():
            user = form.save()
            # 회원가입 완료 후, 자동 로그인 (필수 x)
            auth_login(request, user)
        
            return redirect('accounts:index')
    else:
        # 조회
        # 회원 정보를 입력해서 요청을 보낼 수 있는 form 태그가 있는
        # 페이지가 필요하다.
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

# 요청받은 사용자에게 응답하니, 따로 사용자 정보를 전달받아 로그아웃 할 필요는 없음
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def login(request):
    if request.method == 'POST':
        # 사용자가 보낸 데이터를 토대로 form 생성
        form = AuthenticationForm(request, request.POST)
        # form에 들어있는 데이터 유효성 검사
        if form.is_valid():
            # db에 저장은 -> session id만 할거고,
            # 그건.. login 함수가 해줄 것이다...
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
    # 로그인이란...
    # 내 계정 정보를 입력하여
    # 내 서버에 나를 인증하는 페이지..
        form = AuthenticationForm()     # 인증 폼
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)
    