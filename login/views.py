import pymysql as pymysql
from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from login import models

user_list = []


@csrf_exempt
def index(request):
    # return HttpResponse('Hello World!')
    # return render(request, 'index.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        # temp = {'user' : username, 'pwd' : password}
        # user_list.append(temp)
        models.UserInfo.objects.create(user=username, pwd=password)

    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})

words_list=[]


# def mvp(request):
#     if request.method == 'POST':
#         host = request.POST.get('host')
#         port = request.POST.get('port')
#         db = request.POST.get('db')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#     db = pymysql.connect(host=host, port=port, user=username, passwd=password, db=db, charset="utf8",
#                               autocommit=True, cursorclass=pymysql.cursors.DictCursor)
#     cursor = db.cursor()
#     sql_1 = ""
#     cursor.execute(sql_1)
#     data_1 = cursor.fetchall()
#     temp = {'unfinsh': data_1}
#     words_list.append(temp)
#
#     return render(request, 'mvp.html', {'data': words_list})
