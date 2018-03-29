from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from django import forms
from django.forms import fields

class F1(forms.Form):
    user = fields.CharField(max_length=16,required=True,error_messages={
        'required':'必填',
        'max_lenght':'最大长度16个字符',
    })
    pwd = fields.CharField(max_length=8,required=True,error_messages={
        'required':'必填',
        'max_lenght':'最大长度16个字符',
    })
    age = fields.IntegerField(required=True,error_messages={
        'required':'必填',
        'invalid':'必须为数字',
    })
    email = fields.EmailField(required=True,error_messages={
        'required':'必填',
        'invalid':'邮件格式错误',
    })


def f1(request):
    if request.method == 'GET':
        obj = F1()
        return render(request,'f1.html',{'obj':obj})
    else:
        obj = F1(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            return redirect('https://www.baidu.com')
        else:
            return render(request,'f1.html',{'obj':obj})

