from functools import partial
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from animals.models import Animal
from animals.serializers import AnimalSerializer

class AnimalView(APIView):

    def get(self, _: Request):
        
        animals = Animal.objects.all()
        serialized = AnimalSerializer(instance=animals, many=True)

        return Response({
            "animals": serialized.data
        }, status.HTTP_200_OK)

    def post(self, request: Request):

        serialized = AnimalSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)

class AnimalViewDetail(APIView):
    
    def get(self, request, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)

        serializer = AnimalSerializer(animal)   

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, animal_id):

        try:
            animal = get_object_or_404(Animal, pk=animal_id)

            serialized = AnimalSerializer(instance=animal, data=request.data, partial=True)
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data, status.HTTP_200_OK)

        except KeyError as key:
            return Response(
                {"message": f'You can not update {key} property'}, 
                status.HTTP_422_UNPROCESSABLE_ENTITY
            )
            
        except Http404:
            return Response({"error": "Animal not found"})

    def delete(self, request, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)

        animal.delete()

        return Response(status.HTTP_204_NO_CONTENT)