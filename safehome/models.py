from django.db import models

# # mariaDB에 safehome_area 로 table 추가(자동)
# class Area(models.Model):
#     name = models.CharField(max_length= 30, primary_key=True)
#
#     def __str__(self):
#         return self.name  # 자치구 이름으로 admin에 보이도록한다

# mariaDB에 safehome_crime 으로 table 추가(자동)
class Crime(models.Model):
    id = models.IntegerField(primary_key=True, default = '')
    # 자치구 이름
    area = models.CharField(max_length=30)
    # 살인
    murder = models.IntegerField()
    # 강도
    robber = models.IntegerField()
    # 강간강제추행
    rape = models.IntegerField()
    # 절도
    theft = models.IntegerField()
    # 폭력
    violence = models.IntegerField()

    # 발생합계
    total = models.IntegerField()
    # 검거합계
    arr_total = models.IntegerField()

    # 범죄 검거율
    arrest = models.IntegerField()

    def __str__(self):
        return self.area  # 자치구 이름으로 admin에 보이도록한다

# class Flood(models.Model):
#     # 자치구
#     area = models.CharField(max_length=30, primary_key=True)
#     # 이재민
#     people = models.IntegerField(default=0)
#     # 주택침수세대
#     houses = models.IntegerField(default=0)
#     # 건물
#     buildings = models.IntegerField(default=0)
#     # 공공시설
#     public = models.IntegerField(default=0)
#     # 피해액합계
#     total = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.area  # 자치구 이름으로 admin에 보이도록한다