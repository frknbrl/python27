from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^yeni2/', views.yeni2, name='yeni2'),
]