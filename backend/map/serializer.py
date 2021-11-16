from rest_framework import serializers
# pip install Django django-rest-framework
from .models import Map as map


class MapSerializer(serializers.Serializer):
    type = serializers.CharField()
    short_name = serializers.CharField()
    name = serializers.CharField()
    lat = serializers.CharField()
    long = serializers.CharField()
    population = serializers.CharField()
    cases = serializers.CharField()
    med_point = serializers.CharField()

    class Meta:
        model = map
        fields = '__all__'
    #
    # def create(self, validated_data):
    #     return user.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     user.objects.filter(pk=instance.username).update(**validated_data)