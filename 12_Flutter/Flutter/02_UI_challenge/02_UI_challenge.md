대부분이 위젯이다. 

# 1. 

`row`에서는 가로가 `mainAxisAlignment`, `column`에서는 세로가 `mainAxisAlignment`

space를 주기 위해선 `sizebox` 사용

`StatelessWidget`은 화면 변화가 없는 위젯을 만들 때 사용

# 2. 

개발자도구 사용하기

개발자도구 창 열고, 좌상단 보면 요소 선택 가능

container : div 박스



# 3. 

파란줄 어떻게 없애나?

- const로 하기를 추천?

- 몇몇 위젯은 const라서, 선언할 때 const 를 붙이기를 추천

- 근데 그것들을 구분하긴 힘들다

- => ctrl shift P 한 뒤 `open user setting` 해서 setting.json에 아래 작성

  

  ```
  "editor.codeActionsOnSave": {
  	"source.fixAll": true
  },
  ```

  이러면 필요한 곳에 const 자동으로 붙여줌



부모가 무슨 줄인지 알려주는 세팅도 존재



# 4. code actions

코드를 간단하게 리팩토링 해줌

만든 text를 잘라낸 뒤 이를 padding 위젯 안에 넣는 것은 귀찮다

- 전구 클릭, `wrap with padding` 클릭
- 단축키 있음



# 5. 

Error Lens extension 설치 (어디가 에러인지 직관적으로 보여줌)



위젯 재사용하기

- 위젯 만들고, 전구에서 `extract widget` 하면 재사용 가능한 위젯으로 내보내줌

- 직접 해보기

  - `lib` 폴더 안에 `widgets` 폴더 만들고, `button.dart` 파일 만들기

  - 클래스로 위젯 작성

  -  import 해서 사용

  - ```dart
    import 'package:flutter/material.dart';
    
    class Button extends StatelessWidget {
      final String text;
      final Color bgColor;
      final Color textColor;
    
        // 클래스에는 생성자가 필요함을 상기
      const Button({
        super.key,
        required this.text,
        required this.bgColor,
        required this.textColor,
      });
    
      @override
      Widget build(BuildContext context) {
        return Container(
          decoration: BoxDecoration(
            color: bgColor,
            borderRadius: BorderRadius.circular(45),
          ),
          child: Padding(
            padding: const EdgeInsets.symmetric(
              vertical: 20,
              horizontal: 50,
            ),
            child: Text(
              text,
              style: TextStyle(
                color: textColor,
                fontSize: 20,
              ),
            ),
          ),
        );
      }
    }
    ```

  - 



# 7. Icons and Transforms

Icon 을 쓰면 다운받지 않고 다양한 아이콘을 쓸 수 있다.



Transforms를 쓰면 다양한 변화를 줄 수 있다.

- 부모 컴포넌트의 확대 없이 자식 컴포넌트를 크게 하거나 (overflow 되도록)
- 자식 컴포넌트를 물리적으로 몇 픽셀 정도 아래로 가게 하거나 (부모에 영향을 끼치지 않고)
  - `Transforms.translate 에서 offset을 줘서 x, y 축으로 이동
- 튀어나온 부분 잘라내기
  - container에서 `clipBehavior: Clip.hardEdge`



# 8. reusale cards



재사용 가능한 위젯 안에 색깔 등을 변수로 설정하고 싶을 때

- `final _blackColor = const Color(0xFFFFFF);`
- 만약 `_`를 안붙이면, 생성자에서 `blackColor`도 반드시 선언해줘야 한다. 그럴 필요는 없으니



스크롤 기능을 넣을 거면

- body: SingleChildScrollView 위젯 사용

카드 겹치게는 transform 사용



# 9. code challenge

카드 재사용 할때마다 transform을 적절히 사용하는 것은 귀찮다

이를 카드 위젯 안에 잘 넣어보자

