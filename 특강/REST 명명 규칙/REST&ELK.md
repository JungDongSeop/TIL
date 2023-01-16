# RESTful

### 특징

Client-Server 구조

- 클라이언트와 서버는 서로 독립적
- 클라이언트는 URIs 리소스만 알아야 한다.



Stateless

- 클라이언트의 모든 요청에는 현재 요청에 대한 것만 가지고 있어야 한다.



Cacheable

- 



Uniform interface

- 규격화 (URI만 봐도 이해되도록)



Layered system

- REST는 다중 계층 구조 (그냥 tree 형태라 생각)



### 명명 규칙

1. 소문자 사용
2. 언더바 대신 하이픈 사용
3. 마지막에 슬래시 포함 x
4. 행위는 포함하지 않는다 (delete 하는 행위 등은 url에 넣지 말고, DELETE 요청으로)
5. 파일 확장자는 URI에 포함시키지 않는다
6. (선택) 가급적 전달하고자하는 자원의 명사를 사용하되, 컨트롤 자원을 의미하는 경우 예외적으로 동사 허용
7. 영어는ㄴ 복수형으로 작성 (개념적 tree 구조)





# ELK

elasticsearch + logstash + kibana