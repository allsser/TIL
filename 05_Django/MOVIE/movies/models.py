from django.db import models

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=40)     # 영화명
  title_en = models.CharField(max_length=40)  # 영화명(영문)
  audience = models.IntegerField()            # 누적관객수
  open_date = models.DateField()              # 개봉일
  genre = models.TextField()                  # 장르
  watch_grade = models.TextField()            # 관람등급
  score = models.FloatField()                 # 평점
  poster_url = models.TextField()             # 포스터 이미지 URL
  description = models.TextField()            # 영화 소개


def __str__(self):
  return f'[{self.pk}] {self.title}'