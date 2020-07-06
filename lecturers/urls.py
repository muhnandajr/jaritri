from django.conf.urls import url 
from lecturers import views 
 
urlpatterns = [ 
    url(r'^api/lecturers$', views.lecturer_list),
    url(r'^api/lecturers/(?P<pk>[0-9]+)$', views.lecturer_detail),
]