from rest_framework import serializers 
from company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','business','address','website','email','pic_name','pic_number','create_at','updated_at')