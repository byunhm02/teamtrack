from django.shortcuts import render
import os
from rest_framework import serializers,status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
import requests
from django.conf import settings
from django.http import JsonResponse
from .models import TeamUserManager,TeamUser
from django.contrib.auth import get_user_model,authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import kakaoLoginSerializer,TeamUserSerializer,KakaoUserCreateSerializer, RegistrationSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verify(request):
    return Response({'detail': 'Token is verified.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny]) 
def login(request):
    serializer=LoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        nickname=serializer.validated_data['nickname']
        password=serializer.validated_data['password']
        
        user=authenticate(request,nickname=nickname,password=password)
        if user is None:
            if not User.objects.filter(nickname=nickname).exists():
                return Response({'message': '회원가입이 필요합니다'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'message':'아이디 또는 비밀번호가 일치하지 않습니다.'},status=status.HTTP_401_UNAUTHORIZED)
    
        refresh=RefreshToken.for_user(user)
        access_token = refresh.access_token
        
        return Response({
                'refresh_token': str(refresh),
                'access_token': str(access_token),
            }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([AllowAny])  
def register(request):
    
    serializer=RegistrationSerializer(data=request.data)
    
    
    if serializer.is_valid(raise_exception=True):
        user=serializer.save() #RegistrationSerializer에서 create 메서드를 호출하여 사용자 객체를 생성합
        user.set_password(serializer.validated_data['password'])

        user.save()
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def kakao_register(request):
    access_token=request.data.get("access_token")
    
    #근데 여기서 엑세스토큰의 유효성을 검사하는 api를 호출하면 안되나??
    if not access_token:
            return JsonResponse({'error':'access_code is required'},status=400)
    
    
    # 엑세스 토큰을 사용하여 사용자 정보 가져오기
    user_info_url = 'https://kapi.kakao.com/v2/user/me'
    user_info_response = requests.get(
        user_info_url,
        headers={'Authorization': f'Bearer {access_token}'}
    )
    
    if user_info_response.status_code != 200:
        return JsonResponse({'error': 'Failed to get user info from Kakao'}, status=400)
    kakao_user_info = user_info_response.json()
    nickname = kakao_user_info['properties'].get('nickname')

    
    if not nickname:
        return JsonResponse({'error':'Failed to get nickname from kakao'},status=400)
    
    #이미 등록된 사용자인지 검사
    if User.objects.filter(nickname=nickname).exists():
        return JsonResponse({'error': 'User already registered. Please login.'}, status=400)
    
    #새로운 사용자 생성
    serializer=KakaoUserCreateSerializer(data={'nickname':nickname})
    if serializer.is_valid(raise_exception=True):
        user=serializer.save()
        user.set_unusable_password()
        user.save()
        
        refresh_token=RefreshToken.for_user(user)
        access_token = refresh_token.access_token
        
        return Response({
            'refresh_token':str(refresh_token),
            'access_token':str(access_token)

        },status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def kakao_login(request):
    serializer = kakaoLoginSerializer(data=request.data)
    
    if not serializer.is_valid():
        return JsonResponse(serializer.errors, status=400)
    
    access_code = serializer.validated_data['access_code']
    
    # 인가 코드 사용해 kakao 서버에 엑세스 토큰 요청
    token_url = "https://kauth.kakao.com/oauth/token"
    headers = {
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    data = {
            "grant_type": "authorization_code",
            "client_id": settings.KAKAO_CLIENT_ID,
            "client_secret": settings.KAKAO_CLIENT_SECRET,
            "redirect_uri": settings.KAKAO_REDIRECT_URI,
            "code": access_code
    }
    token_response = requests.post(token_url, headers=headers, data=data)
    if token_response.status_code != 200:
        return JsonResponse({'error': 'Failed to obtain access token from Kakao'}, status=400)
    
    tokens = token_response.json()
        
    # 디버깅을 위한 로그 추가
    print("Token Response:", tokens)
    
    if 'access_token' in tokens:
        access_token=tokens['access_token']
        
        #카카오 사용자 정보 요청
        user_info_url = "https://kapi.kakao.com/v2/user/me"
        headers = {
                "Authorization": f"Bearer {access_token}"
        }
        user_info_response = requests.get(user_info_url, headers=headers)
        
        #if user_info_response.status_code != 200:
        #    return JsonResponse({'error': 'Failed to obtain user info from Kakao'}, status=400)
    
        user_info = user_info_response.json()
        
        # 디버깅을 위한 로그 추가
        print("User Info:", user_info)
        
        if 'id' not in user_info:
                return JsonResponse({'error': 'Failed to obtain user info from Kakao'}, status=400)
        
        
        nickname=user_info['properties']['nickname']
        
        try: 
            user=User.objects.get(nickname=nickname)
            
            #사용자 존재 시 jwt토큰 발급
            #token=get_tokens_for_user(user)
            refresh_token=RefreshToken.for_user(user)
            access_token = refresh_token.access_token
            return Response({
            'refresh_token':str(refresh_token),
            'access_token':str(access_token)

        },status=status.HTTP_200_OK)
        except User.DoesNotExist:
            #존재하지 않을경우 발급한 엑세스 토큰을 이용해 회원가입하도록!
            return JsonResponse({
                'error': 'User is not registered. Please register first.',
                'access_token': access_token,
                'nickname': nickname
                }, status=400)
    else:  
        return JsonResponse({'error': 'Failed to obtain access token'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)