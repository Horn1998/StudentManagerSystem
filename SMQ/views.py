from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json
def SMQView(request):
    return render(request,'SMQ.html',locals())
# Create your views here.

@csrf_exempt #增加装饰器，作为跳过csrf中间件的保护
def find_message(request):
    query_dict = dict(request.POST)
    print(query_dict)
    cursor = connection.cursor()
    query = "select * from 基本信息表 where"
    if query_dict['num'][0] != '':
        query += " 学号 = '" + query_dict['num'][0] + "' and "
    if query_dict['sex'][0] != '':
        query += " 性别 = '" + query_dict['sex'][0] + "' and "
    if query_dict['age'][0] != '':
        query += " 年龄 = " + query_dict['age'][0] + " and "
    if query_dict['name'][0] != '':
        query += " 姓名 = '" + query_dict['name'][0] + "' and "
    if query_dict['status'][0] != '':
        query += " 状态 = '" + query_dict['status'][0] + "' and "
    query += ' 1 = 1;'
    cursor.execute(query)
    rows = cursor.fetchall()
    context = {'ans':json.dumps(rows), 'target': 0}
    return render(request, 'SMQ.html', context)

