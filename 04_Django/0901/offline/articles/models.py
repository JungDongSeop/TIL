from django.db import models

# Create your models here.
# article table 생성하기 위한 class 하나 정의
class Article(models.Model):
    # 제목과 내용 field (column) 생성
    # schema title Text(50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # print(Article) 했을 때, 문자열이 출력되도록
    # 즉, 인터넷 창에서 이용자가 친 제목이 나오도록
    def __str__(self) -> str:
        return self.title
    