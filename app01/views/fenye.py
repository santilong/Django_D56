#Author:Santi
from django.shortcuts import HttpResponse,render,redirect

INFO_LIST = []
for i in range(1, 999):
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


def fenye2(request):
    from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
    current_page = request.GET.get('p')
    paginator = Paginator(INFO_LIST,10)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
    except EmptyPage as e :
        posts = paginator.page(paginator.num_pages)
    return render(request,'fenye2.html',{'posts':posts})