#Author:Santi
from django.shortcuts import HttpResponse,render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

INFO_LIST = []
for i in range(1, 900):
    dic = {'name': 'root' + str(i), 'age': str(i)}
    INFO_LIST.append(dic)

def fenye1(request):
    current_page = int(request.GET.get('p'))
    per_page_count = 10
    start = (current_page - 1) * per_page_count
    end = current_page * per_page_count
    info_list = INFO_LIST[start:end]
    prev_page = current_page - 1
    next_page = current_page + 1
    return render(request, 'fenye1.html', {'info_list':info_list,'prev_page':prev_page,'next_page':next_page})


class CustomPaginator(Paginator):
    def __init__(self,current_page,per_page_count,*args,**kwargs):
        self.current_page = int(current_page)
        self.per_page_count = int(per_page_count)
        super(CustomPaginator,self).__init__(*args,**kwargs)

    def range(self):
        part = int(self.per_page_count / 2) ###求出显示数量一半的值
        if self.num_pages < self.per_page_count: ###当总数少于显示数量时以总数为end；
            return range(1,self.num_pages)
        if self.current_page <= part:
            return range(1,self.per_page_count) ###当当前页面值低于part时，显示范围为1到显示数量；
        if self.current_page + part > self.num_pages:
            return range(self.num_pages - self.per_page_count + 1 ,self.num_pages + 1) ###如果当前页面+5大于总页数，则end为总页数，start为总页数-每页显示数 + 1
        return range(self.current_page - part, self.current_page + part + 1) ###其他情况都显示一半

def fenye2(request):
    current_page = request.GET.get('p')
    paginator = CustomPaginator(current_page,11,INFO_LIST,10)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
    except EmptyPage as e :
        posts = paginator.page(paginator.num_pages)
    return render(request,'fenye2.html',{'posts':posts})

def fenye3(request):
    from app01.views.fenyeClass import PagnatorCustom
    total_num = len(INFO_LIST) ### 数据总个数
    current_page = request.GET.get('p') ###当前页
    obj = PagnatorCustom(total_num,current_page) ###创建自定义分页类对象
    start = int(obj.start) ###起始位置
    end = int(obj.end) ###结束位置
    info_list = INFO_LIST[start:end] ###数据切片
    return render(request,'fenye3.html',{'info_list':info_list,'obj':obj})