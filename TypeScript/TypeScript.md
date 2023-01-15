https://storm-sun-fa6.notion.site/TypeScript-a5bf7d66b2fe4a34811d9c4ff5c357a0 참조



# TypeScript란?

설명

- javascript에 '정적 타입'이란 요소를 추가한 언어. JS의 상위 집합 (Superset)이다.

- 자바스크립트와 동일한 문법과 특성을 가지며, 거기에 `Type` 요소만 추가된 것이다.
- 브라우저는 타입스크립트 파일을 읽을 수 없다. 브러우저로 작동하려면 컴파일러를 통하여 ts 파일을 js 파일로 변환해 주어야 한다.

배경

- js 는 동적 타입 언어라서, 긴 코드 작성 시 버그가 많이 발생한다.

  - 동적 타입 언어는 아래와 같은 특징을 가진다.

    - 변수 타입 변경 O, js는 개발자의 의도와 관계없이 자동으로 타입이 변경되기도 한다.

    - 에러가 발생해도 프로그램을 실행한다.

      (C, JAVA 등의 정적 타입 언어는 컴파일 시점에 타입 체크를 진행하여, 통과하지 못하면 프로그램 실행을 막는다.)

- 이는 대형 프로젝트에 적합하지 않아, js를 포함하는 상위 집합 typescript가 개발되었다.



# 개발환경 설정

설치

- Node.js를 설치하고, vscode의 터미널 창에 `npm install -g typescript` 실행

사용

- 생성
  - vscode에서 practice.ts 파일을 생성
- ts 파일을 js로 변환
  - 터미널을 열고, `tsc practice.ts` 입력
- 컴파일된 js 파일 실행하기
  - 터미널에 `node practice.js` 입력
- 자동 컴파일 설정하기
  - 매번 `tsc` 명령어 입력할 필요 없이 자동화하기
  - `tsc -w 파일경로` 입력 (watch, 계속 파일을 지켜본다는 의미)



# Type 종류

ts는 타입 변환이 불가능하다.

변수 종류

- ```
  boolean, number, string, object, array, tuple, enum, any, void, null, undefined, unknown, never
  ```

- 

변수 타입선언

- 기본 표기

  - ```typescript
    let name: string;
    let age: number;
    ```

  - 선언한 변수를 다른 타입의 변수값으로 변경하려 하면 오류가 발생

- 타입 추론

  - 타입 선언이 없으면 컴파일러가 타입을 추론

  - ```typescript
    let a = ture;	// boolean으로 판단
    let b = 'hello';// string으로 판단
    
    let name: string = '동섭'		// 되도록 피해서 적기
    ```

  - 마지막 코드처럼, ts 컴파일러가 타입을 유추할 수 있는 것에 중복하여 타입을 지정하는 것은 피하자

- any

  - 모든 타입의 값을 지정할 수 있다.
  - 코드 안전성을 위해 지양

- never

  - 절대 반환하지 않는 함수에 사용

  - 도달되지 않는 코드를 의미

  - 무한루프에 빠지거나 오류를 발생하기 위해 존재하는 함수 등

  - ```typescript
    const neverEx = () => {
        while(true) {
            console.log("함수 실행중");
        }
    }
    ```

  - 위 `neverEx` 함수의 타입은 never이다.

- 유니온타입

  - 하나의 변수에 지정할 수 있는 타입이 여러 개일 때 사용

  - ```typescript
    let a: string | number
    ```

  - string, number 두 종류의 타입 지정이 허용됨

- 커스텀타입

  - type 키워드를 사용하여 새로운 타입을 선언할 수 있다.

  - ```typescript
    type Centimeter = number;
    type Kilogram = number;
    
    type Student = {
        name: string;
        height?: Centimeter;
        weight: Kilogram;
    }
    ```

  - `type Student` 생성. 이 때 `height`는 선택사항



# 배열(Array)

선언

- ```typescript
  let list: number[] = [1, 2, 3]
  ```

  - `number[]` : 배열 타입
  - `number` : 요소 타입
  - `[1, 2, 3]` : 배열 요소

- `any[] = [1, '단어']` 같은 경우도 가능

- 유니온타입 `let dict: (number | string)[] = (1, '숫자 일')` 도 가능 



제네릭 배열

- `Array<Type>` 형태로 선언

- 

  ```typescript
  let str1: Array<string> = ['동섭'];
  let str2: Array<string | number> = ['동섭', 98];	// 유니온 타입
  let str3: typeof str2 = ['동섭', 98]				// 타입 쿼리(type queries) 
  ```

- 타입을 참조할 때는 타입 쿼리를 이용.

- ```typescript
  let arr: Array<() => string> = {() => '사과', () => '딸기'};
  console.log(arr[0]());							// result: '사과'
  ```

- 제네릭 배열 타입은 객체 타입도 지정 가능, 위처럼 익명 함수로도 받을 수 있다.



# 튜플



- `let member: [튜플 타입] = [배열];` 구조로 이루어짐

```typescript
let member: [string, nu]
```



# 객체 타입

js와의 차이

- ts는 객체를 선언할 때 어떤 타입인지 명확하게 정의해야 한다.

객체 선언

- ```typescript
  const student1: object = {};		// 
  const student2 = {}					// any 타입
  ```

- 타입을 선언하지 않으면 `typeof` 연산자에서 any 타입으로 나타남. (any는 object보다 넓은 범위)

옵션 속성

- ```typescript
  const cat: { type: string, age?: number } = {
      type: 'Persian'
  };
  cat.age = 2;
  ```

- 선택적 속성 (`?`)을 사용하면 해당 필드는 객체 생성 때 비워두고, 이후 값을 추가할 수 있다.

인덱스 시그니처

- ```typescript
  const student: { [index: string]: number } = {};
  
  student.id = 1234;
  student.id = '사과';		// 에러
  ```

- 빈 객체를 만들 때 필드의 자료형을 지정하지 않은 채 인덱스를 사용하면 된다. student라는 객체에 id(string)로 지정하고, 해당 값은 1234(number)로 추가



# 7. 열거형(Enums)



- 비슷한 종류의 아이템들을 묶어서 표현할 수 있는 수단