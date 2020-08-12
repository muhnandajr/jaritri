from rest_framework import serializers 
from thesis.models import Thesis
from centraldata.serializers import StudentSerializer
from lecturers.serializers import LecturerSerializer
from company.serializers import CompanySerializer
from topics.serializers import TopicSerializer
from authentication.serializers import UserSerializer
class ThesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thesis
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['name'] = UserSerializer(read_only=True)
        self.fields['lecturer_adviser'] = LecturerSerializer(read_only=True)
        self.fields['company_name'] = LecturerSerializer(read_only=True)
        self.fields['thesis_topic'] = LecturerSerializer(read_only=True)
        return super(ThesisSerializer, self).to_representation(instance)

