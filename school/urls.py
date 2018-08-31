#!/user/bin/env python
from django.urls import path
from school import views
urlpatterns = [
    path('students', views.students, name='students'),
    path('stuadd', views.stuadd, name='stuadd'),
    path('delstu', views.delstu, name='delstu'),
    path('stuedit', views.stuedit, name='stuedit'),
]
