from django.conf.urls import url 
from internships import views 
 
urlpatterns = [ 
    url(r'^api/internships$', views.internship_list),
    url(r'^api/internships/(?P<pk>[0-9]+)$', views.internship_detail),
]