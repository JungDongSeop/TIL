string interpolation     (보간법)

실수로 max 등 예약어에 할당을 해 버렸다  => 명령어 `del max` 실행

왜 안바뀌지? 원본에는 변화가 없다

```python
for i in range(len(fruit_list)):

    fruit_list[i].lower()
```

여러 줄에 걸친 숫자들 input

```python
list_1 = [list(map(int, input().split())) for i in range(N)]
```

바로 list 의 원소들로 비교

```python
S = [[x1, y1], [x2, y2]]
for x, y in S:
    x = x + y
```

type 찾는 법

```python
if type(5) == int:
    print("wow")
```

가변 인자 `*args`, 키워드 가변 인자 `*kwargs`

```python
*args 는 입력받은 인자들을 Tuple 로 반환
**kwargs 는 입력받은 인자들을 dictionary 로 반
```

아스키코드

```python
ord('A')        # 65
chr(65)        # 'A'
```

sum list

```python
sum([[1],[2,3],[4,5,6],[7,8,9,10]], [])    # [1,2,3,4,5,6,7,8,9,10]
```

얕은 복사, 깊은 복사

```python
listA = [[False] * 3] * 3
listA[1][2] = True
#이 때 listA == [[False, False, True],[False, False, True],[False, False, True]]
```

파일 open 할 대

```python
# 파일 열기
movie = open('sample.json', encoding='utf-8')
    # sample.json이 이 .py 파일과 같은 위치에 있을 때
    # 뒤 encoding은?
# 파일 로딩
movie_detail = json.load(movie)
```

단축키

```python
Alt + 방향키            # 줄 한칸 위로 옮김
ctrl + Alt + 방향키    # 여러 줄에 동시에 입력 가
```

코드 짤 때 무엇이 주체인지 생각하고 코드 짜기!!

.

class 에서 메서드 작성할 때 클래스 변수 사용하기

```python
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1        # 클래스.클래스변수 이런 식으로 해야
        Doggy.birth_of_dogs += 1
```

class 메서드 할 때는 `@classmethod` 넣고 작성

    안그러면 그냥 인스턴스 메서드로 들어감

    클래스 메서드는 인스턴스 변수나 메서드 아예 안쓰는 메서드 작성 시 사용

dictionary는 sequence가 아님

.

dictA.get('key') 할 때 key가 없으면 None 반환

.

path parameter

중괄호 안에 들어갈 단어?

? 뒤 Query String

?api_key=_****__****

&language=en_US (아니면 en_UK, ko_KR 등등 골라서)

이렇게 경로를 만들어서 request 하면 됨

responses

200 : 성공

404 : 요청한 주소 존재하지 않음

401 : 인증받지 않은 유저 (api key 없을 때)

python requests 사용법

```python
import requests

url = 'https://api.agify.io/?name=jun'
response = requests.get(url)        # response는 dict, list 등 제공된 데이터 형태
requests.get(url).json()
```

url 예시 : [https://www.agify.io/movie.{movie_id}](https://www.agify.io/movie.%7Bmovie_id%7D)

api_key 필요

회원가입 후 api_key 신청, 발급, 그 key값 저장해둔 뒤 계속 사용

notion 공용 문서에 발급받는 방법 설명 나옴

인터넷 rest api 로 데이터 받는 법

```python
URL = 'https://api.agify.io' # base url

params = {                    # query string 
    'name': 'michael',
    'country_id': 'KR',
}

response = requests.get(URL, params=params).json()
```

html : CSS 선택자에 마우스 올리면 명시도? 순서도? 나타남

bootstrap 에서 d-flex는 부모의 class에 부여, 그 후 정렬하고 싶은거 생기면 임의로 부모 만든 뒤 justify~ 작성

이미지 크기 조절은 `<a>`에서 `style="width: 30px"`, `<img>`에서 `class="img-fluid"`

이미지 간격 조절은 `<a>`에서 `class="mx-3"`

## 관통 PJT

## 관통 PJT

길러야 하는 것 : 자료를 보는 법, PJT 경험

README.md 에 기록할 것들

- 문제 발생 시 원인, 해결 과정/방법 기록

- 참고 문헌 기록

- 어려웠던 이유

- 새로운 시도와 그 이유 

pjt 하나 당 1 repository 만들어서 올리기

    폴더 만들고

    git init

    git add .

    git commit -m "first commit"

    git lab에서 새 프로젝트 만들기

    git remote add origin https:// 어쩌고 복붙

    git push 하면 오류 뜨면서 push 명령어 새로 줌, 그거 복붙

    이후 gitlab 가서 project information - members - invite memebers - 교수님을 maintaner로 설정

1. pjt 대충 설명 

2. 배운 내용

3. 요구 사항

4. 어려웠던 점

5. 후기
   
   그 외에 어떤 함수 썻는지, 어떤 방법 쓰니까 좋았는지, 헷갈리는 거, 실패한 코드와 그 이유, 기타 등등 전부 작성

### 질문

style 태그는 head 에 넣는게 일반적인가? Y

form 태그 : 내가 가진 정보를 어딘가로 보내는 태그, enter을 입력하면 내가 입력한 정보가 전송됨, action이 비어있으면 내 현재 위치로 

css 하다가 모르겠는 경우 : 임시로 class="test" 한 뒤 test에 이것저것 넣어서 판단,

    크롬 켜서 f12 눌러서 확인

`border: 5px dashed yellow;` 이런거 적어서 경계, 컨텐츠크기 등 파악

일반 형제 결합자 : `A ~ B{ color: red;}` A 부모 벗어나기 전까지의 B에 설정

인접 형제 결합자 : `A + B{ color: red;}` A 바로 다음의 B에 설정

bootstrap에서 대체 width-75 쓰면 justify-content-center 안되는 이유가 뭐지?
