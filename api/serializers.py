from rest_framework import serializers
from api.models import News, ICE, People, Section


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'content']


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['name', 'lastname']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['name', ]


class ICECreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ICE
        fields = ['name', ]


class ICEListSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(read_only=True, many=True)

    class Meta:
        model = ICE
        fields = ['id', 'name', 'sections']
