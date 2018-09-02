from django.shortcuts import render

# Create your views here.


USER_LIST = []

for i in range(1,999):
    row = 'root'+ str(i)+'-'+str(i)
    USER_LIST.append(row)




def index(request):
    data_list = USER_LIST
    max_row = 10 #每页显示多少行
    max_page = 5 #页码显示多少页
    current = request.GET.get('p',1)
    count = len(data_list)
    pages = count//max_row
    current = int(current)
    start = (current-1)*max_row
    end = current*max_row
    new_USER_LIST = data_list[start:end]
    if current <=1:
        prev_page = 1
    else:
        prev_page = current-1
    if current >= pages+1:
        next_page = current
    else:
        next_page = current+1

    if current ==1:
        page_list = range(1,pages+2)[0:max_page]

    elif current >= pages:
        page_list = range(1,pages+2)[pages:pages+max_page]
    else:
        page_list = range(1,pages+2)[current:current+max_page]

    return render(request,'paging_index.html',{'user_list':new_USER_LIST,
                                               'prev_page':prev_page,
                                               'next_page':next_page,
                                               'page_list':page_list,
                                               'current':current,
                                               'pages':pages+1})