# REST API 사용

1. `$ pip install djangorestframework` 해서 설치 받은 뒤 requirements 에 올리기

2. settings.py - INSTALLED_APP 에 `'rest_framework',` 추가

3. 모델 만들고 migrate, admin 관리자 만들어서 임의로 데이터 추가, settings.py 연결

4. 프로젝트 urls.py 에 아래처럼 앱 연결

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/v1/', include('music.urls')),
   ]
   ```

5. serializer.py 만든 뒤 아래처럼 작성

   ```python
   from rest_framework import serializers
   from .models import Artist, Music
   
   class ArtistListSerializer(serializers.ModelSerializer):
   
       class Meta:
           model = Artist
           fields = ('id', 'name',)
   ```

   ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공

   - Model 정보에 맞춰 자동으로 필드 생성
   - serializer 유효성 검사기 자동 생성

4. views.py 에

   ```python
   from rest_framework.response import Response
   from rest_framework.decorators import api_view
   from rest_framework import status
   from django.shortcuts import get_object_or_404, get_list_or_404
   
   from articles.serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
   from .models import Article, Comment
   
   @api_view(['GET', 'POST'])
   def article_list(request):
       
       if request.method == 'GET':
           # articles = Article.objects.all()
           articles = get_list_or_404(Article)
           serializer = ArticleListSerializer(articles, many=True)
           return Response(serializer.data)
   
       elif request.method == 'POST':
           serializer = ArticleSerializer(data=request.data)
           if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
           # return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
   
   ```

   article_list 함수

   - GET 요청인 경우 모든 기사의 정보를 JSON으로 응답
     - get_list_or_404 함수는, 올바른 요청인 경우 리스트 (전체 목록. Article.objects.all() 과 같은 역할) 를 전달하고, 올바르지 않은 요청이면 404 에러 발생
     - many=True 속성의 경우 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize 하면 many=True 를 작성해야 함
   - POST 요청인 경우
     - ArticlsSerializer 은 단일 객체를 처리하기 위해 만든 클래스
     - 이전까지의 ArticleForm 과 같다
     - raise_exception 속성은 에러가 난 경우 에러 발생 (추가로 주석 부분을 적을 필요 없어짐)

5. postman 다운받아서 연결 되는지 확인

6. 이제 전부 작성해 보자

7. serializer.py 에

   ```python
   from rest_framework import serializers
   from .models import Article, Comment
   
   class ArticleListSerializer(serializers.ModelSerializer):
   
       class Meta:
           model = Article
           fields = ('id', 'title', 'content',)
       
   class CommentSerializer(serializers.ModelSerializer):
   
       class Meta:
           model = Comment
           fields = '__all__'
           read_only_fields = ('article', )
   
   
   class ArticleSerializer(serializers.ModelSerializer):
       # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
       comment_set = CommentSerializer(many=True, read_only=True)
       comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
   
       class Meta:
           model = Article
           fields = '__all__'
           # readonly 로 comment_set, comment_count 를 사용하면 안됨
           # Meta 안에는 해당 속성이 없기 때문에
   
   
   ```

   List 가 들어간 클래스들은 전체 목록을 위한 클래스, 아닌 것들은 각 객체를 보기 위한 클래스

   CommentSerializer 클래스에서 article 컬럼은 외래키로 받아서 사용할 것이기 때문에, 입력을 받으면 안된다. 그러니 read_only_fields 로 해서 이후 views.py 에 `serializer.save(artist=artist)` 식으로 저장

   comment_set 은 해당 기사의 전체 댓글을 보기 위한 변수. read_only 속성은 이후 serializer.save()를 할 때 저 값이 비어있어 NOT NULL 오류를 일으키기 때문. 이전에는 save(commit=False) 를 하면 됐지만, serializer는 그게 안됨.

   comment_count 은 댓글의 개수를 보기 위한 변수. source 속성은 IntegerField를 채울 값? 역참조한 데이터이므로 comment_set 으로 역참조매니저 사용

8. views.py 에

9. ```python
   from rest_framework.response import Response
   from rest_framework.decorators import api_view
   from rest_framework import status
   from django.shortcuts import get_object_or_404, get_list_or_404
   
   from articles.serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
   from .models import Article, Comment
   
   
   @api_view(['GET', 'POST'])
   def article_list(request):
       
       if request.method == 'GET':
           # articles = Article.objects.all()
           articles = get_list_or_404(Article)
           serializer = ArticleListSerializer(articles, many=True)
           return Response(serializer.data)
   
       elif request.method == 'POST':
           serializer = ArticleSerializer(data=request.data)
           if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
           # return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
   
   
   @api_view(['GET', 'DELETE', 'PUT'])
   def article_detail(request, article_pk):
       # article = Article.objects.get(pk=article_pk)
       article = get_object_or_404(Article, pk=article_pk)
   
       if request.method == 'GET':
           serializer = ArticleSerializer(article)
           return Response(serializer.data)
   
       elif request.method == 'DELETE':
           article.delete()
           return Response(status=stauts.HTTP_204_NO_CONTENT)
   
       elif request.method == 'PUT':
           serializer = ArticleSerializer(article, data=request.data)
           if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response(serializer.data)        
   
   
   @api_view(['GET'])
   def comment_list(request):
       if request.method == 'GET':
           # comments = Comment.objects.all()
           comments = get_list_or_404(Comment)
           serializer = CommentSerializer(comments, many=True)
           return Response(serializer.data)
   
   
   @api_view(['GET', 'DELETE', 'PUT'])
   def comment_detail(request, comment_pk):
       # comment = Comment.objects.get(pk=comment_pk)
       comment = get_object_or_404(Comment, pk=comment_pk)    
       if request.method == 'GET':
           serializer = CommentSerializer(comment)
           return Response(serializer.data)
   
       elif request.method == 'DELETE':
           comment.delete()
           return Response(status=stauts.HTTP_204_NO_CONTENT)
   
       elif request.method == 'PUT':
           serializer = CommentSerializer(comment, data=request.data)
           if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response(serializer.data)        
   
   
   @api_view(['POST'])
   def comment_create(request, article_pk):
       # article = Article.objects.get(pk=article_pk)
       article = get_object_or_404(Article, pk=article_pk)
       serializer = CommentSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           serializer.save(article=article)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
   
   ```

10. 
