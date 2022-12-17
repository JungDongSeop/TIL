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

- 안그러면 그냥 인스턴스 메서드로 들어감

- 클래스 메서드는 인스턴스 변수나 메서드 아예 안쓰는 메서드 작성 시 사용

dictionary는 sequence가 아님

.

dictA.get('key') 할 때 key가 없으면 None 반환

.

path parameter

- 중괄호 안에 들어갈 단어?
- ? 뒤 Query String
- ?api_key=___
- &language=en_US (아니면 en_UK, ko_KR 등등 골라서)
- 이렇게 경로를 만들어서 request 하면 됨

responses

- 200 : 성공
- 404 : 요청한 주소 존재하지 않음
- 401 : 인증받지 않은 유저 (api key 없을 때)

python requests 사용법

```python
import requests

url = 'https://api.agify.io/?name=jun'
response = requests.get(url)        # response는 dict, list 등 제공된 데이터 형태
requests.get(url).json()
```

- url 예시 : [https://www.agify.io/movie.{movie_id}](https://www.agify.io/movie.%7Bmovie_id%7D)

- api_key 필요

- 회원가입 후 api_key 신청, 발급, 그 key값 저장해둔 뒤 계속 사용

- notion 공용 문서에 발급받는 방법 설명 나옴

인터넷 rest api 로 데이터 받는 법

```python
URL = 'https://api.agify.io' # base url

params = {                    # query string 
    'name': 'michael',
    'country_id': 'KR',
}

response = requests.get(URL, params=params).json()
```

- html : CSS 선택자에 마우스 올리면 명시도? 순서도? 나타남
- bootstrap 에서 d-flex는 부모의 class에 부여, 그 후 정렬하고 싶은거 생기면 임의로 부모 만든 뒤 justify~ 작성
- 이미지 크기 조절은 `<a>`에서 `style="width: 30px"`, `<img>`에서 `class="img-fluid"`
- 이미지 간격 조절은 `<a>`에서 `class="mx-3"`



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



# git branch 사용법



#### branch

실습

- init, add, commit 하기. 이후엔 만들어진 commit이 분화됨
- 브랜치 만들기 : `git branch {브랜치 명}`
- 브랜치 목록 보기 : `git branch`
- 브랜치 삭제 : `git branch -d {브랜치 명}`
- 브랜치 작업공간으로 이동 : `git switch {브랜치 명}`
  - 작업 공간 이동 시, Working Directory의 파일들도 해당 가지에 맞게 나타남
  - 해당 작업 공간에서 add, commit

브랜치 안에서 push 할 때는 `git push -u origin {브랜치명}`

#### merge

나뉜 branch들을 하나로 합치는 명령어

`git merge {브랜치 명}`

병합 종류

- 

- 브랜치 합치기
  - master 브랜치 공간으로 이동
  - `git merge viktor`, 브랜치 명 입력해서 합침
  - `git log --oneline --graph` 치면 그림으로 이해 가능



#### Fork

원격 저장소 소유권이 있는 경우 => `Shared repository model`

원격 저장소 소유권이 없는 경우 => `Fork & Pull model`

실습

- 소유권이 없는 원격 저장소를 fork를 통해 내 원격 저장소로 복제
- 복제된 내 원격 저장소를 로컬 저장소에 clone
- 로컬 저장소, 원본 원격 저장소를 동기화 (`git remote add upstream {원본 url}`)
- 브랜치 생성, 코드 작성
- 복제 원격 저장소에 해당 브랜치 push
- Pull Request 요청
- 이후 사용자는 master로 switch, master에서 pull 해서 모두 같은 폴더 받기



# 새로  git 설정하는 방법

- git clone <원하는 url>
- 이후 git add, commit, push 하면 로그인 창이 뜸?
- 이게 맞나? 아니었다. 

  `git config --global --lsit` 해서 내 이름 확인
  
  ```
  -- 사용자 이름을 선택하여 삭제
  git config --global --unset user.name 사용자이름
  -- 전체 사용자 이름 삭제
  git config --global --unset-all user.name
  -- 사용자 이메일을 선택하여 삭제
  git config --global --unset user.email 사용자이메일
  -- 전체 사용자 이메일 삭제
  git config --global --unset-all user.email
  -- 사용자 이름, 이메일 추가
  git config --global user.name 사용자이름
  git config --global user.email 사용자이메일
  ```
  
- 윈도우 자격 증명 관리자 가서 git 설정 다 됐나 확인
