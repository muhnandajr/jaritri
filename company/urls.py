from django.conf.urls import url 
from company import views 
 
urlpatterns = [ 
    url(r'^api/companies$', views.company_list),
    url(r'^api/companies/(?P<pk>[0-9]+)$', views.company_detail),
]