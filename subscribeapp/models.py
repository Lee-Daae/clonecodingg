from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


class Subscription(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        # 어떤 유저와 어떤 프로젝트 그 쌍이 가지는 구독 정보가 단 하나가 되도록
        unique_together = ('user', 'project')
