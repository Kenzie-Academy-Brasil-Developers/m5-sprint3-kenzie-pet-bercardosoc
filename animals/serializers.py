from django.shortcuts import get_object_or_404
from animals.models import Animal
from rest_framework import serializers

from animals.models import Animal
from characteristics.models import Characteristic
from characteristics.serializers import CharacteristicSerializer
from groups.models import Group
from groups.serializers import GroupsSerializer

class AnimalSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.CharField()

    group = GroupsSerializer(read_only=True, source="animal")

    characteristics = CharacteristicSerializer(many=True)

    def create(self, validated_data): 

        group_id = validated_data.pop("group_id")
        characteristics = validated_data.pop("characteristics")

        group = get_object_or_404(Group, pk=group_id)

        animal = Animal.objects.create(**validated_data, group=group)

        for characteristic in characteristics:
            
            characteristic, _ = Characteristic.objects.get_or_create(**characteristic)
            animal.characteristics.add(characteristic)

        return characteristic