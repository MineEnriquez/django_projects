from django.conf.urls import url
from . import views	# the . indicates that the views file can be found in the same directory as this file

 # #1:  INDEX                   
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<id>[0-9]\d+)$', views.show),
    url(r'^(?P<id>[0-9]\d+)/edit$', views.edit),
    url(r'^(?P<id>[0-9]\d+)/delete$', views.destroy),
]

