from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^checkout$', views.checkout, name="checkout"),
    url(r'^buy/(?P<item_id>\d{1,50})$', views.buy, name="buy"),
]