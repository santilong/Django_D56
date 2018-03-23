#Author:Santi
from django.shortcuts import render,HttpResponse,redirect
from app01 import models

def students(request):
    stu_list = models.Student.objects.all()
    cla_list = models.Classes.objects.all()
    return render(request,'students.html',{'stu_list':stu_list,'cla_list':cla_list})

def addstudent(request):
    ret = {'status':True,'error':None,'data':None}
    try:
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('classid')
        obj = models.Student.objects.create(username=u,age=a,gender=g,cs_id=c)
        ret['data'] = obj.id
    except Exception as e:
        ret['status'] = False
        ret['error'] = e
    import json
    return HttpResponse(json.dumps(ret))

def delstudent(request):
    ret = {'status': True, 'error': None}
    print(request.POST)
    try:
        nid = int(request.POST.get('nid'))
        models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status'] = False
        ret['error'] = str(e)
    import json
    return HttpResponse(json.dumps(ret))


