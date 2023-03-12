Dart의 특징

1. UI 최적화
2. 생산적
3. 모든 플랫폼에 적용
   - dart-web : dart를 js로 변환
   - dart-native : dart 코드를 CPU의 아키텍쳐에 맞게 변환 (데탑, 리눅스 등 거의 모든 곳)
   - 어떻게 컴파일되나? JIT (dart VM) & AOT (ahead of time)
     - 컴파일(내가 짠 코드를 기계어로 번역) 시 시간이 오래 걸림
     - 버튼 변경할 때마다 모든 부분을 컴파일하는 것은 비효율적
     - 이 때 JIT (just in time) 컴파일러를 사용하면, 바로 바뀐 결과를 확인 가능 (가상머신에서 작동 중. 개발 중에만 사용)
     - 배포 시에는 dartVM 사용 x. ARM으로 컴파일
4. null safty
   - 프로그램을 안전하게 해줌



Flutter가 dart를 택한 이유

- 피드백이 빠르면서 (JIT) 최종 앱 컴파일이 빠름(AOT)
- 둘 다 구글이 만듬 (flutter에 필요하면 dart 언어 자체를 수정 가능)
