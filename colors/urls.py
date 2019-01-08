from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list', views.colorsList, name='colorsList'),
    url(r'^add/(?P<color_name>[A-Za-z]+)/$', views.addColor, name='addColor'),
    url(r'^get/(?P<color_name>[A-Za-z]+)/$', views.getColor, name='getColor'),

]