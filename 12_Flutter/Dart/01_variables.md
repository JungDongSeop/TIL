

# 0. hello world



dart에는 반드시 main 함수가 필요하다 (다른 많은 함수들처럼)



```dart
void main() {
    print('hello world');
}
```



이 때, `;`를 붙이는 것은 매우 중요하다.

dart는 자동적으로 `;`를 붙이지 않는다. (이후 `;`를 잘 써야 하는 상황이 존재)

모든 코드를 main() 안에 쓰는 것 잊지 말기



# 1. var keyword

```dart
void main() {
  var name = 'aaa';
  name = 'bbb';
  String name2 = 'ccc';
}

```

var로 선언하더라도 string을 boolean으로 바꾸는 등의 행위는 할 수 없다.



var & 타입 명시

- 관습적으로, 함수나 메서드 내부에 지역 변수를 선언할 때는 var 사용
- class에서 변수나 프로퍼티를 할 때는 타입 명시



# 2. Dynamic type

dart는 개발자 친화적 언어라, 규칙에 약간의 자유가 존재 => dynamic

여러 타입을 가질 수 있는 변수에 쓰는 키워드 (일반적으로는 잘 사용 x)

```dart
void main() {
  var name;				// dynamic name;이라고 써도 됨
  name = 'aaa';
  name = 12;
  print(name);
}
```

flutter나 json을 같이 쓸 경우처럼 type을 모를 때 쓰면 좋을지도..?

but 필요할 때만 써야함



```dart
void main() {
  dynamic name;
  if(name is String){
    name.isEmpty;
  }
}
```

이런 식으로 하면 String의 다양한 메서드들을 마음대로 사용 가능



# 3. Nullable Variables

개발자가 null 값을 참조할 수 없도록 하는 것 (런타임 에러 발생)





```dart
//Without null safety:
bool isEmpty(String string) => string.length == 0;

main() {
    isEmpty(null)
}
```

=> 런타임 에러 발생 (NoSuchMethodError)

- null에는 .length라는 메서드가 없으므로



해결법 : null값이 가능함을 반드시 명시 (일반적으론 not nullable)

```dart
//
void main() {
  String? name = 'name';		// null 값도 가능
  name = null;					// String name = 'name' 으로 했으면 여기서 error
  // name.length;				// 여기서 error (null은 length 메서드가 없으므로)
  if (name != null) {
      name.isNotEmpty;
  }
  name?.isNotEmpty;				// 위의 조건문을 이처럼 줄일 수도 있음
}
```



# 4. Final Variables

수정할 수 없는 변수 설정

```dart
void main() {
    final name = 'name';	// 수정 불가능
}
```



# 5. Late Variables

late 수식어 (final or 데이터 타입 앞에 선언)

- 한 번만 할당할 수 있는 변수
- api 작업 시 자주 사용

```dart
void main() {
    late final String name;
 	// api 받아오기 등 코드 실행
    
    // print(name);				// 에러. 값을 넣기 이전에는 접근 불가능
    name = 'name';
    print(name);
}
```

초기 수식어 없이 변수 선언 가능 (final을 이후 천천히 결정 가능)



# 6. Constant Variables

dart의 const는 js, ts의 const와 다름 (이것들은 final과 비슷)

- const는 compile-time constant를 만들어 줌
- 즉, 컴파일 할 때 알고 있는 값에 사용 가능함 (api key는 컴파일 할 때 알고 있음. api로 받아오는 데이터는 컴파일 할 때 모름)



앱에서 사용할 상수들은 이렇게 선언하자

```dart
void main(){
    const API = '21g21griqe';
    
    // ...
    
    // const data = fetchAPI(); 		// 에러
    final API = fetchAPI();
    
    
}
```



