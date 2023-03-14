# 0. Basic Data Types

class



- string

- bool

- int
  - num 클래스를 상속받음

- double

object

- num
  - num으로 선언한 경우 int, double 둘 다 가능



# 1. Lists

맨 마지막 줄에 `,` 붙이면 자동으로 줄 정렬 해줌

장점

- collection if
  - if 로 존재할지 안할지 모르는 변수 
  - 로그인 여부에 따라 버튼 표시할 때 사용
- collection for
  - 코드를 줄여줌
  - 이후 설명

```dart
void main() {
	var numbers = [1, 2, 3, 4];
    List<int> numbers2 = [1, 2, 3, 4];		// 클래스를 다룰 때는 이렇게 선언하기로 약속
    numbers.add(1);
    
   // collection if
   	var giveMeFive = true;
    var ifFive = [1, 2, 3, 4, if(giveMeFive) 5];
   // 이것과 같음
    // if (giveMeFive) {ifFive.add(5);}
    
}
```



# 2. String Interpolation

보간법 (String 안에 변수 넣기)



```dart
void main() {
  var name = 'name';
  var age = 10;
  var greeting = 'hello, my name is $name and i am ${age + 10} years old.';
  
  print(greeting);
}
```



# 3. Collection for



```dart
void main() {
  var oldFriends = ['a', 'b'];
  var newFriends = ['c', 
                    'd', 
                    'e', 
                    for (var friend in oldFriends) "new $friend"
                   ];
  
  print(newFriends);
  
  
}

```



# 4. Maps

python 의 딕셔너리 느낌

다양한 메서드들을 사용 가능

class로 표시하기 더 편한 경우도 존재. 이 경우는 구분

```dart
void main() {
  var player = {
    'name': 'name',
    'xp': 20,
  };
  
//   이 경우, player은 Maps<String, Object> 꼴 (이유 : 'name', 20 두 종류가 있어서)
  
//   이렇게 빈 map도 생성 가능
  Map<int, bool> player1 = {
    
  };
  
  Map<List<int>, bool> player2 = {
    
  };
    
  List<Map<String, Object>> playeer3 = {
      {'name': 'name', 'xp': 20'}.
  }
  
}

```



# 5. Sets



```dart
void main() {
  var numbers = {1, 2};
  Set<int> numbers1 = {1, 2};
  numbers.add(3);
}
```

