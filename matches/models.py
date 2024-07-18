from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    #logo = models.CharField(max_length=255, null=True, blank=True)  # 이미지 URL이나 경로를 저장할 필드
    sport=models.ForeignKey(Sport,related_name='teams', on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
        return self.name
    
class Match(models.Model):
    ourTeam = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    opponentTeam = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateField()
    time=models.TimeField()

    def __str__(self):
        return f'{self.ourTeam.name} vs {self.opponentTeam} on {self.date}'
    