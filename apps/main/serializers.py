from rest_framework import serializers

from .models import (
    Category,
    Region,
    District,
    Color,
    Item,
)
from auths.serializers import MyUserSerializer


class RegionSerializer(serializers.ModelSerializer):
    """
    Region serializer.
    """
    class Meta:
        model = Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    """
    District serializer.
    """
    class Meta:
        model = District
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    """
    Color serializer.
    """
    class Meta:
        model = Color
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Category serializer.
    """
    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    """
    Item serializer.
    """
    region = RegionSerializer()
    district = DistrictSerializer()
    color = ColorSerializer()
    author = MyUserSerializer()

    class Meta:
        model = Item
        fields = '__all__'
