from rest_framework import serializers


class PassengersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['passenger_id','name','surname','email','status','phone_number']