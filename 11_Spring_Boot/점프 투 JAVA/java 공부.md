## 01. 자바란 무엇인가

자바의 특징

- 간단하다
- 객체 지향적이다
- 인터프리터 언어이다.
  - 텍스트 소스(.java) => 컴파일 (.class) => 인터프리트하면서 실행(JVM)
  - 시스템에 무관한 파일을 만듦으로써, 컴파일 언어에 가까운 속도와 독립성을 얻음
- 강력하다
  - 포인터 연산 x => 잘못될 주소 가르칠 가능성 제거
- 안전하다
  - 자료형 타입에 굉장히 민감 => 컴파일만 되면 코드에 문제 발생 x
- 플랫폼 독립적이다.
  - 실행 파일은 이진 코드(클래스) 파일 => 자바 런타임이 설치되어 있으면 어디에서나 실행
- 멀티 쓰레딩
  - 하나의 프로그램 단위가 동일한 쓰레드를 통시 수행
- 동적이다
  - 하나의 모듈을 갱신할 때 다른 모듈을 모두 갱신할 필요가 없다 (인터페이스가 모든 인스턴스 변수와 도구의 실행문을 배제한 채 객체 간의 상호 작용을 정의하기 때문)



자바 시작

1. JDK 설치 (java 개발환경)
2. Intellij 설치 (개발 도구 IDE)
3. 자바소스와 컴파일 (javac 는 java compiler (.class)를 의미)
4. path 설정
5. HelloWorld.java 파일 생성 (클래스명도 HelloWorld로 똑같이 작성)



자바 구조

``` java
public class AAA {
    public static void main(String[] args) {
        System.out.println('HelloWorld')
    }
}

접근제한자 클래스선언 클래스이름 {
    접근제한자 static 반환타입 메서드이름(파라미터) {
        //구현할 코드 작성
    }
}
```



- 접근제한자

  - 클래스나 메서드에 접근할 수 있는 범위를 지정

  - public, private, protected, default


  - private > protected > public 순으로 제한이 많음

- 클래스선언

  - class

  - 객체를 생성하는 틀, 프레임, 공장 개념

- 클래스이름

  - 카멜케이스로 작성

- 메서드, 파라미터, ...

  - main() : 기본 메서드. 자바 프로그램이 실행되면 제일 먼저 메인 메서드를 찾아서 실행. 길게 작성된 소스에서 그 프로그램의 시작이 어딘지 알 수 없으면 안되므로 시작점을 알려주는 용도

  - String : 문자열

  - args : 변수 명. 임의의 이름으로 작성

- 반환할 타입

  - 반환할 값이 없으면 void

- static

  - static으로 선언된 함수나 변수는 자바 버추얼 머신에서 인스턴스 객체의 생성 없이 호출할 수 있다. (객체 생성없이 해당 메서드를 호출해서 쓸 수 있다.)

  - 자바 프로그램을 실해앟면 static으로 지정된 메서드를 먼저 메모리에 할당시킨다.

  - 이후, main으로 이름이 만들어진 메서드가 있는지를 찾아서 그 메서드를 가장 먼저 시작점의 메서드로써 호출을 하게 되는 것





## 02. 자바 시작하기

변수

- 규칙

  - 숫자로 시작 x
  - _, $ 이외의 특수문자 x
  - 자바의 키워드는 변수명으로 사용 x

- 대입

  - ```java
    int a;
    a = 1;
    ```

- 사용자 정의 자료형

  - ```java
    class Animal {
        
    }
    ```

  - 이후 `Animal cat;` 이런 식으로 선언 가능



명명 규칙

- 클래스명
  - 명사, 카멜케이스
- 메서드 명
  - 동사, 시작은 소문자 + 카멜케이스
- 변수 명
  - 짧지만 의미가 있게



주석

- 여러 줄 주석 : `/* */`
- 한 줄 주석 : `//`



## 03. 자료형

### 원시 자료형

특징

- `new` 키워드로 값을 생성할 수 없음. 리터럴로만 값을 세팅 (String은 리터럴로도 표기 가능하지만 원시 자료형은 아님)

숫자

- int, long, float, double, 

불

- true/false

문자

- char `'a', 97(아스키코드), '\u0061' (유니코드)` 전부 동일한 'a'를 가르킴

### 참조 자료형

문자열

- String
- 내장 메서드 (equals, indexOf, contains, charAt, replaceAll, substring, toUpperCase, split)
- 문자열 포매팅 (`System.out.println(String.format('I am %d years', 24))`)
  - 정수 %d, 문자열 %s, 문자 %c, 부동소수 %f
  - `System.out.printf('I am %d years', 24)` 처럼 printf 함수를 사용하면 바로 포매팅된 문자열을 출력 가능

StringBuffer

- ```java
  StringBuffer sb = new StringBuffer();
  sb.append('hello');
  String result = sb.toString();
  System.out.println(result);			// 'hello' 출력
  ```

- 메모리 사용량이 적음, but StringBuffer 자료형은 String보다 무거우니, 여러번 변경 시 사용하는 것이 효율적

- appent, insert, substring

배열(Array)

- 숫자 배열 `int[] name = {1, 2, 3};` 처럼 표시

- 배열의 길이는 고정됨에 주의

  - ```java
    String[] weeks = new String[7];
    ```

- 배열의 길이는 `weeks.length`

리스트(List)

- 크기가 정해져 있지 않다.

- `import java.util.ArrayList`를 import 해야함

- ```java
  import java.util.ArrayList;
  
  public class Sample {
      public static void main(String[] args) {
          ArrayList nums = new ArrayList();
      }
  }
  ```

- 메서드 get, size, contains, remove

- 제네릭스?

- 문자열 리스트에는 String.join 메서드도 존재

- 정렬

  - ```java
    import java.util.Comaprator;
    
    ...
    		args.sort(Comparator.naturalOrder());	// 오름차순 정렬
    ```

맵

- dictionary 와 비슷
- 종류 : Hashmap, LinkedHashMap, TreeMap (뒤 2개는 순서를 가짐)
- HashMap의 메서드 : put, get, getOrDefault, containsKey, remove, size, keySet

집합

- ````java
  import java.util.Arrays;
  import java.util.HashSet;
  
  public class Sample {
      public static void main(String[] args) {
          HashSet<String> set = new HashSet<>(Arrays.asList("H", "i"));
          System.out.println(set);
      }
  }
  ````

- `import java.util.HashSet;` import

- 교집합, 차집합, 합집합 구하는 법은 검색

- 메서드 addAll, remove

- 종루 : HashSet, TreeSet, LinkedHashSet (뒤 2개는 순서를 가짐)

상수집합(Enum)

- 값을 찾을 때 인덱스가 아닌, 변수명 그 자체로 찾아올 수 있음

- ```java
  enum Coffee {
      AMERICANO, CAFE_LATTE		// AMERICANO 변수는 아메리카노를 판 개수
  }
  
  int americano = countSellCoffee(Coffee.AMERICANO); 	// 이런 식으로 사용 가능 
  ```

형변환

- 문자 => 숫자 : `Integer.parseInt(args)`
- 정수 => 문자 : `String.toString(args)`
- 실수 => 문자 : `Double.parseDouble(num)`

final

- 자료형에 값을 단 한번만 설정할 수 있게 강제하는 키워드

- ```java
  ...
      	final int n = 123;
  		n = 456;			// 컴파일 에러
  ```

- 



## 04 제어문

if문

- ```java
  if (조건) {
      ...;
  } else if (조건) {
      ...;
  } else {
      ...;
  }
  ```

switch/case 문

while 문

for 문

for each 문

- ```java
  for (String num:nums) {
      System.out.pringln(num);
  }
  ```



## 05 객체 지향 프로그래밍

