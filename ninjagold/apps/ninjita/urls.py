from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.process_money),
    url(r'^something$', views.something),
    url(r'^reset$', views.reset),
]

