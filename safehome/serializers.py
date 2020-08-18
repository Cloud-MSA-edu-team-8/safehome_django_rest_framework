from rest_framework import serializers
from .models import Alcohol, Children, Crime, Fire_damage, Flood, House, Population

class AlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'area',
            'accident_num',
            'dead_num',
            'casual_num',
            'acc_rate',
            'casual_rate',
            'code'
        )
        model = Alcohol

class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'area',
            'accident_num',
            'accident_rate',
            'safe_num',
            'safe_rate',
            'code'
        )
        model = Children

class CrimeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'area',
            'murder',
            'robber',
            'rape',
            'theft',
            'violence',
            'total',
            'arr_total',
            'arrest'
        )
        model = Crime

class FireDamageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'area',
            'fire_damage',
            'code'
        )
        model = Fire_damage

class FloodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'area',
            'people',
            'houses',
            'buildings',
            'public',
            'total_cost'
        )
        model = Flood

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'area',
            'price'
        )
        model = House

class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'area',
            'household',
            'total_male',
            'total_female',
            'total_total',
            'kor_male',
            'kor_female',
            'kor_total',
            'for_male',
            'for_female',
            'for_total'
        )
        model = Population
