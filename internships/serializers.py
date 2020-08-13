from rest_framework import serializers 
from internships.models import Internship
from centraldata.serializers import StudentSerializer
from lecturers.serializers import LecturerSerializer
from company.serializers import CompanySerializer
from topics.serializers import TopicSerializer
from authentication.serializers import UserSerializer



class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['name'] = UserSerializer(read_only=True)
        self.fields['member'] = StudentSerializer(read_only=True)
        self.fields['lecturer_adviser'] = LecturerSerializer(read_only=True)
        self.fields['company_name'] = LecturerSerializer(read_only=True)
        self.fields['intern_topic'] = LecturerSerializer(read_only=True)
        return super(InternshipSerializer, self).to_representation(instance)

