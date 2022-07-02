from django.shortcuts import get_object_or_404
from animals.models import Animal
from rest_framework import serializers

from animals.models import Animal
from characteristics.models import Characteristic
from characteristics.serializers import CharacteristicSerializer
from groups.models import Group
from groups.serializers import GroupSerializer

class AnimalSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)

    def create(self, validated_data): 

        group = validated_data.pop("group")
        characteristics = validated_data.pop("characteristics")

        group, _ = Group.objects.get_or_create(**group)
        animal = Animal.objects.create(**validated_data, group=group)

        for characteristic in characteristics: 
            characteristic, _ = Characteristic.objects.get_or_create(**characteristic)
            animal.characteristics.add(characteristic)

        return animal 

    def update(self, instance, validated_data):
        keys_not_available = ('sex', 'group',)

        for key, value in validated_data.items():
            if key in keys_not_available:
                raise KeyError(key)

            if key == "characteristics" and type(value) == list:
                for characteristic in value:
                    c, _ = Characteristic.objects.get_or_create(**characteristic)
                    instance.characteristics.add(c)
            
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

