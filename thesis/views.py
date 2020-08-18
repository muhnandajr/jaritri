from django.shortcuts import render

from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from thesis.models import Thesis
from thesis.serializers import ThesisSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def thesis_list(request):
    # GET list of lecturers, POST a new Lecturer, DELETE all lecturers
    if request.method == 'GET':
        thesiss = Thesis.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            thesiss = thesiss.filter(name__icontains=name)
        
        thesiss_serializer = ThesisSerializer(thesiss, many=True, context={'request': request})
        return JsonResponse(thesiss_serializer.data, safe=False)

    elif request.method == 'POST':
            thesis_serializer = ThesisSerializer(data=request.data, context={'request': request})
            if thesis_serializer.is_valid():
                thesis_serializer.save()
                return JsonResponse(thesis_serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
            count = Thesis.objects.all().delete()
            return JsonResponse({'message': '{} Thesis Data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) 
    return JsonResponse(thesis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def thesis_detail(request,pk):
    # find lecturer by pk (id)
    try: 
        thesis = Thesis.objects.get(pk=pk) 
        if request.method == 'GET': 
            thesis_serializer = ThesisSerializer(thesis, context={'request': request}) 
            return JsonResponse(thesis_serializer.data)
        elif request.method == 'PUT': 
            thesis_serializer = ThesisSerializer(thesis, data=request.data, context={'request': request}) 
            if thesis_serializer.is_valid(): 
                thesis_serializer.save() 
                return JsonResponse(thesis_serializer.data) 
            return JsonResponse(thesis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            thesis.delete() 
        return JsonResponse({'message': 'Thesis data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)    
    except Thesis.DoesNotExist: 
        return JsonResponse({'message': 'The Thesis data does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST','DELETE'])
def thesis_user(request, pk):
    # GET list of lecturers, POST a new Lecturer, DELETE all lecturers
    thesis = Thesis.objects.get(name=pk) 
    if request.method == 'GET': 
        thesis_serializer = ThesisSerializer(thesis, context={'request': request}) 
        return JsonResponse(thesis_serializer.data)
    # if request.method == 'GET':
    #     thesiss = Thesis.objects.filter(name=pk)
        
    #     thesiss_serializer = ThesisSerializer(thesiss, many=True, context={'request': request})
    #     return JsonResponse(thesiss_serializer.data, safe=False)

    elif request.method == 'POST':
            thesis_serializer = ThesisSerializer(data=request.data, context={'request': request})
            if thesis_serializer.is_valid():
                thesis_serializer.save()
                return JsonResponse(thesis_serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
            count = Thesis.objects.all().delete()
            return JsonResponse({'message': '{} Thesis Data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) 
    return JsonResponse(thesis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)