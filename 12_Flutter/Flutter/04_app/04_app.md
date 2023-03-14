# 0. User Interface

flexible, expanded





# 1. Timer

버튼을 누르면 timer가 생성되고 (late), flutter 내부의 Timer 속성 사용 (일정 주기마다 함수가 실행되는 식으로)



# 2. Pause



# 3. date format

1500초를 25분으로 변환 

`split`, `first` 등 여러 개가 섞인 느낌?

```dart
  String format(int seconds) {		// seconds는 1500
    var duration = Duration(seconds: seconds);
    return duration.toString().split(".").first.substring(2, 7);
  }
```

