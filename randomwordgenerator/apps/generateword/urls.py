from django.conf.urls import url
from . import views

#Here we are going to list ONLY the list of URL - Regex  -- 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reset$', views.reset),
]