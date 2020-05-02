from rest_framework import serializers
from app.models import ParkModel


class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkModel
        fields = ['id', 'latitude', 'longitude', 'comment', 'created_by']