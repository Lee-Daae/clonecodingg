from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # 유저객체가 사라질때 이 프로필도 없어지게
    nickname = models.CharField(max_length=20, unique=True, null=True)

#upload_to='profile/' 는 media 밑에 profile/링크 설정하는 의미
    image = models.ImageField(upload_to='profile/', null=True) # 이미지를 받아서 서버에 저장되는 경로

    message = models.CharField(max_length=100, null=True)
    