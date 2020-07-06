from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from company.models import Company
from company.serializers import CompanySerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def company_list(request):
    # GET list of companies, POST a new company, DELETE all companies
    if request.method == 'GET':
        companies = Company.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            companies = companies.filter(name__icontains=name)
        
        companies_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False)

    elif request.method == 'POST':
            company_data = JSONParser().parse(request)
            company_serializer = CompanySerializer(data=company_data)
            if company_serializer.is_valid():
                company_serializer.save()
                return JsonResponse(company_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
            count = Company.objects.all().delete()
            return JsonResponse({'message': '{} Company were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) 
    return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, pk):
    # find company by pk (id)
    try: 
        company = Company.objects.get(pk=pk) 
        if request.method == 'GET': 
            company_serializer = CompanySerializer(company) 
            return JsonResponse(company_serializer.data)
        elif request.method == 'PUT': 
            company_data = JSONParser().parse(request) 
            company_serializer = CompanySerializer(company, data=company_data) 
            if company_serializer.is_valid(): 
                company_serializer.save() 
                return JsonResponse(company_serializer.data) 
            return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            company.delete() 
        return JsonResponse({'message': 'Company was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)    
    except Company.DoesNotExist: 
        return JsonResponse({'message': 'The Company does not exist'}, status=status.HTTP_404_NOT_FOUND) 