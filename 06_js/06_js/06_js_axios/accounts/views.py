from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm
)
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.http import JsonResponse

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 !
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index') 


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    # CODE HERE
    # 현재 활성화 된 유저 객체 정보 받아오기
    User = get_user_model()
    person = get_object_or_404(User, pk=user_pk)
    me = request.user
    # 인증을 거친 유저여야지만 follow 가능 (user pk가 있음)
    if request.user.is_authenticated:
        # 본인 팔로우 안됨
        if me != person:
            # 저 사람의 팔로워 목록에 내가 있으면
            # if person.followers.get(pk=me.pk):  # get API는 대상이 0일때도 오류 발생
            if person.followers.filter(pk=me.pk).exists():
                # 이미 팔로우 중인데 또 팔로우 버튼을 눌렀다?
                person.followers.remove(me)
                is_followed = False
            # 없으면
            else:
                # 팔로우 안했는데 팔로우 버튼을 눌렀다?
                person.followers.add(me)
                is_followed = True
            # JSON 데이터를 응답해 줘야한다.
            # follow boolean 구분해서 JSON으로 보내줄 것 -> 딕셔너리로 전송
            context = {
                'is_followed': is_followed,
                'followers_count': person.followers.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
