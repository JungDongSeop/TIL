# 0. State



StatefulWidget

- 상태를 가지고 있음
- 상태에 따라 데이터를 바꾸고, 이를 UI에 표현

카운터 앱 구현

- 클래스 안에 메서드 구현해서 사용



# 1. setState



setState : state에게 값이 바뀌었다고 알려주는 함수 (react와 비슷)

- setState가 실행되어야 build가 재실행되고, UI가 바뀜



# 2. recap



# 3. BuildContext



루트 컴포넌트의 `MaterialApp` 안에 `theme`을 주면 배경, 글꼴, 색상 등을 한번에 실행 가능

- 텍스트는 `textTheme` 등

부모 요소와 대화

- 부모 요소의 theme 안의 myTextLarge 에 접근하는 등, 부모 요소에 접근해야 하는 경우가 존재

- 이 때 buildContext 사용

- `BuildContext context` 에서 context 안에는, 이전 모든 상위 컴포넌트들에 대한 정보가 있음. 빠르게 접근 가능 (위젯 트리에서 위젯에 접근)

- ```dart
  import 'package:flutter/material.dart';
  
  void main() {
    runApp(App());
  }
  
  class App extends StatefulWidget {
    @override
    State<App> createState() => _AppState();
  }
  
  class _AppState extends State<App> {
    @override
    Widget build(BuildContext context) {
      return MaterialApp(
        theme: ThemeData(
          textTheme: const TextTheme(
            titleLarge: TextStyle(
              color: Colors.red,
            ),
          ),
        ),
        home: Scaffold(
          backgroundColor: const Color(0xFFF4EDDB),
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: const [
                MyLargeTitle(),
              ],
            ),
          ),
        ),
      );
    }
  }
  
  class MyLargeTitle extends StatelessWidget {
    const MyLargeTitle({
      Key? key,
    }) : super(key: key);
  
    @override
    Widget build(BuildContext context) {
      return Text(
        'My Large Title',
        style: TextStyle(
          fontSize: 30,
          //context에 접근하는 법  
          color: Theme.of(context).textTheme.titleLarge?.color,
        ),
      );
    }
  }
  ```

- 



# 4. widget lifecycle



`initState`

- 상태 초기화
- build 이전에 작동
- 상태는 직접 `int a = 0` 식으로 초기화 가능한데, 이걸 왜 쓰나?
  - 애초에 많이 안씀
  - 종종 부모 요소를 초기화해야 할 때 사용 (api 등)



`dispose`

- 위젯이 스크린에서 제거될 때 호출되는 메서드
- api 업데이트, 이벤트 리스너로 구독 취소 등 무언가를 취소할 때











