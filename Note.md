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
