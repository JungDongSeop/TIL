# Today I Learned

---



명령어 bash 창

- sqlite3 치면 되도록 설정 완 (원래는 winpty sqlite3)

- 열기

  .open db.sqlite3

- 표 열기

  - .tables

- 표 만들기

  - 처음엔 CREATE TABLE "테이블 위치" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(50) NOT NULL ...)  `상황 따라 다르게 입력`
  - 나중에 입력할 땐 CREATE TABLE
  - `테이블 이릅 입력`
  - (
  - name TEXT,
  - age INTEGER
  - )
  - ;

  여기까지 하면 `.tables` 칠 때 테이블 제목, `.schema 테이블제목` 칠 때 비어있는 schema 잘 나옴

- 데이터 삽입
  - INSERT INTO students (name, age) values ('김', 3);
  - 이후 확인은
  - SELECT name FROM students;
