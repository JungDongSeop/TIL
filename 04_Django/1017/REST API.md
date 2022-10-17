## HTTP

- Request Methods
  
  1. GET
     
     - 서버에 리소스의 표현을 요청
     - 데이터만 검색해야 함
  
  2. POST
     
     - 데이터를 지정된 리소스에 제출 (submit)
     - 서버의 상태를 변경
  
  3. PUT
     
     - 요청한 주소의 리소스를 수정
  
  4. DELETE

- Response status codes
  
  1. infromational responses
  2. successful responses
  3. redirection messages
     - redirect 하라 때
  4. client error responses
     - 클라이언트 잘못
  5. server error responses
     - 서버 잘못

- 웹에서의 리소스 식별
  
  - HTTP 요청의 대상을 리소스(자원)라고 함
  
  - 각 리소스는 URI로 식별됨
  
  - URI
    
    - uniform resource identifier (통합 자원 식별자)
    
    - 인터넷에서 하나의 리소스를 가리키는 문자열
    
    - 예시 : URL (경로), URN (이름, ex.책의 ISBN)
    
    - URL
      
      - uniform resource locator (통합 자원 위치)
      
      - 구조
        
        - https://www.example.com:80/path/to/myfile.html/?key=value#quick-start
        
        - 스키마
          
          - http 등, 브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜
        
        - 권한 authority
          
          - :// 의 뒷부분
          - domain (요청 중인 웹 서버. 즉 IP 주소) 과 port (웹 서버의 리소스에 접근하는데 사용되는 게이트. 생략 가능) 를 모두 포함, 둘은 `:`로 구분됨
        
        - path
          
          - ? 전까지
          - 웹 서버의 리소스 경로
          - 오늘날은 실제 위치가 아닌, 추상화된 형태의 구조를 표현 (create.html 이 아닌 그냥 create 로 표시)
        
        - parameters
          
          - 웹 서버에 제공하는 추가적인 데이터
          - `&` 기호로 구분되는 key-value 구분값
        
        - anchor
          
          - # 이후
          
          - 리소스의 다른 부분에 대한 앵커
          
          - 일종의 리소스 내부 북마크
          
          - 서버에는 # 이전까지만 전송, 브라우저에게 # 이후 부분으로 이동하도록 요철
  
  - ​    URN
    
    - 고유한 이름으로 자원을 식별

## REST API

### API

- application programming interface
- 애플리케이션과 프로그래밍으로 소통
- 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇가지 쉬운 구문을 제공

​    

web API

- 웹 서버 or 웹 브라우저를 위한 API
- 현재 웹 개발은 여러 Open API를 활용하는 추세 (Youtube API, Kakao Map API, ...)
- API는 다양한 타입의 데이터를 응답 (HTML, XML, JSON, ...)

REST

- Representational State Transfer
- API 서버를 개발하기 위한 일종의 소프트웨어 설계 바업ㅂ론
- 암묵적으로 네트워킹 문화에 널리 퍼짐
- REST 원리를 따르는 시스템을 RESTful 하다고 함
- 기본 아이디어 : 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
- 자원 정의, 주소 지정 방법
  - 자원 식별 : URL
  - 자원 행위 : HTTP Method (GET, POST)
  - 자원의 표현 : 마지막에 표현되는 추상화된 결과물, JSON

Response JSON

- 장고가 앞으로는 완성된 페이지가 아닌, JSON 형태로 응답
- 지금까지는 사용자에게 페이지(html) 만 제공. 앞으로는 JSON으로 제공
- 그럼 화면구성은? Front-end Framework (Vue.js) 가 담당. 앞으로 장고는 MTV 중 T를 담당하지 않게 됨 (장고는 백엔드로만 사용)





JsonResponse()를 사용한 json 응답

- safe 옵션 : 같이 주어지는 인자가 딕셔너리가 아니면 False로 설정



ModelSerializer

- 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만드는 shortcut을 제공

- Model 정보에 맞춰 자도응로 필드 생성

- serializer 에 대한 유효성 검사기 자동 생성

- .create(), .update() 등 간단한 기본 구현 포함



api_view 데코레이터

- DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음

- 허용하디 않은 것은 405 Method Not Allowed



게시글 데이터 생성하기



삭제

- DELETE

수정

- PUT



N:1 관계



- 댓글 기능 구현
  
  - 읽기 전용 필드 설정
    
    - read_only_fields 를 사용해 외래 키 필드를 '읽기 전용 필드'로 설정
    
    - 유효성 검사에서는 제외시키고 데이터 조회 시에는 출력하도록 설정



N:1 역참조 데이터 조회

1. 특정 게시글에 작성된 댓글 목록 출력하기
   
   - 기존 필드 override

2. 특정 게시글에 작성된 댓글의 개수 출력하기
   
   - 새로운 필드 추가





### 장고 shortcuts functions

django.shortcuts 패키지는 개발에 도움이 되는 여러 함수와 클래스 제공

- render(), redirect(), get_object_or_404(), get_list_or_404()
