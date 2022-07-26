# 개념 구조화

### 프로그래밍 => 프로그램을 만드는 행위

    프로그램 : 명령어들의 모임

#### 프로그래밍 언어

    컴퓨터는 기계어를 사용, 기계어의 대안으로 사람이 이해하는 언어인 프로그래밍 언어 사용

- 소스 코드 : 프로그래밍 언어로 작성된 프로그램

- 번역기
  
  소스 코드를 기계어로 번역
  
  - 인터프리터  : 한 줄씩 번역 (python)
  
  - 컴파일러 : 통째로 번역

# 파이썬 특징

1. 배우기 쉬움

2. 인터프리터

3. 객체 지향 프로그래밍 

# 개발 환경 종류

- IDE
  
  통합 개발 환경  (VS code, Pycharm 등)
  
   기능
  
      1. 줄 바꿈 : `Alt + 화살표`
  
      2. 줄 복사 : `Alt + shift + 화살표`
  
      3. 단어 교체 : `Ctrl + D`

- Jupyter Notebook
  
  소스 코드와 함께 실행 결과와 마크다운 저장 가능

- IDLE

# 코드 작성법

## 코드 스타일 가이드

- PEP8 `python 공식 가이드라인`

- 들여쓰기는 `space`, `tab`혼용 금지 (`space` 권장)

- 주석
  
  - 코드를 잘 이해할 수 있도록
  
  - 가독성을 저해할 정도로 무분별한 사용 x  

## 변수

- 추상화 (변수를 사용해야 하는 이유)
  
  - 가독성 증가, 의미 단위 작성 가능, 수정 용이

- 식별자 (첫글자 숫자 x, 키워드 x, 내장함수 x, 모듈명 x)

### 연산자

- +, -, \*, /, //, \*\*

---

# 자료형

1. Boolean
   
       Falsy : False는 아니지만 False로 취급 `0, 0.0, (), [], {}`
   
       논리 연산자 단축 평가 : 결과 확실한 경우 두 번째 값 확인 x, 그냥 첫 번째 값 반환

2. Numeric
   
   1. Int
   
   2. Float
      
      부동 소수점 때문에 다른 값이 나올 수 있음
      
      해결책 : 입실론보다 작은 걸 확인 or math 모듈 활용
   
   3. Complex

3. String
   
   1. escape sequence
      
      \\n, \t, \0, \\\, ...
   
   2. %-formatting
      
      ```python
      score = 4.5
      print('내 성적은 %d' % score)     # 내 성적은 4
      ```
   
   3. str.format()
      
      ```python
      name = 'Kim'
      score = 4.5
      print('Hello, {}! score is {}', format(name, score)
      ```
   
   4. f-string
      
      ```python
      name = 'Kim'
      score = 4.5
      print(f'Hello, {name}! score is {score}')
      ```

    4. None

### 컨테이너

- 여러 개의 값 저장 (list)

- 순서가 있다 vs 순서가 없다
1. 시퀀스형
   
   1. 리스트
   
   2. 튜플
   
   3. 레인지

2. 비시퀀스형
   
   1. 세트
   
   2. 딕셔너리

---

# 조건문

```python
if 조건:
    running code
else:
    running code
```

조건 표현식

```python
true인 경우 값 if 조건 else false인 경우 값
```

# 반복문

while, for 문 (for 문의 in 뒤에는 iterable만 가능)

참고

- 순회할 수 있는 자료형(iterable) :  `string, list, dict, tuple, range, set 등`

- 순회형 함수 `range, enumerate`

list comprehension

```python
list_1 = [i ** 3 for i in range(1, 4)]        #list comprehension
dict_1 = {i : i ** 3 for iin range(1, 4)}    # dictionary comprehension
```

반복 제어

- break            `break가 있는 반복문만을 끝`

- continue       `곧바로 다음 반복을 수행`

- for_else

- pass

---

# 함수

사용 이유 : decomposition(분해), abstraction(추상화)  => 결국엔 **재사용성**

구조

- define & call

- input                         `parameter : 정의할 때 변수, argument : 호출할 때 변수`
  
  positional arguments : 함수 호출 시 위치에 따라 함수에 전달되는 arguments
  
  keyword arguments : 함수 호출 시 직접 변수의 이름으로 특정 argument에 전달
  
  default arguments values : 함수 설정 시 미리 값을 정해 놓은 argument 
  
     `print()의 end = '\n' 등`
  
  가변 인자              `*arg, list로 여러 개의 인자를 받을 때`  **인자들을 tuple로 처리**
  
  가변 키워드 인자 `**kwarg, 몇 개의 키워드 인자를 받을지 모르는 함수 정의할 때,                              dictionary로 묶여 처리`

- docstring(문서화)    `주석으로 코드 내용을 문서로써 정리`

- scope(범위)               `L E G B   (Local socpe, Enclosed scope, Global scope, Built-in scope 순으로 이름(식별자)를 찾아나감`
  
     global, nonlocal

- output

기본 내장함수

```python
map(function, iterable)        
filter(function, iterable)
zip(*iterable)                # 여러 iterable을 모아 tuple을 원소로 하는 zip object 반
lambda[parameter]:표현식
```

---

# 모듈

##### 모듈

    다양한 기능을 하나의 file 로

            코드를 .py 단위로 작성

            `import module`

            `from module import `

            `from package import module`

            `from package.module import var, function, Class`

##### 패키지

    다양한 file을 하나의 folder로

            여러 module의 집합

##### 라이브러리

    다양한 package를 하나의 묶음으로

##### pip   ~~~~

    이것들의 관리자

            PyPI 에 저장된 외부 package 들을 설치하도록 도와주는 package 관리 시스템

            `$ pip install SomePackage`

            `$ pip install SomePackage == 1.05`

            `$ pip list`

            `$ pip show SomePackage`

            `$ pip freeze > requirements.txt`        패키지 목록을 관리 및 설치, 패키지를 기록하는 파일의 이름이 requirements.txt

            `$ pip install -r requirements.txt`

##### 가상환경

    패키지의 활용 공간    

            다양한 버전의 프로그래밍 언어 독립적인 package 로 관리 가능

            `$ python -m venv <폴더명>`

            `$ source venv/Scripts/activate`         가상환경 활성화/비활성화

---

# 데이터 구조화

### 메서드

간단 설명 : 클래스 안에 정의된 함수 (즉 객체의 기능)

`데이터 구조.메서드()` 형태로 활용

예시

```python
List.append(10)
String.split()
```

###### python 공식 문서 표기법(배커스-나우르 표기법)

```python
str.replace(old, new[, count])
# old, new는 필수, [,count]는 선택적 인
```

### 문자열

str 타입, 변경 불가능한 **imutable**   

`word = 'ssafy' ; word = 'I'` 하면, 변수 `word`의 메모리 주소 자체가 바뀜

    (아예 단어를 삭제하고 새로 저장)

문자열 조회/탐색 및 검증 메서드

```python
s.find(x)         # x의 첫 번째 위치 반환, 없으면 -1
s.index(x)         # x의 첫 번째 위치 반환, 없으면 오류 발
s.isalpha()        # 알파벳 문자 여부, 단순 알파벳이 아니라 숫자인가 아닌가 판단
s.isupper()        # 대문자 여부
s.islower()        # 소문자 여부
s.istitle()        # 타이틀 형식 여부
```

문자열 변경 메서드

```python
s.replacce(old, new[, count])        # 바꿀 대상 글자를 새로운 글자로 바꿔 반환               
s.strip([chars])                    # 공백 or 특정 문자 제거(양쪽, lstrip은 왼쪽)
s.split(sep = Npne, maxsplit = -1)    # 공백 or 특정 문자를 기준으로 분리, list로 반환                
'separator'.join([iterable])        # 구분자로 iterable을 합침, 중간중간에 seperator로 분리       
    # 문자열 ''.join(iterable) 이니 문자열 메서드임
s.capitalize()                        # 첫 번째 글자를 대문자로
s.title()                            # 공백 다음 알파벳을 대문자
s.upper()                            # 전부 대문자
s.lower()                            # 전부 소문자
s.swapcase()                        # 대 소문자 서로 변경
```

### 리스트

가변 자료형(변경 가능)

리스트 메서드

```python
L.append(x)                # list 마지막에 x 추가
L.insert(i,x)            # list 인덱스 i에 x 삽입 (x가 list 길이보다 크면 맨 뒤)
L.remove(x)                # 가장 왼쪽에 있는 항목(첫번째) x를 제거, 존재하지 않으면 error
L.pop()                    # list 가장 오른쪽 항목(마지막) 반환 후 제거
L.pop(i)                    # list 인덱스 i의 항목 반환 후 제거
L.extend(m)                # 순회형(iterable) m의 모든 항목들을 list 끝에 추가
L.index(x, start, end)    # list 항목 중 가장 왼쪽에 있는 항목 x의 인덱스 반환    
L.reverse()                # list 거꾸로 정렬
L.sort()                    # list 정렬
L.count(x)                # list에서 항목 x의 갯수 반
```

시퀀스형 연산자

```python
[a,b] + [c,d]        # 산술연산자ㅏ
[a,b] * 3             # 반복연산자
```

### 집합

셋 메서드

```python
s.copy()        # set의 얕은 복사
s.add(x)        # set에 항목 x 추가
s.pop()        # set에 랜덤 항목 반환, set이 비어있을 경우 error
s.remove(x)   # set에 항목 x 삭제, 항목이 없으면 error
s.discard(x)  # set에 항목 x 삭제, 항목 없으면 삭제
s.update(t)   # set s에 t의 원소를 합침
s.clear()     # 모든 항목 제거
s.isdisjoint(t) # s와 t의 교집합이 공집합이면 True 반환
s.issubset(t)   # s가 t의 부분집합이면 True 반환
s.issuperset(t) # t가 s의 부분집합이면 True 반환
```

### 딕셔너리

key 는 immutable 데이터만 사용 가능, ordered

value 는 상관없음

```python
d.clear()    # 모든 항목 제거
d.copy()     # d의 얕은 복사본 반환
d.keys()     # d의 모든 키를 담은 뷰를 반환
d.values()   # d의 모든 값을 담은 뷰를 반환
d.items()    # d의 모든 키-값 tuple을 담은 뷰를 반환
d.get(k)     # 키 k의 값을 반환, 없으면 None 반환
d.get(k,v)   # 키 k의 값을 반환, 없으면 v 반환
d.pop(k)     # 키 k의 값을 반환하고 키 k인 항목을 d에서 삭제, 없으면 error
d.pop(k,v)   # 키 k의 값을 반환하고 키 k인 항목을 d에서 삭제, 없으면 v 반환
d.update([other])  # d의 값을 매핑하여 업데이트
```

## 얕은 복사

    <mark>부연설명 : 변수 `a = 1`에서, `a`는 숫자 `1`이 저장된 메모리 주소를 뜻함</mark>

        (박스 안의 내용물이 아닌, 박스의 위치를 저장)

복사방법

1. 할당
   
   대입 연산자 `=`
   
   ```python
   listA = [1,2,3]
   copy_listA = listA
   copy_listA[0] = 'hello'    # 박스의 위치에 접근해서 데이터를 바
           # 이 때 listA = ['hello', 2, 3]
   ```
   
   `=`를 통한 복사는 해당 객체에 대한 객체 참조를 복사 `얕은 복사`

2. 얕은 복사
   
   b는 a와 다른 주소에, a에 대한 내용물을 복사하여 저장
   
   주소 자체가 다르니, 수정해도 값 연동 x
   
   ```python
   a = [1,2,3]
   b = a[:]        # 슬라이싱 사용하면, 다른 주소에 a의 내용물을 복사하여 저장
   b[0] = 5
   print(a, b)    # [1,2,3] [5,2,3]
           # but 1차원에서만 가능 (왜? b[0]이 list면 그 list의 주소를 복사하여
                               # 별도의 메모리에 저장하기 때)
   ```
   
   2차원에서는
   
   ```python
   a = [1,2,['a','b']]
   b = a[:]
   b[2][0] = 0
   print(a,b)  # [1,2,[0,'b']
           # 2차원 값의 주소를 복사해옴
   ```

3. 깊은 복사
   
   이 문제를 해결
   
   ```python
   import copy
   a = [1,2,['a','b']]
   b = copy.deepcopy(a)
   b[2][0] = 0
   print(a,b)   # [1,2,['a','b']] [1,2,[0,'b']]
   ```
