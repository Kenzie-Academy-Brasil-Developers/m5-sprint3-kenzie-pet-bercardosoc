from rest_framework import serializers, status

from groups.models import Group


class GroupSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    scientific_name = serializers.CharField()

    """ def create(self, validated_data):

        group, created = Group.objects.get_or_create(**validated_data)

        if not created: 
            raise ValueError(
                {"message": f"`{validated_data['name']}` already exists."}, status.HTTP_409_CONFLICT
            )
        
        return group """