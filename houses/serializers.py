from rest_framework import serializers
from .models import CareTaker, Houses, LandLords, Teenants


class CareTakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareTaker
        fields = ['user_id', 'house_id']

class HousesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = ['name', 'rent_amount', 'description', 'rating',
                  'description', 'location']

class LandLordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandLords
        fields = ['user_id', 'num_houses']

class TeenantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teenants
        fields = ['user_id', 'house_id']