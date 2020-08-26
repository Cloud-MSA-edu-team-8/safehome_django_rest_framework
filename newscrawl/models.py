from django.db import models

# Create your models here.

# 뉴스 데이터
class NewsData(models.Model):
    title = models.CharField(max_length=500)
    link = models.URLField()
    def __str__(self):
        return self.title