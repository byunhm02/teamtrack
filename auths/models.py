from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class TeamUserManager(BaseUserManager):
    def create_user(self,nickname,password=None,myteam=None):
        if not nickname:
            raise ValueError('Users must have a nickname')
        
        
        user=self.model(
            nickname=nickname,
            #password=password,
            myteam=myteam
        )
        
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self,nickname,password=None):
        if not nickname:
            raise ValueError('Users must have a nickname')
        
        superuser=self.create_user(
            nickname=nickname
        )
        superuser.is_admin=True
        superuser.set_password(password)
        superuser.is_staff = True
        superuser.is_superuser = True

        superuser.save()
        
        return superuser

class TeamUser(AbstractBaseUser):
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    nickname=models.CharField(max_length=50,unique=True)
    myteam = models.ForeignKey('matches.Team', on_delete=models.SET_NULL, null=True, blank=True)
    objects=TeamUserManager()
    

    
    
    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD='nickname'
    REQUIRED_FIELDS = []
    
    
    def __str__(self):
        return self.nickname
    
    #사용자가 관리자(is_admin=True)인 경우, 그 사용자를 스태프로 간주
    @property
    def is_staff(self):
        return self.is_admin
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True