from django.shortcuts import render, HttpResponse ,redirect
from django.forms import fields
from django import forms
from fromdata import models
from fromdata import forms as fform


# Create your views here.


class IndexForm(forms.Form):
    user = fields.CharField(max_length=32,
                            min_length=6,
                            required=True,
                            error_messages={
                                            'required':'用户名不能为空',
                                            'max_length':'最大不能超过32位',
                                            'min_length':'最小不能少于6位',
                                        })
    pwd = fields.CharField(max_length=32, min_length=6, required=True)
    email = fields.EmailField(required=True)
    age = fields.IntegerField(min_value=0, required=True)


def index(request):
    if request.method == 'GET':
        obj = IndexForm()
        return render(request, 'form/index.html',{'obj':obj})
    else:
        obj = IndexForm(request.POST)
        if obj.is_valid():
            print('正确',obj.cleaned_data)
            return HttpResponse(obj.cleaned_data)
        else:
            print('错误',obj.errors)
            return render(request,'form/index.html',{'obj':obj})


def users(request):
    user_list = models.UserInfo.objects.all()
    return render(request,'form/user.html',{'user_list':user_list})

def add_user(request):
    if request.method == 'POST':
        obj = fform.UserForm(request.POST)
        if obj.is_valid():
            print('正确',obj.cleaned_data)
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect('users')
        else:
            print('错误',obj.errors)
            return render(request,'form/add_user.html',{'obj':obj})
    else:
        obj = fform.UserForm()
        return render(request,'form/add_user.html',{'obj':obj})


def edit(request,nid):
    user_obj = models.UserInfo.objects.filter(id=nid)
    if request.method == 'GET':
        user_obj = user_obj.first()
        obj = fform.UserForm({
            'username':user_obj.username,
            'email':user_obj.email,
        })
        return render(request,'form/edit.html',{'obj':obj,'nid':nid})
    else:
        obj = fform.UserForm(request.POST)
        if obj.is_valid():
            user_data = obj.cleaned_data
            print(user_data)
            user_obj.update(**user_data)
            return redirect('users')
        else:
            return render(request,'form/edit.html',{'obj':obj})


def upload(request):
    if request.method == 'GET':
        return render(request,'upload.html')
    else:
        user = request.POST.get('user')
        img = request.FILES.get('img')

        with open(img.name,'wb') as f:
            for line in img.chunks():
                f.write(line)
        return HttpResponse('......')
