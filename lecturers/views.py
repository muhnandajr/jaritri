from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from lecturers.models import Lecturer
from lecturers.serializers import LecturerSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def lecturer_list(request):
    # GET list of lecturers, POST a new Lecturer, DELETE all lecturers
    if request.method == 'GET':
        lecturers = Lecturer.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            lecturers = lecturers.filter(name__icontains=name)
        
        lecturers_serializer = LecturerSerializer(lecturers, many=True)
        return JsonResponse(lecturers_serializer.data, safe=False)

    elif request.method == 'POST':
            lecturer_data = JSONParser().parse(request)
            lecturer_serializer = LecturerSerializer(data=lecturer_data)
            if lecturer_serializer.is_valid():
                lecturer_serializer.save()
                return JsonResponse(lecturer_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
            count = Lecturer.objects.all().delete()
            return JsonResponse({'message': '{} Lecturer were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) 
    return JsonResponse(lecturer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lecturer_detail(request, pk):
    # find lecturer by pk (id)
    try: 
        lecturer = Lecturer.objects.get(pk=pk) 
        if request.method == 'GET': 
            lecturer_serializer = LecturerSerializer(lecturer) 
            return JsonResponse(lecturer_serializer.data)
        elif request.method == 'PUT': 
            lecturer_data = JSONParser().parse(request) 
            lecturer_serializer = LecturerSerializer(lecturer, data=lecturer_data) 
            if lecturer_serializer.is_valid(): 
                lecturer_serializer.save() 
                return JsonResponse(lecturer_serializer.data) 
            return JsonResponse(lecturer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            lecturer.delete() 
        return JsonResponse({'message': 'Lecturer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)    
    except Lecturer.DoesNotExist: 
        return JsonResponse({'message': 'The Lecturer does not exist'}, status=status.HTTP_404_NOT_FOUND) 