from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from internships.models import Internship
from internships.serializers import InternshipSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def internship_list(request):
    # GET list of lecturers, POST a new Lecturer, DELETE all lecturers
    if request.method == 'GET':
        internships = Internship.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            internships = internships.filter(title__icontains=title)
        
        internships_serializer = InternshipSerializer(internships, many=True, context={'request': request})
        return JsonResponse(internships_serializer.data, safe=False)

    elif request.method == 'POST':
            internship_serializer = InternshipSerializer(data=request.data, context={'request': request})
            if internship_serializer.is_valid():
                internship_serializer.save()
                return JsonResponse(internship_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
            count = Internship.objects.all().delete()
            return JsonResponse({'message': '{} Internship Data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) 
    return JsonResponse(internship_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def internship_detail(request, pk):
    # find lecturer by pk (id)
    try: 
        internship = Internship.objects.get(pk=pk) 
        if request.method == 'GET': 
            internship_serializer = InternshipSerializer(internship, context={'request': request}) 
            return JsonResponse(internship_serializer.data)
        elif request.method == 'PUT': 
            internship_serializer = InternshipSerializer(internship, data=request.data, context={'request': request}) 
            if internship_serializer.is_valid(): 
                internship_serializer.save() 
                return JsonResponse(internship_serializer.data) 
            return JsonResponse(internship_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            internship.delete() 
        return JsonResponse({'message': 'Internship data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)    
    except Internship.DoesNotExist: 
        return JsonResponse({'message': 'The Internship data does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST','DELETE'])
def internship_user(request, pk):
    # GET list of lecturers, POST a new Lecturer, DELETE all lecturers
    internship = Internship.objects.get(name=pk) 
    if request.method == 'GET': 
        internship_serializer = InternshipSerializer(internship, context={'request': request}) 
        return JsonResponse(internship_serializer.data)

    elif request.method == 'POST':
            thesis_serializer = ThesisSerializer(data=request.data, context={'request': request})
            if thesis_serializer.is_valid():
                thesis_serializer.save()
                return JsonResponse(thesis_serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
            count = Thesis.objects.all().delete()
            return JsonResponse({'message': '{} Thesis Data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) 
    return JsonResponse(thesis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)