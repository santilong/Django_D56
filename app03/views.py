from django.shortcuts import render,HttpResponse,redirect
from app03 import models
# Create your views here.
from django import forms
from django.forms import fields

class User_info(forms.Form):
    user = fields.CharField(max_length=8,required=True,error_messages={
        'required':'必须填哈 你个瓜批',
        'max_length':'太短',
    })
    email = fields.EmailField(max_length=32,required=True,error_messages={
        'required':'必须填哈 你个瓜批',
        'max_length':'太短',
        'invalid':'邮件格式错误',
    })


def users(request):
    user_lsit = models.USERS.objects.all()
    return render(request,'users.html',{'user_lsit':user_lsit})

def addusers(request):
    if request.method == 'GET':
        user_info = User_info()
        return render(request,'addusers.html',{'user_info':user_info})
    elif request.method == 'POST':
        user_info = User_info(request.POST)
        if user_info.is_valid():
            models.USERS.objects.create(**user_info.cleaned_data)
            return redirect('/users.html')
        else:
            return render(request, 'addusers.html', {'user_info': user_info})


def edituser(request,nid):
    if request.method == 'GET':
        data = models.USERS.objects.filter(id=nid).first()
        obj = User_info({'user':data.user,'email':data.email}) ###字典，前端返回数据库读取的数据到INPUT的默认值；
        return render(request,'edituser.html',{'obj':obj,'nid':nid})
    else:
        obj = User_info(request.POST)
        if obj.is_valid():
            models.USERS.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('users.html')
        else:
            return render(request, 'edituser.html', {'obj': obj,'nid':nid})
