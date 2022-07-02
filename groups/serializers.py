from rest_framework import serializers, status

from groups.models import Group

class GroupsSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    scientific_name = serializers.CharField()