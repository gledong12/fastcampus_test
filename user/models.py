from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=20)
  type = models.IntegerField() # 0은 사용자 1은 사장님 2는 배달기사