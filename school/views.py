from django.shortcuts import render,HttpResponse
from school import models
import json
# Create your views here.


def students(request):
    stu_list = models.Students.objects.all()
    cls_list = models.Classes.objects.all()
    return render(request,'students.html',{'stu_list':stu_list,'cls_list':cls_list})


def stuadd(request):
    result = {
        'status': True,
        'errormsg': None,
        'data': None
    }
    try:
        if request.method == 'POST':
            age = request.POST.get('inputAge')
            name = request.POST.get('inputName')
            cs = request.POST.get('selectClass')
            gender = request.POST.get('inputGender')
            obj = models.Students.objects.create(
                name=name,
                age=age,
                gender=gender,
                cs_id=cs
            )
            result['data']=obj.id
    except Exception as e:
        result['status'] = False
        result['errormsg'] = str(e)

    s = json.dumps(result)
    return HttpResponse(s)


def stuedit(request):
    result = {
        'status': True,
        'errormsg': None,
        'data': None
    }
    try:
        if request.method == 'POST':
            print(request.POST)
            s_id = request.POST.get('s_id')
            age = request.POST.get('inputAge')
            name = request.POST.get('inputName')
            cs = request.POST.get('selectClass')
            gender = request.POST.get('inputGender')
            models.Students.objects.filter(id=s_id).update(
                name=name,
                age=age,
                gender=gender,
                cs_id=cs
            )

    except Exception as e:
        result['status'] = False
        result['errormsg'] = str(e)

    s = json.dumps(result)
    return HttpResponse(s)


def delstu(request):
    result = {
            'status':True,
            'msg':None
        }
    if request.method == 'POST':

        s_id = request.POST.get('s_id')
        try:
            models.Students.objects.get(id=s_id).delete()
        except Exception as e:
            result['status'] = False
            result['msg'] = str(e)
    s = json.dumps(result)
    return HttpResponse(s)