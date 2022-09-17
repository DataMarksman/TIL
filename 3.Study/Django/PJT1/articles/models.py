from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # auto now add 가 created에 붙어있는 것 주의
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 이후 프린트 찍었을때 보는 용도
    def __str__(self):
        return self.title
