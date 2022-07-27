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

# 

# 객체 지향 프로그래밍

프로그래밍의 패러다임 중 하나, 프로그램을 여러 개의 '객체'들의 모임으로 파악하는 것

각각의 객체는 '메시지'를 주고받고, 데이터를 처리

`객체 = 정보 + 행동 (즉 변수 + 함수)`

기존 방식 : 절차지향 프로그래밍 (global data를 중심으로, 여러 함수들을 거칠 뿐)

                        (중간 함수를 바꾸면 이후의 함수들도 바꿔야 하는 경우가 많음)

        => 데이터와 기능(메서드)의 분리, 추상화, 이후 메서드 간의 상호작용

장점

- 클래스 단위로 모듈화시켜, 많은 인원이 참여하는 대규모 개발에 적합

- 필요한 부분만 수정하기 쉬워, 프로그램의 유지보수가 쉬움

단점

- 설계 시 많은 자원이 듦 (상호 작용 구조를 만드는 게 힘듦)

- 실행 속도가 상대적으로 느림

### 객체

클래스에서 정의한 것을 토대로 메모리에 할당된 것 (변수, 자료 구조, 함수, 메서드 등

    (즉, 속성과 행동으로 구성된 모든 것) (속성`attribute`  + 행동`method`)

python의 모든 것이 객체다

##### 객체의 특징

- 타입(type) : 어떤 연산자와 조작이 가능한가 (문자열끼리 + 가능)

- 속성(attribute) : 어떤 상태 데이터를 가지는가

- 조작법(method) : 어떤 행위(함수)를 할 수 있는가

### 인스턴스

특정 클래스로 만든 객체 (특정 타입의 객체)

    ex) 가수는 클래스다, 아이유는 객체다, 아이유는 가수의 인스턴스다

    `'hi'` : 문자열 타입(클래스)의 인스턴스 (객체)

## 기본 문법

- 클래스 정의     `class MyClass`

- 인스턴스 생성 `my_instance = MyClass()`

- 메서드 호출     `my_instance.my_method()`

- 속성                  `my_instance.my_attribute`

클래스 : 객체들의 분류/설계도    (class)

인스턴스 : 각각의 실체, 객체/예  (instance)

##### 객체 비교하기

- ==
  
  - 동등한(equal), 두 객체가 동등한(내용이 같은) 경우 True, 두 객체가 같아 보이지만 실제로 동일한 대상은 아닐 수 있음

- is
  
  - 동일한(identical), 두 변수가 동일한 객체(주소)를 가리키는 경우

```python
a=[1,2,3];b=[1,2,3]
print(a == b, a is b)         # True False
b = a
print(a == b, a is b)         # True True
```

## 속성

(데이터, 정보, 상태) 즉 변수를 뜻함?

객체 = 정보 + 행동, `정보 = 클래스 변수(공통) + 인스턴수 변수(개인)`

- 인스턴스 변수
  
  - 인스턴스가 개인적으로 갖는 속성, 각 인스턴스의 고유한 변수 (사람 이름 등)
  
  - 생성자 메서드(`__init__` )에서 `self.<name>`으로 정의
  
  - 인스턴스 생성 이후 `<instance>.<name>`으로 접근

```python
class Person:                
    def __init__(self, name):    # (인스턴스 변수)
        self.name = name__

john = Person('john')
print(john.name)        # john    (인스턴스 변수)
```

- 클래스 변수
  
  - 클래스 선언 내부에서 정의
  
  - `<classname>.<name>`으로 접근 및 할당
  
  - 클래스 변수를 변경할 때는 항상 `클래스.클래스변수` 형식으로 변경
    
    인스턴스 변수가 없으면 자동으로 클래스 변수를 찾음

```python
class Circle():
    pi = 3.14        # 클래스 변수
    def __init__(self, r):
        self.r = r    # 인스턴스 변수
c1 = Circle(5)
c1.pi = 5            # 인스턴스 변수 바꿈
Circle.pi = 5        # 클래스 변수 바
print(cq.pi)        # 3.14
print(Circle.pi)    # 3.14
```

## 메서드

특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 함수

    (list 의 모든 객체에서는 append() 사용 가능)

- 인스턴스 메서드
  
      인스턴스 변수 처리    `self`
  
  - 클래스 내부에 정의되는 메서드의 기본
  
  - 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨
    
    - `self` : 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
    
    - 생성자 메서드 : 인스턴스 변수들의 초기값을 설정 (인스턴스 생성, `__init__` 메서드 자동 호출)
    
    - 매직 메서드 : `____`가 있는 메서드, 특정 상황에 자동으로 불리는 메서드
      
      특수한 동작을 하기 위해 만들어짐
      
      인스턴스 메서드의 일종
      
      `ex) __str__ : 해당 객체의 출력 형태를 지정, print() 사용 시 자동호출`
    
    - 소멸자 메서드 : 객체가 소멸되기 직전 호출

- 클래스 메서드
  
  - 클래스 변수 처리   `cls`
  
  - `@classmethod`라는 데코레이터를 사용하여 정의
    
    - 데코레이터 : 
  
  - 호출 시, 첫번째 인자로 클래스(cls)가 전달됨
  
  - ```python
        @classmethod
        def func(cls):
            pass
    ```

- 정적 메서드
  
  - 인스턴스 변수, 클래스 변수 전부 사용 x
  
  - 속성을 다루지 않고 행동만 하는 메서드 정의할 때 사용
  
  - `@staticmethod` 데코레이터 사용하여 정의
  
  - 함수처럼 동작하지만, 클래스의 namespace에 귀속됨

인스턴스와 클래스 간의 이름공간(namespace)

    클래스를 정의하면, 클래스와 해당하는 이름공간 생성

    인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성

    인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

        (`c1.pi` 등에서 인스턴스 변수 설정 안했으면, 클래스 변수 출력)

### 요약

객체 ----  정보  (클래스 변수, 인스턴스 변수)

        ----- 행동   (클래스 메서드, 인스턴스 메서드, 스태틱 메서드)          

## 객체지향의 핵심 4가지

- 추상화
  
  - 복잡한 것은 숨기고, 필요한 것만 표현

- 상속
  
  - 두 클래스 사이 부모-자식 관계를 정립하는 것
  
  - 정보(변수), 행동(함수)를 상속받아 사용 가능
  
  - 상속 관련 함수와 메서드
  
  - - isinstance(object, classinfo)
      
          classinfo의 instance거나 subclass인 경우 True
    
    - issubclass(class, classinfo)
    
    - super()
      
         자식 class에서 부모 class 사용 시, super() 사용하여 호출
  
  - 다중 상속
    
    두 개 이상의 클래스 상속, 중복된 속성이나 메서드는 상속 순서에 의해 결정
  
  - 상속 관련 메서드
    
    mro 메서드 : 해당 인스턴스의 클래스가 어떤 부모 클래스 갖는지 확인하는 메서드

- 다형성
  
  - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음
  
  - 서로 다른 클래스에 속한 객체들이 동일한 메세지에 대해 다른 방식으로 응답
  
  - 메서드 오버라이딩
    
    클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경

- 캡슐화
  
  - 객체 일부 구현 내용에 대해, 외부에서의 직접적인 액세스 차단(정보를 숨긴 채 활용)
  
  - 민감한 정보를 숨기는데 사용
  
  - 접근제어자
    
    - public member
      
      언더바(\_) 없이 시작하는 메서드, 어디서나 호출, override 허용
    
    - protected member
      
      언더바 1개로 시작, (암묵적으로) 부모 클래스 내부와 자식 클래서에서만 호출, 하위클래스 override 허용
    
    - private member
      
      언더바 2개로 시작, 본 클래스 내부에서만 사용 가능, 하위 클래스 상속 및 호출 불가능
  
  - getter, setter 메서드
    
    - getter : 변수의 값을 읽는 메서드, `@property` 데코레이터 사용
    
    - setter : 변수의 값을 설정하는 메서드, `@변수.setter` 사용
  
  - ex) 나이 19세 이하 입력 시 오류 출력, 이런 경우 캡슐화를 써서 ~~ ?
    
    모르겠음

# 에러와 예외 처리

## 디버깅

버그를 없애는 과정

- print() 찍어서 이상한 부분 찾기

- 정상적으로 작동한 이후에 수정한 부분 살펴보기

- 보통 조건/반복, 함수, 제어가 되는 시점에서 문제 발생

- text editor, IDE 에서의 기능 활용 (`breakpoint`, `변수 조회`)

- Python tutor 사용

## 문법 에러

python은 1줄씩 읽어서, 오류가 발생하면 즉시 중지

- `Invalid syntax` : 문법 오류

- `assign to literal` : 잘못된 할당 

- `EOL(End of Line)` :

- `EOF(End of FIle)`

## 예외

실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤

    문장, 표현식이 무법적으로 맞더라도 발생하는 에러 (0으로 나누기 등)

사용자 정의 예외를 만들어 관리할 수 있음 (로그인 안하고 파일 수정 시 에러)

- `ZeroDivisionError`

- `NameError` : namespace상에 이름이 없는 경우 (정의 x)

- `TypeError` : 타입 불일치 (int형과 str형을 더하는 경우 등), argument 개수 초과 등

- `ValueError` : 타입은 맞지만 값이 적절핮 않거나 없는 것

- `IndexError` : 인덱스가 존재하지 않거나 범위를 벗어나는 것

- `KeyError` : dictionary에서 key가 존재하지 않는 경우 (`key()` 사용 시 에러 안 남)

- `ModuleNotFoundError` : 모듈을 찾지 못햇을 때 

- `ImportError` : 모듈을 있으나 존재하지 않는 클래스/함수 가져오는 경우

- `KeyboardInterrupt` : 임의로 프로그램 종료한 경우

- `IndentationEror` : Indentation이 적절하지 않은 경우 (들여쓰기)

##### 파이썬 내장 예외

## 예외 처리

##### try/except

try 문 / except 절을 이용하여 예외 처리

try문 : 예외 발생하지 않은 경우, except 실행 없이 종료

except문 : 예외 발생 시 except 절 실행

반드시 하나 이상의 except 절 있어야함

else : try 문에서 예외가 발생하지 않으면 실행

finally : 예외 상관없이 항상 실행

##### as

에러 메시지 처리(as)

예외를 다른 이름에 대입 `except IndexError as err `
