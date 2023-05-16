

## 위젯



### state 대신 쓸 만한 것

[ValueListenableBuilder](https://api.flutter.dev/flutter/widgets/ValueListenableBuilder-class.html)

- 참조하고 있는 값이 바뀌면, 자동으로 다시 빌드를 진행함

FutureBuilder

- http 응답, 저장소에서 이미지 가져오기 등 1회성 응답에 사용

StreamBuilder

- 위치 업데이트, 음악 재생, 스톱워치 등 일부 데이터를 여러 번 가져올 때 사용

- setState 를 쓰지 않고도 UI 업데이트 가능, 항상 스트림의 최신값을 가져옴

  

### UI 관련

Expanded

- 자식 부모로써 사용. 
- 부모 요소를 전부 채우도록 UI 구성

Flexible

- 부모 요소로써 사용.
- 자식 부모가 부모 요소에 맞도록 확대 or 축소



InkWell

- 버튼 누를 시, 터치 부분에 잉크가 퍼지는 듯한 애니메이션 제공



Stack

- Container, Column 과 다르게, Stack 안의 childern들은 겹친 상태로 UI 표시
- 위치를 직접 정해야 하므로, Positioned 위젯을 활용

ClipRRect

- 네모난 위젯을 강제로 둥근 모서리를 갖도록 변경



Hero

- 애니메이션을 매우 쉽게 적용 가능

AnimatedContainer

- 컨테이너 속성을 변경할 경우, 보기 좋게 애니메이션 효과를 적용해 줌 (점점 작아진다던가, 모서리가 둥글어 진다거나)
