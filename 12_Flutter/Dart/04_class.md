# 0. Class

다른 언어와의 차이에 대해서도 주의

class 에서 property를 정의할 때는 type 선언

```dart
class Player {
//   String name = 'aa';
  final String name = 'aa';   // name 변경 불가능
  int xp = 15;
  
  
//   클래스 안의 메서드
  void sayHello() {
    print('Hi, i am $name');    //dart에서는 this.name이라고 쓰지 않는 것을 권장
  }
}

void main() {
  var player = Player();
  print(player.name);
//   player.name = 'bb';
  print(player.name);
}
```





# 1. Constructors

뜻 : 생성자 함수

class 에서 name, age 등의 property 에 인자로 받은 값을 할당 가능

새로운 player 생성

```dart
class Player {
//   이렇게도 작성할 수 있음. 아래 코드가 더 효율적
  
//   late final String name;   // name 변경 불가능
//   late int xp;
  
//   Player(String name, int xp){
//     this.name = name;
//     this.xp = xp;
//   }

  final String name;   // name 변경 불가능
  int xp;
  
  Player(this.name, this.xp); 
  
  //   클래스 안의 메서드
  void sayHello() {
    print('Hi, i am $name');    //dart에서는 this.name이라고 쓰지 않는 것을 권장
  }
}

void main() {
  var player = Player('aa', 15);
  player.sayHello();
  var player2 = Player('bb', 20);

}
```





# 2. Named Constructor Parameters

위 방식은 class가 커질 때 불편 (positional argument)

```dart
class Player {
  final String name;
  int xp;
  
  Player({required this.name, required this.xp});      // 이런 방식으로 하면 아래 방식처럼 인자를 선언해야 함
  
  //   클래스 안의 메서드
  void sayHello() {
    print('Hi, i am $name'); 
  }
}

void main() {
  var player = Player(name: 'aa', xp: 15);
  player.sayHello();
}
```



# 3. Named Constructor

`:`을 써서 class의 argument와 property를 일대일 초기화하는 생성자를 만들 수 있음

```dart
class Player {
  final String name;
  int xp, age;
  String team;
  
  Player({required this.name, required this.xp, required this.age, required this.team});  
 
//  클래스를 초기화하는 메서드
//   Player 객체를 parameter + 기본값 들로 초기화
//   named 방식
  Player.createBluePlayer({
    required String name, 
    required int age,
  }) :  this.age = age, 
        this.name = name,
        this.team = 'blue',
        this.xp = 0;
  
//   더 간단히 작성
//   positional 방식
  Player.createRedPlayer(String name, int age) :
    this.age = age,
    this.name = name,
    this.team = 'red',
    this.xp = 0;
  
  void sayHello() {
    print('Hi, i am $name'); 
  }
}

void main() {
  var player = Player.createBluePlayer(
    name: 'aa',
    age: 21,
  );
  var player = Player.createRedPlayer('bb', 21,);
}
```





# 4. Recap

json을 class로 바꾸는 연습

```dart
class Player {
  final String name;
  int xp;
  String team;
  
//   나만의 방식으로 데이터 처리
  Player.fromJson(Map<String, dynamic> playerJson) :
    name = playerJson['name'],
    xp = playerJson['xp'],
    team = playerJson['team'];
  
  void sayHello() {
    print('Hi, i am $name'); 
  }
}

void main() {
  var apiData = {
    {
      'name': 'aa',
      'team': 'red',
      'xp': 0,
    },
    {
      'name': 'aa',
      'team': 'red',
      'xp': 0,
    },    
    {
      'name': 'aa',
      'team': 'red',
      'xp': 0,
    }
  };
  
//   이부분 문법이 특이하다
  apiData.forEach((playerJson) {
    var player = Player.fromJson(playerJson);
    player.sayHello();
  });
}
```



# 5. Cascade Notation



```dart
class Player {
  String name;
  int xp;
  String team;
  
  Player({required this.name, required this.xp, required this.team});  
 
  void sayHello() {
    print('Hi, i am $name'); 
  }
}

void main() {
//   이런 방식으로 선언 후 변경도 가능하지만
  
//   var aa = Player(name: 'aa', xp: 10, team: 'red');
//   aa.name = 'bb';
//   aa.xp = 100000;
//   aa.team = 'blue';
  
//   이런 방식의 cascade 가 더 간단
  var aa = Player(name: 'aa', xp: 10, team: 'red')
    ..name = 'bb'
    ..xp = 100000
    ..team = 'blue'
    ..sayHello();

}
```



# 6. Enums

enums 타입은 실수를 예방할 수 있음 (단순 오타 등)

- 선택의 폭을 좁히는 역할

```dart
enum Team { red, blue }   // 문자열로 x

class Player {
  String name;
  int xp;
  Team team;
  
  Player({required this.name, required this.xp, required this.team});  
 
  void sayHello() {
    print('Hi, i am $name'); 
  }
}

void main() {
  
//   이 때 String으로 준 경우 team: 'redd' 같은 오타를 예방
  var aa = Player(name: 'aa', xp: 10, team: Team.red);

}
```





# 7. Abstract method

추상화 클래스 (파이썬의 클래스 상속)

- 객체를 생성할 수 없음
- 다른 클래스들이 직접 구현해야 하는 메서드들을 모아놓은 청사진
- 수많은 청사진에 메서드의 이름과 반환 타입만 정해서 정의할 수 있음

자주 사용하진 않지만 유용함

```dart
abstract class Human {
  void walk();
}


enum Team { red, blue }

// Human 클래스를 상속
class Player extends Human{
  String name;
  int xp;
  Team team;
  
  
  Player({required this.name, required this.xp, required this.team});  
  
  void walk() {
    print('im walking');
  }
 
  void sayHello() {
    print('Hi, i am $name'); 
  }
}

// Human class를 상속, 이 안의 walk)() 메서드를 상속받아서 사용
class Coach extends Human {
  void walk() {
    print('coach is walking');
  }
}


void main() {
  
}
```





# 8. Inheritance

클래스 상속

```dart
class Human {
  final String name;
  Human({required this.name});		// constructor
  void sayHello() {
    print('hi im $name');
  }
}

enum Team {red, blue}

class Player extends Human {
  final Team team;
  
//   named argumant를 쓰기
//   super을 써서 name을 전달해주면 이 클래스를 전달한 name과 함께 호출하게 된다
//   super은 확장한 부모 클래스를 의미. 여기선 Human
  Player({
    required this.team,
    required String name
  }) : super(name: name);  
  
//   부모 클래스의 메서드 재사용
  @override
  void sayHello() {
    super.sayHello();
    print('and I play in ${team}');
  }
}

void main() {
  var player = Player(team: Team.red, name:'aa');

  player.sayHello();
}
```





# 9. Mixins

생성자가 없는 클래스

클래스에 프로퍼티들을 추가할 때 등에 사용

- 특히 하나의 프로퍼티 등을 재사용 할 때
- with로 연결된 클래스의 메서드 등을 사용 가능

extends vs with

- extends 
  - 확장한 그 클래스는 부모 클래스가 됨
  - 자식 클래스는 `super`을 사용해 부모에 접근, 그 순간 자식은 부모 클래스의 인스턴스가 됨
- Mixin
  - 내부의 프로퍼티와 메서드만 가져옴
  - 그저 뺏어옴
  - 조건 : 생성자가 없는 클래스일 것

```dart
class Strong {
    final double strenghtLevel = 15;
}

// 다른 클래스들의 메서드와 프로퍼티를 가져옴
class QuickRunner with Strong, QuickRunner{
    void runQuick() {
		print('run!');
    }
}

class Tall {
    final double height = 2;
}

class Player with Strong, QuickRunner, Tall {
    
}
```

