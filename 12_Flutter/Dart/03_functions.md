# 0. Defining a function

화살표 함수 사용 가능

```dart
void sayHello(String name){
  print("hello $name");
}

String sayHello2(String name){
  return "hello $name";
}

String sayHello3(String name) => "hello $name";

void main() {
  sayHello('aa');
  print(sayHello2('aa'));
  print(sayHello3('aa'));
}
```



# 1. Named Parameters

flutter에서 자주 사용

required 는 매우 자주 사용

- 비밀번호 등은 필수이니

null safety 해결이 중요

1. 디폴트 값 주기
2. required 사용

```dart
String sayHello(String name, int age, String country){
  return 'Hello $name $age from $country';
}

// 디폴트 값을 줘야함 (Dart는 null safety가 적용되므로, null일 때 접근 불가능)
String sayHello1({String name = 'name', int age = 99, String country = 'kr'}){
  return 'Hello $name $age from $country';
}

// required modifier (디폴트 안주고 null값 해결. 값을 안주면 에러 )
String sayHello2({
  required String name, 
  required int age, 
  required String country}){
  return 'Hello $name $age from $country';
}

void main() {
  print(sayHello('aa', 12, 'korea'));
  // print(sayHello(age: 12, country: 'korea, 'name: 'aa')); 에러
  print(sayHello1(age: 12, country: 'korea', name: 'aa'));

}

```



# 2. 복습



# 3. Optional Positional Parameters

잘 안씀

```dart
// 나라는 null 이 될 수 있고, 디폴트 값도 적용
String sayHello(
  String name, 
  int age, 
  [String? country = 'korea']
) => 'Hello $name, $age from $country';


void main() {
  sayHello('aa', 2);
}
```



# 4. QQ Operator

`??`

`?=`

그 외 and, or, < 등은 같음

```dart
String capitalizeName(String? name) {
//   이러면 에러 남 (null일 수도 있는데 메서드를 적용해서)
//   name.toUpperCase();
  if (name != null){
    return name.toLowerCase();
  }
  return '익명';
}

String cap(String? name) => name != null ? name.toUpperCase() : '익명';


// QQ operator
String cap2(String? name) => name?.toUpperCase() ?? '익명';

void main() {
  capitalizeName('aa');
  capitalizeName(null);
  
  
//   ??= 사용법
  String? name;
  name ??= 'aa';
  name = null;
  name ??= 'another';
  print(name);
}
```



# 5. Typedef

자료형이 헷갈릴 때 도움이 될 alias를 만드는 방법

간단한 경우에 사용을 추천.

- 복잡한 경우는 이후의 class를 추천

```dart
typedef ListOfInts = List<int>;

// 아래 두 함수는 같음

// List<int> reversedListOfNumbers(List<int> list) {
//   var reversed = list.reversed;
//   return reversed.toList();
// }

ListOfInts reversedListOfNumbers(ListOfInts list) {
  var reversed = list.reversed;
  return reversed.toList();
}

void main() {
  reversedListOfNumbers([1, 2, 3]);
}
```

