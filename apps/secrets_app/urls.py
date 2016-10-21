from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^like/(?P<secret_id>\d+)$', views.like, name='like'),
]
