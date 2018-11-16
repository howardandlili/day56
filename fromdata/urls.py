#!/user/bin/env python
__author__ = 'Howie'
from django.urls import path,re_path
from fromdata import views
urlpatterns = [
    re_path('^$', views.index, name='index'),
    path('users', views.users, name='users'),
    path('add_user', views.add_user, name='add_user'),
    re_path(r'edit-(\d+)', views.edit, name='edit'),
    path('upload', views.upload, name='upload'),
]