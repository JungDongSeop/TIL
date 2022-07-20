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

# 조건문

```python
if 조건:
    running code
else:
    running code
```

조건 표현식

```python
ㅍtrue인 경우 값 if 조건 else false인 경우 값
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

# 함수

사용 이유 : decomposition(분해), abstraction(추상화)  => 결국엔 **재사용성**

구조

- define & call

- input                         `parameter : 정의할 때 변수, argument : 호출할 때 변수`
  
  positional arguments : 함수 호출 시 위치에 따라 함수에 전달되는 arguments
  
  keyword arguments : 함수 호출 시 직접 변수의 이름으로 특정 argument에 전달
  
  default arguments values : 함수 설정 시 미리 값을 정해 놓은 argument 
  
     `print()의 end = '\n' 등`
  
  가변 인자              `*arg, list로 여러 개의 인자를 받을 때`
  
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

# 

# 모듈
