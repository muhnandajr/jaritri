from rest_framework import serializers 
from centraldata.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','student_name','student_nim','student_number_phone','student_email','file','student_address','student_city','student_province','student_postal_code','create_at','updated_at')