# 

---



RDB

- 관계형 데이터베이스
- 어떤 사람이 물건을 주문한 경우, 사람 DB와 주문 DB를 연결 (보통 primary key로 연결)
- 구조
  - 스키마 (테이블의 구조) (자료의 구조, 표현 방법, 관계 등을 기술한 것)
  - 테이블 (관계 라고도 부름)
    - 필드 (속성, 컬럼)
    - 레코드 (튜플, 행)

RDBMS

- 관계형 데이터베이스 관리 시스템
- RDB 를 업데이트 및 관리하는 시스템
- SQLite, MySQL, PostgreSQL, ...
- 특징
  - 파일 형식으로 넣음, 비교적 가벼움
  - 안드로이드, 맥 등에 기본 탑제
  - 오픈 소스

- 단점
  - 대규모 동시 처리에는 적합하지 않음
- 장점
  - 어떤 환경에서나 실행 가능한 호환성
  - 데이터 타입이 비교적 적고 강하지 않음 -> 유연한 학습
  - django Framework의 기본 DB



## SQL

- RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
- RDBMS에서 DB 스키마 생성 및 수정, 테이블에서 검색 및 관리가 가능



커맨드

1. DDL (데이터 정의 언어)
   - 테이블, 스키마 등을 정의 
   - (CREATE, DROP, ALTER)
2. DML (데이터 조작 언어)
   - 데이터를 조작(추가, 조회, 변경, 삭제)
   - INSERT, SELECT, UPDATE, DELETE
3. DCL (데이터 제어 언어)

​	DDL은 테이블 관련, DML은 데이터 관련

문법

- 모든 SQL문은 SELECT, INSERT 등의 키워드로 시작, 반드시 `;`로 끝남
- 대소문자 구분 X (but 대문자로 작성하는 것을 권장)
- 주석은 --
- 세부 사항은 앞으로 배울 예정
- Statement (문)
  - 독립적으로 실행할 수 있는 코드 조각
  - Clause로 이루어짐
- Clause (절)
  - ex) `SELECT column_name FROM table_name;` 에서 `SELECT column_name`



실습

- .sqlite3 파일 만든 뒤 DDL.sql 파일 생성, 이후 우클릭-use database 해서 둘 연결

#### DDL

데이터 정의, 테이블 구조를 관리

CREATE, ALTER, ...

- CREATE TABLE statement
  - db에 새 테이블을 만듦 (스키마 정의)
  - 이후 그 문에 커서 올리고 우클릭, run selected query 클릭하면 됨

데이터 타입 종류

1. NULL

2. INTEGER

3. REAL

4. TEXT

5. BLOB (그냥 binary 이미지 데이터. ex. 이미지)

   boolean은 그냥 정수 0, 1 로 사용

- 다음 규칙으로 데이터타입 결정
  - 값에 둘러싸는 '' 와 소수점, 지수가 없으면 INTEGER
  - '' 로 묶이면 TEXT
  - 따옴표, 소수점, 지수가 없으면 REAL
  - 따옴표 없이 NULL이면 NULL

- 특징
  - 동적 타입 시스템
    - 데이터에 맞춰서 데이터 타입이 결정됨 (정적인 경우는 데이터 타입에 맞춰서 데이터를 입력받음)
    - 데이터 타입을 지정하지 않아도 데이터를 바로 입력 가능
    - but 호환성 때문에 미리 타입을 정해두는 것이 좋음

타입 선호도

- 특정 컬럼에 저장된 데이터에 권장되는 타입
- SQLite는 비교적 가벼운 엔진이라 데이터 타입이 적지만, 호환성을 위해 정적인 db 엔진과의 호환을 위해 어떤 종류의 데이터 타입을 묶어서 처리
- ex. INT, INT2, INT4, INT8 등을 전부 INTEGER 타입으로 묶음



Constratints (제약)

- 데이터 무결성
  - DB 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두는 것
  - DB의 상태를 일정하게 하고 데이터의 무결성을 유지하기 위함임
- 실습
  - NOT NULL
    - 컬럼이 NULL 값이 되도록 허용하지 않음
  - UNIQUE
    - 컬럼의 모든 값이 고유한 값이 되도록 함
  - PRIMARY KEY
    - 고유성을 식별하는데 사용되는 컬럼
    - 기본적으로 NOT NULL 제약조건
    - INTEGER 타입에만 사용 가능
  - AUTOINCREMENT
    - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
    - 1, 2, 3에서 3 삭제 후 생성 시 1, 2, 4가 되도록 제약 
    - INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
- rowid 특징
  - 테이블을 생성할 때마다 rowid라는 암시적 자동 증가 컬럼이 자동으로 생성
  - 새 행을 삽입할 때마다 정수 값을 자동으로 할당 (1부터 시작)
  - 명시적으로 명령하지 않는 경우, 테이블에서 가장 큰 rowid + 1 값을 생성
  - 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 만들면, 그 컬럼은 rowid 컬럼의 별칭 (alias)이 됨. 즉 고유 키를 원하는 이름으로 사용 가능

ALTER TABLE

- 기존 테이블의 구조를 수정
- rename table, rename column, add new column to a tabel, delete column
- 실습
  - ALTER TABLE table_name RENAME TO new_contacts;
  - ALTER TABLE table_name RENAME COLUMN name TO last_name
  - ALTER TABLE table_name ADD COLUMN name TEXT
    - 기존 데이터가 있을 경우 에러 발생 가능 (이전 데이터는 해당 열에 해당하는 값이 NULL 상태인데, 만약 추가된 컬럼에 NOT NULL이 있으면)
    - => DEFAULT 제약 조건 사용
  - ALTER TABLE table_name 
    - 삭제 못하는 경우
      - 컬럼이 다른 부분에서 참조되는 경우
      - PRIMARY KEY
      - UNIQUE 속성

DROP 

- 데이터 테이블을 제거
- 특징
  - 취소, 복구가 불가능하니 주의해야 한다.
- 실습
  - DROP TABLE table_name
    - 존재하지 않는 테이블 제거 시 오류



### DML

데이터 조작하기 (CRUD)

INSERT, SELECT, UPDATE, DELETE

`CREATE TABLE users ( ..... );`  해서 빈 테이블 만든 뒤, bash 창에 sqlite3 입력해서 켠 다음 아래 코드 실행하면, 원하는 속성을 가진 데이터 임포트 완료

```
sqlite> .open mydb.sqlite3
sqlite> .mode csv
sqlite> .import users.csv users
sqlite> .exit
```



- DML INDEX
  - Simple query
    - select 문을 사용하여 데이터 조회
    - 매우 다양한 절과 함께 사용하기에 복잡하다.
    - 실습
      - SELECT column1, column2 FROM table_name;
  - Sorting rows
    - order by 절을 사용
    - NULL은 제일 작은 값으로 인식
    - 실습
      - SELECT select_list FROM table_name ORDER BY column-1 ASC, column_2 DESC;
  - Filtering data
    - 데이터를 필터링하여 중복제거, 조건 설정 등
    - 실습
      - SELECT DISTINCT 절
      - SELECT DISTINCT select_list FROM table_name;
      - WHERE 절
      - FROM 절 뒤에 작성
      - WHERE column_1 = 10
      - WHERE column_2 LIKE 'KO%'
        - `%`는 0개 이상의 문자를 의미, `_`는 문자 단 1개만 의미
      - WHERE column_3 IN (1, 2)
      - WHERE column_4 BETWEEN 10 AND 20
        - 비교연산자, 논리연산자도 있음
      - LIMIT 10
        - 최대 10개까지만 출력. SELECT 문 맨 뒤에 입력
      - LIMIT 10 OFFSET 10
        - 10번째부터 최대 10개 출력
  - Grouping data
    - 특정 그룹으로 묶인 결과를 생성
    - 선택된 컬럼 값을 기준으로 데이터 (행) 들의 공통 값을 묶은 뒤 표시
    - Aggregate function
      - 집계 함수
      - 데이터의 최대값, 최소값, 평균, 합계, 개수 등을 계산
      - AVG(), COUNT(), MAX(), MIN(), SUM() 등
    - 실습
      - 그룹의 개수 세기
        - SELECT country, COUNT(*) FROM users GROUP BY country;
  - Changing data
