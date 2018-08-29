from django.shortcuts import render
from school import models
# Create your views here.

def students(request):
    stu_list = models.Students.objects.all()
    return render(request,'students.html',{'stu_list':stu_list})