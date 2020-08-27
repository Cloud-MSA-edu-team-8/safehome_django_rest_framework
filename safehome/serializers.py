from rest_framework import serializers
from .models import Area, Alcohol, Children, Crime, Fire_damage, Flood, House, Population, Total, Total_rate, Svgd

class AreaSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'code',
           'areas',
       )
       model = Area

class AlcoholSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'areas',
           'accident_num',
           'dead_num',
           'casual_num',
           'acc_rate',
           'casual_rate',
       )
       model = Alcohol

class ChildrenSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'areas',
           'accident_num',
           'accident_rate',
           'safe_num',
           'safe_rate',
       )
       model = Children

class CrimeSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'areas',
           'murder',
           'robber',
           'rape',
           'theft',
           'violence',
           'total',
           'arr_total',
           'arrest',
       )
       model = Crime

class FireDamageSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'areas',
           'fire_damage',
       )
       model = Fire_damage

class FloodSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'area',
           'people',
           'houses',
           'buildings',
           'public',
           'total_cost',
       )
       model = Flood

class HouseSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'areas',
           'price',
       )
       model = House

class PopulationSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'areas',
           'household',
           'total_male',
           'total_female',
           'total_total',
           'kor_male',
           'kor_female',
           'kor_total',
           'for_male',
           'for_female',
           'for_total',
       )
       model = Population

class TotalSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'areas',
           'population',
           'flood_vic',
           'crime_num',
           'crime_arr',
           'fire_cost',
           'child_car_num',
           'alc_car_num',
           'house_price',
       )
       model = Total

class TotalRateSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'areas',
           'population_rate',
           'population',
           'flood_vic_rate',
           'flood_vic',
           'crime_num_rate',
           'crime_num',
           'crime_arr',
           'fire_cost_rate',
           'fire_cost',
           'child_car_rate',
           'child_car_num',
           'alc_car_rate',
           'alc_car_num',
           'house_price_rate',
           'house_price',
       )
       model = Total_rate

class SvgdSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'code',
           'colour',
           'location'
       )
       model = Svgd
