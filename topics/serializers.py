from rest_framework import serializers 
from topics.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id','name','create_at','updated_at')