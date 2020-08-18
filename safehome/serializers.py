from rest_framework import serializers
from .models import Children, Crime, Fire_damage, Flood, Alchohol, House

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

