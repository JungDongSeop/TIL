import random
from unicodedata import name
from django.shortcuts import render

# Create your views here.

# request 변수에는 요청받은 모든 정보가 있음?
def index(request):
    print(dir(request))
    print(request.user)
    # template을 return
    return render(request, 'articles/index.html')

def greeting(request):
    name = 'Alice'

    foods = ['파스타', '짬뽕', '비빔밥']

    context = {
        'name' : name,
        'foods' : foods
    }
                                        # context도 return 됐으니, greeting.html에서도 context 안의 변수 'name'을 사용 가능
    return render(request, 'articles/greeting.html', context)

# import random 사용
def dinner(request):
    foods = ['라면', '김밥', '쫄면', '떡볶이']

    wallet = []

    context = {
        'foods' : foods,
        'random_menu' : random.choice(foods),
        'wallet' : wallet
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):

    print(dir(request))
    # GET으로 받은 정보가 request 안에 있음
    # request.GET 하면 그 정보에 접근 가능
    print(request.GET)
    print(request.GET.get('username'))

    username = request.GET.get('username')
    context = {
        'username': username
    }

    return render(request, 'articles/catch.html', context)

def profile(request, name):
    context = {
        'name': name
    }

    return render(request, 'articles/profile.html', context)