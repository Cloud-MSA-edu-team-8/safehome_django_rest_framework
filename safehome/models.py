from django.db import models

# # mariaDB에 safehome_area 로 table 추가(자동)
# class Area(models.Model):
#     name = models.CharField(max_length= 30, primary_key=True)
#
#     def __str__(self):
#         return self.name  # 자치구 이름으로 admin에 보이도록한다

# mariaDB에 safehome_crime 으로 table 추가(자동)

class Alcohol(models.Model):

    # 자치구 이름
    area = models.CharField(max_length=30, default='')

    # 음주운전 교통사고 발생건수
    accident_num = models.IntegerField(default=0)
    # 사망자수
    dead_num = models.IntegerField(default=0)
    # 부상자수
    casual_num = models.IntegerField(default=0)
    # 음주운전 사고 발생 비율
    acc_rate = models.FloatField(default=0)
    # 부상자 비율
    casual_rate = models.FloatField(default=0)

    # 시군구코드
    code = models.IntegerField(primary_key=True, default = '')

    def __str__(self):
        return self.area  # 자치구 이름으로 admin에 보이도록한다

class Children(models.Model):
    # 자치구 이름
    area = models.CharField(max_length=30,default='')

    # 어린이 교통사고 발생건수
    accident_num = models.IntegerField(default=0)
    # 어린이 교통사고 발생비율
    accident_rate = models.FloatField(default=0)
    # 어린이보호구역내 어린이 교통사고 발생건수
    safe_num = models.IntegerField(default=0)

    # 어린이보호구역내 어린이 교통사고 발생비율
    safe_rate = models.FloatField(default=0)
    # 시군구코드
    code = models.IntegerField(primary_key=True, default = '')

    def __str__(self):
        return self.area  # 자치구 이름으로 admin에 보이도록한다

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

class Fire_damage(models.Model):

    # 자치구 이름
    area = models.CharField(max_length=30,default='')
    # 재산피해소계
    fire_damage = models.IntegerField(default=0)

    # 시군구코드
    code = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.area  # 자치구 이름으로 admin에 보이도록한다

class Flood(models.Model):
    id = models.IntegerField(primary_key=True, default='')
    # 자치구
    area = models.CharField(max_length=30)
    # 이재민
    people = models.IntegerField(default=0)
    # 주택침수세대
    houses = models.IntegerField(default=0)
    # 건물
    buildings = models.IntegerField(default=0)
    # 공공시설
    public = models.IntegerField(default=0)
    # 피해액합계
    total_cost = models.IntegerField(default=0)

    def __str__(self):
        return self.area  # 자치구 이름으로 admin에 보이도록한다

class House(models.Model):
    # 시군구코드
    id = models.IntegerField(primary_key=True, default='')
    # 자치구
    area = models.CharField(max_length=30)
    # 평당가
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.area

class Population(models.Model):
    # 시군구코드
    id = models.IntegerField(primary_key=True, default='')
    # 자치구
    area = models.CharField(max_length=30)
    # 세대수
    household = models.IntegerField(default=0)
    # 남자 total
    total_male = models.IntegerField(default=0)
    # 여자 total
    total_female = models.IntegerField(default=0)
    # 총 인구수
    total_total = models.IntegerField(default=0)
    # 한국인 남자
    kor_male = models.IntegerField(default=0)
    # 한국인 여자
    kor_female = models.IntegerField(default=0)
    # 총 한국인
    kor_total = models.IntegerField(default=0)
    # 외국인 남자
    for_male = models.IntegerField(default=0)
    # 외국인 여자
    for_female = models.IntegerField(default=0)
    # 총 외국인
    for_total = models.IntegerField(default=0)

    def __str__(self):
        return self.area

class Total(models.Model):
    # 시군구코드
    id = models.IntegerField(primary_key=True, default='')
    # 자치구
    area = models.CharField(max_length=30)
    # 인구수
    population = models.IntegerField(default=0)
    # 이재민
    flood_vic = models.IntegerField(default=0)
    # 4대범죄 발생건수
    crime_num = models.IntegerField(default=0)
    # 검거율
    crime_arr = models.IntegerField(default=0)
    # 화재피해액
    fire_cost = models.IntegerField(default=0)
    # 어린이 교통사고 수
    child_car_num = models.IntegerField(default=0)
    # 음주운전 건수
    alc_car_num = models.IntegerField(default=0)
    # 평당가
    house_price = models.IntegerField(default=0)
