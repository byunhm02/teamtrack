from rest_framework import serializers
from auths.models import TeamUser,TeamUserManager
from matches.models import Team,Sport,Match

class SelectTeamSerializer(serializers.Serializer):
    sport_name = serializers.CharField(max_length=100)
    team_name = serializers.CharField(max_length=100)

    def validate(self, data):
        sport_name = data.get('sport_name')
        team_name = data.get('team_name')

        # sport_name과 team_name의 유효성 검사
        try:
            sport = Sport.objects.get(name=sport_name)
        except Sport.DoesNotExist:
            raise serializers.ValidationError("Invalid sport name")

        try:
            team = Team.objects.get(name=team_name, sport=sport)
        except Team.DoesNotExist:
            raise serializers.ValidationError("Invalid team name for the given sport")

        data['sport'] = sport
        data['team'] = team
        return data
    
class MatchSerializer(serializers.ModelSerializer):
    ourTeam = serializers.CharField(source='ourTeam.name')
    opponentTeam = serializers.CharField(source='opponentTeam.name')

    class Meta:
        model = Match
        fields = ['date', 'time', 'ourTeam','opponentTeam']