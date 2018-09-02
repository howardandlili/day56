#!/user/bin/env python
__author__ = 'Howie'
from django.urls import path
from paging import views
urlpatterns = [
    path('', views.index, name='index'),
]