# Vue with DRF

서버란?

- 클라이언트에게 정보와 서비스를 제공하는 컴퓨터 시스템
- 서비스 전체를 제공 == django
- 데이터만 제공 == DRF API

클라이언트란?

- 서버에 적절한 요청을 통해, 서버로부터 반환 받은 응답을 사용자에게 표현하는 기능



# CORS

발생한 일

- 브라우저가 요청을 보내고, 서버의 응답이 도착했지만, 브라우저가 이를 막음
- 보안상의 이유로 브라우저는 동일 출처 정책(SOP)에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한함



SOP

- 동일 출처 정책
- 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식
- 문서를 분리함으로써 공격받을 수 있는 경로를 줄임
- Origin (출처)
  - URL의 Protocol, Host, Port를 모두 포함한 부분



CORS

- 교차 출처 리소스 공유
- 추가 HTTP Header를 사용하여, 웹 어플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제
  - 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 서버에 지정할 수 있는 방법
- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
- CORS policy
  - 교차 출처 리소스 공유 정책
  - 이 policy에 맞춰서 (올바른 CORS Header) 요청



# DRF Auth System

Authentication 

- 인증, 입증
- 사용자가 누구인지 확인하는 행위
- 401 Unauthorized
  - 미승인



Authorization

- 권한 부여, 허가
- 인증이 먼저 필요 (ID가 진짜 사용자인지)
- 403 Forbidden
  - 서버는 클라이언트가 누구인지 알고 있음



settings.py에는 기본적인 인증 절차를 어떠한 방식으로 둘 것인지를 설정해야함

- 우리는 TokenAuthentication 사용
- 모든 상황에 대한 인증 방식을 정의하는 것이므로, 각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식이 필요
  - 이 경우 view 함수마다 (각 요청마다) 다른 종류의 데코레이터 설정



종류

- BasicAuthentication, SessionAuthentication, RemoteUserAuthentication 등
- TokenAuthentication
  - 간단하게 구현 가능, 기본적인 보안 기능, 다양한 외부 패키지(확장성 좋음)
  - 매 요청마다 토큰을 같이 전송
    - `Authorization: Token 9944b~~~` (공백 지키기)
  - 문제점
    - 토큰 생성 시점, 관리 방법, 기능 관리 등
  - Dj-Rest-Auth
    - 회원가입, 인증, 비밀번호 재설정, 사용자 정보 검색, 정보 수정 등을 위한 REST API end point 제공
    - 프로젝트의 urls.py에서 `path('accounts/', include('dj-rest-auth.urls'))` 한줄만 쳐도 accounts/password, login, logout 등 다양한 기능을 사용 가능
    - 회원가입은 없음. 토큰을 생성해서 인증해야하기 때문에
    - dj-rest-auth 공식 문서 참조



실습

- 회원가입 완료 시 Token을 store에서 관리함 (action을 통해 state에 저장)



# DRF Auth with Vue



# DRF-spectacular
