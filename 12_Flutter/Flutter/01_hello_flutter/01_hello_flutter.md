# 1. Installation



단계

SDK 설치 (공식문서 대신 chocolatey 사용 https://chocolatey.org/install#individual)

1. https://chocolatey.org/install 방문

   - Choose How to Install Chocolatey 에서 Individual 선택

   - 작업표시줄의 윈도우 아이콘 우클릭 - `Windows Powershell (관리자)` 클릭

   - **Get-ExecutionPolicy** 입력

   - `Restricted`가 나타나면,  `Set-ExecutionPolicy AllSigned` 또는 `Set-ExecutionPolicy Bypass -Scope Process` 입력

   - ```
     Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
     ```

     입력. 선택창이 나타나면 Y 입력

   - 이후 `choco` 입력해서 chocolatey가 설치되었는지 확인

2. flutter 설치

   - 파워쉘을 닫지 말고, `choco install flutter` 입력. 선택창이 나타나면 Y 입력
   - 명령어 `flutter` 또는 `flutter --version`을 입력해서 에러 메시지 외의 다른 메시지가 나타나면 성공
   - 이 때 `command not found` 에러가 나면, 경로 문제일 가능성이 있음. 
     - `윈도우 검색 - 시스템 환경 변수 편집 - 고급 - 환경 변수 - 시스템 변수` 에서 `Path`를 누르고, flutter가 설치된 위치를 path에 추가 (파워쉘 코드를 읽다 보면 경로를 알 수 있을지도?).
     - 만약 `C:\tools\flutter`처럼 flutter가 설치되어 있으면 path에 `C:\tools\flutter\bin` 을 추가

3. 안드로이드 시뮬레이터 설치

   - https://docs.flutter.dev/get-started/install/windows#android-setup 참고
   - 그냥 적당히 next 눌러가면서

4. 에러 확인

   - 파워쉘에서 `flutter doctor --android-licenses` 입력
   - 이 때 **Android sdkmanager not found. Update to the latest Android SDK and ensure that the** **cmdline-tools are installed to resolve this.** 에러가 나면, 아래 과정 진행
     - https://while1.tistory.com/entry/Flutter-android-sdkmanager-not-found-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0
   - 이후 다시  `flutter doctor --android-licenses`  입력, 이후 선택창에서 계속 y 입력 (동의하기)
   - `All SDK package licenses accepted ` 나오면 동의 완료

5. 그 외에도 여러 에러가 나는데, 각자 검색해서 해결
   - 윈도우 버전 문제는 https://brain-nim.tistory.com/80
   
   







# 1. Dart Pad

dartpad.dev/ 로 가면 설치할 필요 없이 flutter 코드 실행 및 샘플 코드를 볼 수 있다. 



# 2. Running Flutter

