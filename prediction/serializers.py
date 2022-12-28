from prediction.models import *
from rest_framework import serializers


class TraductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traduction
        fields = '__all__'


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()