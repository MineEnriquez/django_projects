from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.index),
     url(r'^displaydata$', views.displaydata),
     url(r'^newrecord$', views.newrecord),
 ]