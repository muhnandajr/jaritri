from rest_framework import serializers 
from lecturers.models import Lecturer

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('id','name','email','nip','nidn','create_at','updated_at')