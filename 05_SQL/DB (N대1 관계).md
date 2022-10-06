## RDB 관계

- 1:1 

  - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련

- N:1

  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련

    ex. 고객 한 명이 여러 개의 물품을 주문하는 경우

- N:N

  - 양쪽 모두 N:1 관계



### 외래 키 (Foreign Key)

- RDB에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 1개의 키에 해당, 이는 참조되는 측 테이블의 기본 키 (Primary Key)임
- 특징
  - 키를 사용하여 부모 테이블의 유일한 값을 참조
  - 데이터 무결성을 위해 반드시 유일한 값이어야 함 (참조 무결성)

참고. 데이터 무결성에는 (개체 무결성, 참조 무결성, 범위 무결성) 이 있다.



## N:1 (Comment-Article)

0개 이상의 댓글을 1개의 게시글에 작성



### Django Relationship fields

종류

- OneToOneField()
- ForeignKey() :heavy_check_mark:
  - N:1 관계를 담당하는 Django의 모델 필드 클래스
  - 필수 위치 인자 2개 (참조하는 model class, on_delete 옵션)
- ManyToManyField()



### Comment Model

정의

- articles/models.py 에서 models.Model 을 상속받은 Comment 클래스 정의
- 이 때 외래키 필드는 작성 위치와 관계없이 필드의 마지막에 저장
- 인자 on_delete
  - 외래 키가 참조하는 객체가 사라졌을 때 어떻게 처리할 지 정의
  - 데이터 무결성을 위해서 매우 중요한 설정
  - 옵션
    - CASCADE : 부모 객체가 삭체됐을 때, 이를 참조하는 객체도 삭제
    - 기타 PROTECT, SET_NULL, SET_DEFAULT, ...
- 실습
  - makemigrations 진행 (models.py 에 수정 사항이 발생했으니)
  - migrate 진행

### 관계 모델 참조

- Django에서 만든, N:1 or M:N 관계 설정 시 역참조할 때 사용하는 manager를 생성
  - 이전에 모델 생성 시 objects라는 매니저를 통해 queryset api를 사용했던 것처럼, 관계 모델을 통해 queryset api를 사용할 수 있게 됨
- 역참조
  - 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것 (N:1에서 1이 N을 참조)
- 실습
  - Article 모델이 Comment 모델을 참조할 때 사용하는 메시지 만들기
  - article.comment 형식으로는 댓글 객체 참조 X
  - 대신 comment_set manager 를 자동으로 생성해 article.comment_set 형태로 댓글 객체 참조
  - 교재 p46

### Comment 구현

CommentForm 클래스 작성

CREATE

- 이 때 class Meta 에 `fields = '__all__'` 하면, 댓글창에서 글의 종류를 선택할 수 있게 되어버림
- 우리는 특정 게시글 아래에 그 게시글에 대한 댓글만을 다는 기능을 구현하고 싶으니, CommentForm 에서 `exclude = ('article', )` 로 해둠
- `save(commit=False)`
  - 아직 DB에 저장되지 않은 인스턴스를 반환. (create, but don't save the new instance)
  - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용

READ

- 특정 article에 있는 모든 댓글을 가져온 후, context에 추가

  detail 함수에 `comments = article.comment_set.all()` 추가한 뒤, context에도 추가

- 아니면 그냥 html 에 바로

  ```html
      {% for comment in article.comment_set.all %}
          <p>{{ comment.content }} - {{ comment.created_at }}</p>
      {% endfor %}
  ```

  해도 됨

### Comment 추가 사항
