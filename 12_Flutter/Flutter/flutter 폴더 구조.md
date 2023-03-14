# directory structure 구조

기초

- presentation : 위젯, state, 컨트롤러 등 ui와 관련
- application : services (api 요청 등)
- domain : 모델
- data : 앱의 데이터를 처리



layer-first

- 설명

  - 상단에 presentation, application, domain, data 등을 띄우고, 그 안에 기능을 작성

- 장점

  - 코드의 재사용성

  - 각 레이어를 기준으로 테스트 가능 

- 단점

  - 앱 성장 시 확장이 잘 되지 않음
  - 한 기능이 다른 레이어에 걸쳐 있으면, 다른 프로젝트로 넘어가야 하기 때문에 번거롭다.
  - 기능 삭제 시, 관련된 모든 레이어에 접근해서 삭제해야 한다.

feature-first

- 설명
  - 각 기능을 상단에 띄우고, 각 기능마다 presentation, application, domain, data 을 작성
- 장점
  - 코드 추적이 쉬움. 기능과 관련한 코드를 한 곳에서 볼 수 있음
  - 유지보수가 쉬움. 기능 추가/삭제 시에도 한 폴더에서 수정 가능
- 단점
  - 코드 중복/의존성 문제가 발생할 수 있음. 여러 기능에서 사용하는 모델/로직을 어디 위치시킬 지 어려움
  - 일관성이 깨질 수 있음. 기능 별 state 관리, api 요청 방식 등이 다르면 코드 일관성이 깨짐



### 참고 자료



[Flutter 확장 가능한 폴더 및 파일 구조 | by 친메이 모랴 | 플러터 커뮤니티 | 보통 (medium.com)](https://medium.com/flutter-community/flutter-scalable-folder-files-structure-8f860faafebd)

[플러터 프로젝트 구조: 기능 우선 또는 레이어 우선? (codewithandrea.com)](https://codewithandrea.com/articles/flutter-project-structure/)



- assets 추가 시 assets 폴더에 추가하고, pubspec.yaml 파일에 assets 경로 추가하기
- lib 폴더 안에 config 폴더 추가
- constants 폴더
  - **api_path.dart:** api 쓸 때 api 의 end point를 여기 저장 (왜?)
  - **assest_path.dart:** 에셋에 대한 상대 경로
  - **app_constants.dart:** 모든 상수 여기 저장
- widgets 폴더
  - 사용자 custom 위젯들 (버튼 등)
- utils 폴더
  - **local_storage_service.dart:** 로컬 저장소에 저장될 데이터에 대한 getter, setter
  - **secure_storage_service.dart:** 사용자 자격 증명, api 토큰, api 키 등을 암호화해서
  - **rest_api_service.dart:** rest api를 호출하고, db에 저장
  - **native_api_service.dart:** 카메라, 사진, 갤러리 등에 접근
  - ui 폴더
    - animations : 사용자 정의 애니매이션
    - api_dialogs.dart : 사용자 지정 모달
    - ui_utils.dart : 사용자 정의 위젯
- bloc 구조
  - 디자인 패턴. 확장에 용이
  - 어려움. 나중에 하기



