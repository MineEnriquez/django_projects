from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^books/(?P<book_id>\d+)$', views.showbook),
    url(r'^addauthor$', views.addauthor),
    url(r'^createauthor$', views.createauthor),
    url(r'^authors$', views.authorspage),
    url(r'^authors/(?P<author_id>\d+)$', views.showauthor),
    url(r'^addbooktoauthor$', views.addbooktoauthor)
]