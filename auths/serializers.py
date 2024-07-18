from rest_framework import serializers
from auths.models import TeamUser,TeamUserManager

#카카오 로그인을 위한 시리얼라이저
class kakaoLoginSerializer(serializers.Serializer):
    access_code=serializers.CharField()
    
    
#전체 사용자 모델을 시리얼라이즈함 
# 사용자 정보를 조회하거나 업데이트 할 때 사용, 
#일반로그인이나 소셜 로그인 후 사용자 프로필 정보를 가져오거나 수정시 사용 
class TeamUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamUser
        fields='__all__'
        
        
        #id필드는 어떻게 처리?
        def create(self,validated_data):
            user=TeamUser.objects.create_user(
                nickname=validated_data['nickname'],
                password=validated_data.get('password'), #일반 로그인시 필요
                myteam=validated_data.get('email')
            )
            return user
            
            
class KakaoUserCreateSerializer(serializers.Serializer):
    nickname = serializers.CharField()

    def create(self, validated_data):
        user = TeamUser.objects.create_user(
            nickname=validated_data['nickname'],
            myteam=validated_data.get('myteam')
            
        )
        return user
    
#일반 로그인

#일반 사용자의 회원 가입을 처리하기 위한 시리얼라이저.
# 이 시리얼라이저를 사용하여 사용자를 등록할 때는 이메일, 패스워드, 설명을 받고, 닉네임은 사용하지않음..
class RegistrationSerializer(serializers.Serializer):
    nickname = serializers.CharField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model=TeamUser
        fields = ['nickname', 'password']
        
    def create(self, validated_data):
        user = TeamUser.objects.create_user(
            nickname=validated_data['nickname'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
#일반 로그인용 시리얼라이저, 이메일과 패스워드를 받음.  
class LoginSerializer(serializers.Serializer):
    nickname = serializers.CharField()
    password = serializers.CharField(write_only=True)