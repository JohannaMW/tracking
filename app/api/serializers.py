from rest_framework import serializers
from app.models import Owner, Vehicle, Position



class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
    #fields = ('id', 'password', 'username', 'first_name', 'last_name', 'trips', 'email', 'date_joined', 'dob', 'rfid', )
    #read_only_fields = ('date_joined',)

    def create(self, validated_data):
        return Owner.objects.create(**validated_data)

    def update_password(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
