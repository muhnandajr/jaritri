from rest_framework import serializers 
from centraldata.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','nim','generation','email','avatar','address','city','province','postal_code','create_at','updated_at')