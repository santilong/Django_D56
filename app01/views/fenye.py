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
    return render(request, 'fenye1.html', {'info_list':info_list})


