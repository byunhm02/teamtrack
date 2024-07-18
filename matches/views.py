from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Sport,Match
from auths.models import TeamUser,TeamUserManager
from django.shortcuts import get_object_or_404
from .serializers import SelectTeamSerializer,MatchSerializer
# Create your views here.


@api_view(['POST'])
#@permission_classes([AllowAny])  
@permission_classes([IsAuthenticated])
def select_team(request):
    
    user = request.user
    serializer = SelectTeamSerializer(data=request.data)
    
    if serializer.is_valid():
        team = serializer.validated_data['team']
        
        user.myteam = team
        user.save()
        
        #팀의 경기 일정 조회
        matches_as_home = Match.objects.filter(ourTeam=team)
        matches_as_away = Match.objects.filter(opponentTeam=team)
        matches = matches_as_home.union(matches_as_away).order_by('date')
        
        match_serializer = MatchSerializer(matches, many=True)
        
        return Response(
            match_serializer.data
        , status=status.HTTP_200_OK)
        '''
        return Response(
            {
                "detail": "Team selected successfully.",
                "matches": match_serializer.data
            },status=status.HTTP_200_OK
        )
        '''
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def test_select_team(request):
    user = TeamUser.objects.first()  # 임의로 첫 번째 사용자 선택, 실제 구현 시에는 인증된 사용자 사용
    serializer = SelectTeamSerializer(data=request.data)
    
    if serializer.is_valid():
        team = serializer.validated_data['team']
        
        user.myteam = team
        user.save()
        
        # 팀의 경기 일정 조회
        matches_as_home = Match.objects.filter(ourTeam=team)
        matches_as_away = Match.objects.filter(opponentTeam=team)
        matches = matches_as_home.union(matches_as_away).order_by('date')
        
        match_serializer = MatchSerializer(matches, many=True)
        
        return Response({
            "detail": "Team selected successfully.",
            "matches": match_serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)