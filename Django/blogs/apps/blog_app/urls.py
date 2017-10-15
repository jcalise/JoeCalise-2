from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<blog>\d{1,50})/$', views.show),
    url(r'^(?P<blog>\d{1,50})/edit$', views.edit),
    url(r'^(?P<blog>\d{1,50})/delete$', views.destroy)
]