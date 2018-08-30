from django.shortcuts import render,HttpResponse
from school import models
# Create your views here.


def students(request):
    stu_list = models.Students.objects.all()
    return render(request,'students.html',{'stu_list':stu_list})


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

    import json
    s = json.dumps(result)
    return HttpResponse(s)
