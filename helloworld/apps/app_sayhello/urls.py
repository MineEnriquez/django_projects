#file manually added
#  your_project_name_here/apps/your_app_name_here/urls.py
from django.conf.urls import url
from . import views

#Here we are going to list ONLY the list of URL - Regex  -- 

urlpatterns = [
    url(r'^$', views.index),
]