import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


from matches.models import Sport, Team, Match

# 스포츠 데이터 생성
baseball = Sport.objects.create(name='야구')
soccer = Sport.objects.create(name='축구')



# 팀 데이터 생성
kia = Team.objects.create(name='기아', sport=baseball)
doosan = Team.objects.create(name='두산', sport=baseball)
lotte = Team.objects.create(name='롯데', sport=baseball)
samsung = Team.objects.create(name='삼성', sport=baseball)
kium = Team.objects.create(name='키움', sport=baseball)
hanwha = Team.objects.create(name='한화', sport=baseball)
kt = Team.objects.create(name='kt', sport=baseball)
nc = Team.objects.create(name='nc', sport=baseball)
lg = Team.objects.create(name='lg', sport=baseball)
ssg=Team.objects.create(name='ssg', sport=baseball)



# 경기 일정 데이터 생성
Match.objects.create(ourTeam=samsung, opponentTeam=lg, date='2024-08-01', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=ssg, date='2024-08-02', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=ssg, date='2024-08-03', time='18:00:00')
Match.objects.create(ourTeam=samsung, opponentTeam=ssg, date='2024-08-04', time='17:00:00')
Match.objects.create(ourTeam=samsung, opponentTeam=hanwha, date='2024-08-06', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=hanwha, date='2024-08-07', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=hanwha, date='2024-08-08', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=kia, date='2024-08-09', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=kia, date='2024-08-10', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=kia, date='2024-08-11', time='17:00:00')
Match.objects.create(ourTeam=samsung, opponentTeam=kt, date='2024-08-13', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=kt, date='2024-08-14', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=kt, date='2024-08-15', time='17:00:00')
Match.objects.create(ourTeam=samsung, opponentTeam=nc, date='2024-08-16', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=nc, date='2024-08-17', time='18:00:00')
Match.objects.create(ourTeam=samsung, opponentTeam=nc, date='2024-08-18', time='17:00:00')
Match.objects.create(ourTeam=samsung, opponentTeam=doosan, date='2024-08-20', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=doosan, date='2024-08-21', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=doosan, date='2024-08-22', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=lotte, date='2024-08-23', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=lotte, date='2024-08-24', time='18:00:00')
Match.objects.create(ourTeam=samsung, opponentTeam=lotte, date='2024-08-25', time='17:00:00')
Match.objects.create(ourTeam=samsung, opponentTeam=kium, date='2024-08-27', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=kium, date='2024-08-28', time='18:30:00')
Match.objects.create(ourTeam=samsung, opponentTeam=kium, date='2024-08-29', time='18:30:00')


Match.objects.create(ourTeam=lg, opponentTeam=samsung, date='2024-08-01', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=lotte, date='2024-08-02', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=lotte, date='2024-08-03', time='18:00:00')
Match.objects.create(ourTeam=lg, opponentTeam=lotte, date='2024-08-04', time='17:00:00')
Match.objects.create(ourTeam=lg, opponentTeam=doosan, date='2024-08-06', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=doosan, date='2024-08-07', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=doosan, date='2024-08-08', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=nc, date='2024-08-09', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=nc, date='2024-08-10', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=nc, date='2024-08-11', time='17:00:00')
Match.objects.create(ourTeam=lg, opponentTeam=hanwha, date='2024-08-13', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=hanwha, date='2024-08-14', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=hanwha, date='2024-08-15', time='17:00:00')
Match.objects.create(ourTeam=lg, opponentTeam=kia, date='2024-08-16', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=kia, date='2024-08-17', time='18:00:00')
Match.objects.create(ourTeam=lg, opponentTeam=kia, date='2024-08-18', time='17:00:00')
Match.objects.create(ourTeam=lg, opponentTeam=ssg, date='2024-08-20', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=ssg, date='2024-08-21', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=ssg, date='2024-08-22', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=kium, date='2024-08-23', time='18:00:00')
Match.objects.create(ourTeam=lg, opponentTeam=kium, date='2024-08-24', time='17:00:00')
Match.objects.create(ourTeam=lg, opponentTeam=kium, date='2024-08-25', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=kt, date='2024-08-27', time='18:30:00')
Match.objects.create(ourTeam=lg, opponentTeam=kt, date='2024-08-28', time='18:30:00')





#print("Initial data has been loaded successfully!")