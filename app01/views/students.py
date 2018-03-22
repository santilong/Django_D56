#Author:Santi
from django.shortcuts import render,HttpResponse,redirect
from app01 import models

def students(request):
    stu_list = models.Student.objects.all()
    cla_list = models.Classes.objects.all()
    return render(request,'students.html',{'stu_list':stu_list,'cla_list':cla_list})

def addstudent(request):
    ret = {'status':True,'error':None}
    try:
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('classid')
        models.Student.objects.create(username=u,age=a,gender=g,cs_id=c)
    except Exception as e:
        ret['status'] = False
        ret['error'] = e
    import json
    return HttpResponse(json.dumps(ret))