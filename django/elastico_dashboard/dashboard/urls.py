from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buyer', views.buyer, name='buyer'),
    url(r'^seller', views.seller, name='seller'),
]
