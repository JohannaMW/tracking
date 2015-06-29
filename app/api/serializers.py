from rest_framework import serializers
from app.models import Driver, Scooter, Trip, Position


class DriverSerializer(serializers.ModelSerializer):
    all_trips = serializers.SerializerMethodField('get_trips')

    class Meta:
        model = Driver
    #fields = ('id', 'password', 'username', 'first_name', 'last_name', 'trips', 'email', 'date_joined', 'dob', 'rfid', )
    #read_only_fields = ('date_joined',)

    def create(self, validated_data):
        return Driver.objects.create(**validated_data)

    def update_password(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    def validate_password(self, attrs, source):
        username = attrs['username']
        password = attrs[source]
        if password == username:
            raise serializers.ValidationError("Password can not be same as username!")
        if len(password)<4:
            raise serializers.ValidationError("Password is too short!")
        return attrs

    def get_trips(self, obj):
        return Trip.objects.filter(driver=obj).values()


class ScooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scooter

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position


class TripSerializer(serializers.ModelSerializer):
    owner = DriverSerializer(read_only=True)
    scooter = ScooterSerializer()

    class Meta:
        model = Trip