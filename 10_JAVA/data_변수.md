`'`은 문자, `"`은 문자열로 나뉘어 취급함



변수 선언

- ```java
  public class tmp {
      public static void main(String[] args) {
          int number;
          number = 3;
          System.out.println(number);
      }
  }
  ```



산술연산자

- `/` : 몫 출력 (`7/2 === 3`, `7/2.0 === 3.5`)
- 실수형이 정수형으로 바뀌면, 소수점 아래는 버림



데이터 타입

정수

- byte, short, int, long

실수

- float, double (float는 `3.0f`, double은 `3.0` 식으로 작성)

문자열

- 바꾸기
  - `stringName.replaceAll("바꿀 문자열, 새 문자열")`
- 자르기
  - `stringName.substring(a, b)`
  - 끝위치 b는 미작성 가능



사용자 입력

- `Scanner`

- ````java
  import java.util.Scanner
      
      
  ....{
      ....{
          Scanner scanner;
          scanner = new Scanner(System.in);
          String input = scanner.nextLine();
          System.out.pringln(input);
      }
  }
  ````

  

- `next()`

- 띄어쓰기 단위로 구분

- `배가 고프다`를 입력하면, `input == 배가`, `input2 == 고프다`

  ```java
  import java.util.Scanner;
  
  ....{
      ....{
          Scanner scanner = new Scanner(System.in);
          String input = scanner.next();
          String input2 = scanner.next();
      }
  }
  ```

- `parseInt()`

- 숫자를 입력받고 싶을 땐 입력된 문자열 `input`에 대해 `Integer.parseInt(input)` 식으로 사용



예외 처리

- `try catch`

- ```java
  try {
      예외 발생 가능성이 있는 코드
  } catch (Exception e) {
      예외 발생 시 실행될 코드
  }
  ```



조건문

- if

- ```java
  if (조건문) {
      실행
  } else if (조건문) {
      실행
  } else {
      실행
  }
  ```

- switch 

- ```java
  switch (month) {
      case 1:
          실행;
          break;
      case 2:
          실행;
          break;
      ...     
  }
  ```

   이 때 `break`를 안붙이면, case 1일 때 아래의 모든 코드도 실행됨. 우리가 원하는 건 else if처럼 작동하는 것.



반복문

- for

- ```java
  for (int i = 0; 실행조건; i 변화할 코드) {
      조건 코드
  }
  ```

- while

- ```java
  while (실행 조건) {
      실행 코드
  }
  ```

- do-while

- ```java
  do {
      실행 코드
  } while (실행 조건);
  ```

  do 부분을 한 번 실행하고, while 조건이 참이면 다시 do 실행

- 



배열 

- 선언

- `String[] days = {"월", "화", "수"}`

- for - each 문

- ```java
  for (String day : days) {
  	System.out.println(day)
  }
  ```

-  배열에 값 추가

- ```java
  String[] days = {"월", "화", "수"}
  
  String[] days2 = Arrays.copyOf(days, 4);
  days2[3] = "목"
  ```

  copyOf(배열, 길이)

- 배열 통으로 출력

- ```java
  System.out.println(Arrays.toString(days))
  ```

- 2차원 배열

- ```java
  String[][] days = {
      {"1", "2"},
      {"3", "4"}
  }
  ```



메서드

- 종류
  - input, output 존재 여부에 따라 4종류



컬렉션

- 배열과 비슷

- List

- ```java
  import java.util.List;
  import java.util.Collections
  
  ....{
      ....{
          List<Integer> list1 = new ArrayList<>();
          List<Integer> list2 = bew ArrayList<Integer>();
          ArrayList<Integer> list3 = new ArrayList<>();
          
          list.add("치킨", "족발");
          list.remove(0);
          list.set(0, "피자");
          Integer pick = list.get(0);
          boolean containsChicken = list.contains("치킨");
          
          Collections.sort(foods);
          Collections.reverse(foods);
          Collections.shuffle(foods);
          
          //배열을 리스트로
          List<String> names = Arrays.asList("a", "b", "c")
      }
  }
  ```

  Int 같은 원시 자료형을 사용하지 않기 때문에, Integer을 사용해야함

- set (집합)

- ```java
   import java.util.Set;
  
  ....{
      ....{
          Set<String> myFavoriteFoods) = new HashSet<>();
          
          myFavoriteFoods.add("치킨");
          myFavoriteFoods.add("피자");
          
          myFavoriteFoods.remove("치킨");
      }
  }
  ```

  메서드 `size()`, `isEmpty()`



Map

- 연관성이 있는 데이터들을 묶어 표현하는 방법

- ```java
  import java.util.HashMap;
  import java.util.Map;
  
  ....{
      ....{
          Map<String, String> dictionary = new HashMap<>();
          dictionary.put("chicken", "닭");
          
          dictionary.get("hippo");  // 찾기
          
          dictionary.remove("chicken");
          
          dictionary.keys();
          dictionary.values();
          
          Set<Map.Entry<String, String>> entries = dictionary.entrySet();
          for (Map.Entry<String, String> entry : entries) {
              String english = entry.getKey();
              String korean = entry.getValue();
          }
      }
  }
  ```

- 



추천 메서드

1. Arrays.sort() - 이 메서드는 객체 또는 프리미티브 배열을 정렬하는 데 사용됩니다. 배열을 인수로 받아 오름차순으로 정렬합니다.
2. String.toCharArray() - 이 메서드는 문자열을 문자 배열로 변환하는 데 사용됩니다. 각 문자가 별도의 요소인 문자 배열을 반환합니다.
3. Math.max() 및 Math.min() - 이 메서드는 두 숫자 사이의 최대값과 최소값을 찾는 데 사용됩니다. 그들은 두 개의 인수를 취하고 각각 더 크거나 작은 값을 반환합니다.
4. String.indexOf() - 이 메서드는 문자열에서 지정된 문자 또는 하위 문자열의 인덱스를 찾는 데 사용됩니다. 지정된 문자 또는 하위 문자열이 처음 나타나는 인덱스를 반환합니다.
5. StringBuilder.append() - 이 메서드는 StringBuilder 개체의 끝에 문자열을 추가하는 데 사용됩니다. 문자열을 인수로 사용하여 StringBuilder 객체의 끝에 추가합니다.
6. HashMap.put() 및 HashMap.get() - 이 메서드는 각각 HashMap에 키-값 쌍을 추가하고 HashMap에서 값을 검색하는 데 사용됩니다. put() 메서드는 키와 값을 인수로 받아 HashMap에 추가합니다. get() 메서드는 키를 인수로 사용하고 해당 값을 반환합니다.
7. Collections.sort() - 이 메서드는 객체 또는 프리미티브 목록을 정렬하는 데 사용됩니다. 목록을 인수로 받아 오름차순으로 정렬합니다.
8. Arrays.binarySearch() - 이 메서드는 정렬된 배열에서 값을 검색하는 데 사용됩니다. 배열과 값을 인수로 사용하고 값이 있으면 값의 인덱스를 반환하고 없으면 음수 값을 반환합니다.
