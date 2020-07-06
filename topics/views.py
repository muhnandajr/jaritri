from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from topics.models import Topic
from topics.serializers import TopicSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def topic_list(request):
    # GET list of topics, POST a new topic, DELETE all topics
    if request.method == 'GET':
        topics = Topic.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            topics = topics.filter(name__icontains=name)
        
        topics_serializer = TopicSerializer(topics, many=True)
        return JsonResponse(topics_serializer.data, safe=False)

    elif request.method == 'POST':
            topic_data = JSONParser().parse(request)
            topic_serializer = TopicSerializer(data=topic_data)
            if topic_serializer.is_valid():
                topic_serializer.save()
                return JsonResponse(topic_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
            count = Topic.objects.all().delete()
            return JsonResponse({'message': '{} Topic were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) 
    return JsonResponse(topic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk):
    # find topic by pk (id)
    try: 
        topic = Topic.objects.get(pk=pk) 
        if request.method == 'GET': 
            topic_serializer = TopicSerializer(topic) 
            return JsonResponse(topic_serializer.data)
        elif request.method == 'PUT': 
            topic_data = JSONParser().parse(request) 
            topic_serializer = TopicSerializer(topic, data=topic_data) 
            if topic_serializer.is_valid(): 
                topic_serializer.save() 
                return JsonResponse(topic_serializer.data) 
            return JsonResponse(topic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            topic.delete() 
        return JsonResponse({'message': 'Topic was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)    
    except Topic.DoesNotExist: 
        return JsonResponse({'message': 'The Topic does not exist'}, status=status.HTTP_404_NOT_FOUND) 