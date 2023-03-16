from rest_framework import serializers
from .models import *


class PositionJobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PositionJob


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Status


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee

    def to_representation(self, instance):
        representation = super(EmployeeSerializer, self).to_representation(instance)
        representation['PositionJob'] = PositionJobSerializer(instance.PositionJob, many=False).data
        return representation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Order

    def to_representation(self, instance):
        representation = super(OrderSerializer, self).to_representation(instance)
        representation['status'] = StatusSerializer(instance.status, many=False).data
        representation['Employee'] = EmployeeSerializer(instance.Employee, many=False).data
