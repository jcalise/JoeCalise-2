from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process_money/(?P<location>\w{1,50})$', views.process_money, name="process_money"),
]