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
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl = "https://webtoon-crawler.nomadcoders.workers.dev";
  final String today = "today";

  void getTodaysToons() async {
    final url = Uri.parse('$baseUrl/$today');
    final response = await http.get(url);		// await : 이 부분이 처리될때까지 기다려라
    if (response.statusCode == 200) {
      print(response.body);
      return;
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

