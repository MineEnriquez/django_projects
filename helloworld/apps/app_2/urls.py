# URLs
# file manually added
#  your_project_name_here/apps/your_app_name_here/urls.py
from django.conf.urls import url
from . import views

# Here we are going to list ONLY the list of URL - Regex  --

urlpatterns = [
    url(r'^forma$', views.forma),
    url(r'^hello$', views.sayhello),
    url(r'bye$', views.saygoodbye),
    # would only match localhost:8000/bears
    url(r'^bears$', views.one_method),
    # would match localhost:8000/bears/23
    url(r'^bears/(?P<my_val>\d+)$', views.another_method),
    # would match localhost:8000/bears/pooh/poke
    url(r'^bears/(?P<name>\w+)/poke$', views.yet_another),
    # would match localhost:8000/17/brown
    url(r'^(?P<id>[0-9]+)/(?P<color>\w+)$', views.one_more),
]
