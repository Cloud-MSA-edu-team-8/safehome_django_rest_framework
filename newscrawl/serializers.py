from rest_framework import serializers
from .models import NewsData

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'link',
            'contents'
        )
        model = NewsData