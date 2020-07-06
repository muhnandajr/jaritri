from django.conf.urls import url 
from topics import views 
 
urlpatterns = [ 
    url(r'^api/topics$', views.topic_list),
    url(r'^api/topics/(?P<pk>[0-9]+)$', views.topic_detail),
]