from django.conf.urls import url 
from thesis import views 
 
urlpatterns = [ 
    url(r'^api/thesis$', views.thesis_list),
    url(r'^api/thesis/(?P<pk>[0-9]+)$', views.thesis_detail),
]