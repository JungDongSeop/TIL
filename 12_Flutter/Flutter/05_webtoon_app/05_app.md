# 0. introduce

api, 데이터 받아오기, 데이터 폰에 저장하기, 화면 이동하기 등



# 1. AppBar

위젯을 key를 가지고, 식별하기 위한 Id를 가진다.



# 2. Data Fetching

services 폴더 만들고, `api_service.dart` 파일 만들기

라이브러리 설치 (`pub.dev`)

- `flutter ~~` 작성하거나
- `pubspec.yaml` 파일에 직접 작성 (이름과 버전만 적고, 우상단 다운로드 버튼 누르면 자동 설치 됨)

`api_service.dart`

```dart
import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:toonflix/models/webtoon_model.dart';

class ApiService {
  final String baseUrl = "https://webtoon-crawler.nomadcoders.workers.dev";
  final String today = "today";

  // api 보내는 함수. 비동기라서 Futer 데이터형
  Future<List<WebtoonModel>> getTodaysToons() async {
    // 웹툰 목록 저장할 리스트
    List<WebtoonModel> webtoonInstances = [];
    final url = Uri.parse('$baseUrl/$today');
    // 데이터 받아오기
    final response = await http.get(url);
    // 코드가 200이면, Json을 클래스로 형성 후 webtoon model로 만듦
    if (response.statusCode == 200) {
      // json을 클래스로 바꾸는 함수 jsonDecode
      final List<dynamic> webtoons = jsonDecode(response.body);
      // 모든 웹툰 목록에 대해, webtoonInstances에 저장
      for (var webtoon in webtoons) {
        final toon = WebtoonModel.fromJson(webtoon);
        webtoonInstances.add(toon);
      }

      return webtoonInstances;
    }
    throw Error();
  }
}

```

api 사용

```dart
import 'package:flutter/material.dart';
import 'package:toonflix/screens/home_screen.dart';
import 'package:toonflix/services/api_service.dart';	// 여기에 api 함수 있음

void main() {
  ApiService().getTodaysToons();						// api 실행
  runApp(const App());
}
```





# 3. from Json

json 항목 하나하나를 클래스로 만들고, json 전체를 클래스로 만들어진 리스트를 만듦

models 폴더 안에 `webtoon_model.dart` 파일을 만듦



`webtoon_model.dart`

```dart
class WebtoonModel {
  final String title, thumb, id;

  // named construtor 사용 (명명된 생성자).
  // 변수명 json은 이후 api에서 받아올 예정
  WebtoonModel.fromJson(Map<String, dynamic> json)
      : title = json['title'],
        thumb = json['thumb'],
        id = json['id'];
}

```

`api_service.dart`

```dart
import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:toonflix/models/webtoon_model.dart';

class ApiService {
  final String baseUrl = "https://webtoon-crawler.nomadcoders.workers.dev";
  final String today = "today";

  Future<List<WebtoonModel>> getTodaysToons() async {
    List<WebtoonModel> webtoonInstances = [];
    final url = Uri.parse('$baseUrl/$today');
    final response = await http.get(url);
    if (response.statusCode == 200) {
      final List<dynamic> webtoons = jsonDecode(response.body);
      for (var webtoon in webtoons) {
        webtoonInstances.add(WebtoonModel.fromJson(webtoon));
      }
      return webtoonInstances;
    }
    throw Error();
  }
}
```



# 5. waitForWebToons

Future 데이터 출력하기

fetch를 state에 저장하기 (간단한 방법)



# 6. FuterBuilder



state 없이 ui 변형시키기

```dart
import 'package:flutter/material.dart';
import 'package:toonflix/models/webtoon_model.dart';
import 'package:toonflix/services/api_service.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key});

  Future<List<WebtoonModel>> webtoons = ApiService.getTodaysToons();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 2,
        backgroundColor: Colors.white,
        foregroundColor: Colors.green,
        title: const Text(
          "어늘의 웹툰",
          style: TextStyle(
            fontSize: 24,
          ),
        ),
      ),
      // API 받아오기를 statefulWidget에서 할 필요 없이 만드는 위젯
      body: FutureBuilder(
        future: webtoons,
        builder: (context, snapshot) {
          // context는 화면 class 등이 저장된 곳
          // snapshot은 Future의 상태를 저장해 두는 곳 (데이터를 받았는지, 오류인지 등)

          // 데이터 값이 참이면 '성공' 표시, 아니면 로딩 중 화면 표시
          if (snapshot.hasData) {
            return const Text("data connected!");
          }
          return const Text("lodaing...");
        },
      ),
    );
  }
}

// state 사용 방식. 이후 더 좋은 widget 사용 가능. (그 위젯은 StatelessWidget에서도 사용 가능)
// FutureBuilder라는 widget
  /*
  List<WebtoonModel> webtoons = [];
  bool isLoading = true;

  void waitForWebToons() async {
    // await : 이게 끝날 때까지 기다림. 이게 끝나면 로딩이 완료된 것
    webtoons = await ApiService.getTodaysToons();
    isLoading = false;
    // state 변경. setState가 작동하면, 화면 구성을 다시 실행 (아래의 build 실행)
    setState(() {});
  }

  // init state
  @override
  void initState() {
    super.initState();
    // 데이터 받아오는 함수 호출. 여기서 api 요청을 보낼 예정
    waitForWebToons();
  }
  */
```



  # 6. ListView

많은 값을 표현할 때는 row, column 보다 listView 추천

ListView.builder 을 쓰면, 화면에 보이는 것들만 렌더링해서 메모리를 아낄 수도 있음. 가로 스크롤 같은 것도 가능

```dart
import 'package:flutter/material.dart';
import 'package:toonflix/models/webtoon_model.dart';
import 'package:toonflix/services/api_service.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key});

  Future<List<WebtoonModel>> webtoons = ApiService.getTodaysToons();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 2,
        backgroundColor: Colors.white,
        foregroundColor: Colors.green,
        title: const Text(
          "어늘의 웹툰",
          style: TextStyle(
            fontSize: 24,
          ),
        ),
      ),
      // API 받아오기를 statefulWidget에서 할 필요 없이 만드는 위젯
      body: FutureBuilder(
        future: webtoons,
        builder: (context, snapshot) {
          // context는 화면 class 등이 저장된 곳
          // snapshot은 Future의 결과값. 즉 상태를 저장해 두는 곳 (데이터를 받았는지, 오류인지 등)

          // 데이터 값이 참이면 '성공' 표시, 아니면 로딩 중 화면 표시
          if (snapshot.hasData) {
            // 이렇게 웹툰 목록을 반환하면, 항상 모든 데이터를 로딩해서 비효율적. ListView.builder 사용
            /*
            return ListView(children: [
              for (var webtoon in snapshot.data!) Text(webtoon.title)
            ]);
            */

            // ListView.builder은 화면에 나타나지 않는 데이터를 메모리에서 삭제함.
            // ListView.separated 는 Listview.builder 사이사이의 데이터에 widget을 출력함
            return ListView.separated(
              scrollDirection: Axis.horizontal, // 세로로 스크롤
              itemCount: snapshot.data!.length, // 전체 데이터 개수
              itemBuilder: (context, index) {
                // print(index); 를 찍어보면, 항상 10개 전후의 데이터만 로딩됨을 알 수 있음
                var webtoon = snapshot.data![index];
                return Text(webtoon.title);
              },
              separatorBuilder: (context, index) {
                return const SizedBox(width: 10);
              },
            );
          }
          return const Center(
            child: CircularProgressIndicator(), // 로딩 화면
          );
        },
      ),
    );
  }
}

```



# 7. Webtoon Card

부모 요소를 건드리려면 clipBehavior 사용



```dart
  // 웹툰 카드 제작
  ListView makeList(AsyncSnapshot<List<WebtoonModel>> snapshot) {
    return ListView.separated(
      scrollDirection: Axis.horizontal, // 세로로 스크롤
      itemCount: snapshot.data!.length, // 전체 데이터 개수
      padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 20),
      itemBuilder: (context, index) {
        var webtoon = snapshot.data![index];
        return Column(
          children: [
            Container(
              width: 250,
              clipBehavior: Clip.hardEdge,
              decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(15),
                  boxShadow: [
                    BoxShadow(
                      blurRadius: 15,
                      offset: const Offset(10, 15), // 태양의 위치를 바꾼다 생각
                      color: Colors.black.withOpacity(1),
                    )
                  ]),
              child: Image.network(
                webtoon.thumb,
                // 아래 헤더는 403 오류 관련. https://gist.github.com/preinpost/941efd33dff90d9f8c7a208da40c18a9 참조
                headers: const {
                  "User-Agent":
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                },
              ),
            ),
            const SizedBox(
              height: 10,
            ),
            Text(
              webtoon.title,
              style: const TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
        );
      },
      separatorBuilder: (context, index) {
        return const SizedBox(width: 40);
      },
    );
  }


```



# 8. 새 스크린으로 이동

터치 인식 : `GestureDetector`



탭하면 이동하는 코드

```dart
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) =>
                DetailScreen(title: title, thumb: thumb, id: id),		// 이동할 화면 위젯
          ),
        );
        // route : 이동할 위젯을 애니메이션으로 감싸는 등에 필요한 변수
      },
      child: Column(...)

```



# 9. Hero

화면 전환 시 Hero 위젯을 사용하면 애니메이션 사용 가능

사용법 : 같은 tag만 달아주면 됨



# 10. 웹툰별 에피소드 api





```dart
  // 상세 웹툰의 회차에 대한 api 받아서 넣기
  static Future<List<WebtoonEpisodeModel>> getLatestEpisodesById(
      String id) async {
    List<WebtoonEpisodeModel> episodesInstances = [];		// 에피소드 목록들 저장할 리스트
    final url = Uri.parse('$baseUrl/$id/episodes');
    final response = await http.get(url);

    if (response.statusCode == 200) {
      final episodes = jsonDecode(response.body);
      for (var episode in episodes) {
        episodesInstances.add(WebtoonEpisodeModel.fromJson(episode));
      }

      return episodesInstances;
    }
    throw Error();
  }
```





# 12.  Future



DetailScreen 클래스 (statelessWidget) 에서 웹툰 id별 클래스 생성자 만들 시, 변수 id를 사용할 수 없음

```dart
	// 클래스 생성자는 그저 해당 클래스 안에서의 생성만 하기 때문에 불가능
	// Future<WebtoonDetailModal> webtoon = ApiService.getTodaysToons(id);

```

어떻게 해결하나? statefulWidget 에서 state를 써서 해결. (widget.id 식으로)

```dart
class DetailScreen extends StatefulWidget {
  final String title, thumb, id;

  const DetailScreen({
    super.key,
    required this.title,
    required this.thumb,
    required this.id,
  });

  @override
  State<DetailScreen> createState() => _DetailScreenState();
}

class _DetailScreenState extends State<DetailScreen> {
  late Future<WebtoonDetailModal> webtoon;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    webtoon = ApiService.getToonById(widget.id);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(...)
```



api에서 비동기로 리턴하는 Future 를 build 할 때는 `FutureBuilder` 사용

```dart
// detail_screen.dart 에서
			  // 웹툰 상세 정보
              FutureBuilder(
                future: webtoon,
                .....
```





# 17. 좋아요 기능

휴대폰 저장소에 정보를 저장하기 위해선, `pub.dev`에서 `shared_preferences` 설치
