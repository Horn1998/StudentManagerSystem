from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from CC.models import Class
import json
from xlrd import open_workbook
from xlutils.copy import copy
def SGQView(request):
    #表示未选课班级
    print('SGQView 执行成功')
    clist = Class.objects.all().values('班级', '年级')
    return render(request, 'SGQ.html', {'clist': list(clist)})



#根据学期查询学生成绩
def find_message(request):
    print('get_message 执行成功')
    print(request.POST)
    num = request.POST['nums']
    choicetype = request.POST['choicetype']
    cursor = connection.cursor()
    query = 'select 成绩表.课程名,成绩表.成绩 from 成绩表,学期序号表,课程表 where 成绩表.课程名=课程表.课程名 and 学期序号表.序号=课程表.学期序号 and 学期序号表.序号=' + choicetype +' and 成绩表.学号=' + num +';'
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    context = {'ans': rows}
    return HttpResponse(json.dumps(context), content_type="application/json")

# Create your views here.
#查找学生选修课程
def get_class(request):
    print('get_class 执行成功')
    num = request.POST['class']
    cursor = connection.cursor()
    query = "select 班级课程表.课程号,课程表.课程名 from 课程表,班级课程表 where 课程表.课程号=班级课程表.课程号 and 班级课程表.班级 =" + num.strip()
    cursor.execute(query)
    rows = cursor.fetchall()
    lists = []
    print(rows)
    for i in range(len(rows)):
        lists.append(rows[i])
    ans = {'ans': lists}
    return HttpResponse(ans.values())
    #根据学号查找学生所在班级，根据班级查找班级所选课程



def find_class(request):
    print('find_class执行成功')
    course = request.POST['classtype']
    cursor = connection.cursor()
    query = "select 学号,课程表.课程名,成绩, 学分 from 成绩表,课程表 where 班级=" + course +" and 成绩表.课程名=课程表.课程名;"
    cursor.execute(query)
    rows = cursor.fetchall()

    query = "select 班级课程表.课程号,课程表.课程名 from 课程表,班级课程表 where 课程表.课程号=班级课程表.课程号 and 班级课程表.班级 =" + course.strip()
    cursor.execute(query)
    query = cursor.fetchall()  #相关课程
    dicts = {}
    head = []
    #获取头部以及它的位置
    for index in range(len(query)):
        head.append(query[index][1])
    for item in rows:
        dicts.setdefault(item[0], [])
        dicts[item[0]].append([item[1], item[2], item[3]])
    total, tot= 0, 0
    count = {}
    for item in dicts.items():
        for i in item[1]:
            total += i[1] * i[2]
        dicts[item[0]].append(total)
        count[tot] = total
        tot += 1
        total = 0
    # lt = list(count.items())
    # lt.sort(key=lambda  x:x[1], reverse = True)
    # SORT = []
    # for item in lt:
    #     SORT.append(item[0])
    # keys = []
    # for key in dicts:
    #     keys.append(key)
    # temp = []
    # for i in SORT:
    #     temp.append(keys[i])
    # keys = {}
    # for key in temp:
    #     keys[key] = dicts[key]
    # print(SORT)
    for item in dicts:
        temp = []
        for h in head:
            judge = 0
            for item2 in dicts[item][:-1]:
                if item2[0] == h:
                    judge = 1
                    temp.append(item2)
            if judge == 0:
                temp.append(['', 0, 1])
        count = dicts[item][-1]
        temp.append(['', count, 1])
        dicts[item] = temp
    return HttpResponse(json.dumps(dicts), content_type="application/json")



def export(request):
    print('find_class执行成功')
    course = request.POST['classtype']
    cursor = connection.cursor()
    query = "select 学号,课程表.课程名,成绩, 学分 from 成绩表,课程表 where 班级=" + course + " and 成绩表.课程名=课程表.课程名;"
    cursor.execute(query)
    rows = cursor.fetchall()

    query = "select 班级课程表.课程号,课程表.课程名 from 课程表,班级课程表 where 课程表.课程号=班级课程表.课程号 and 班级课程表.班级 =" + course.strip()
    cursor.execute(query)
    query = cursor.fetchall()  # 相关课程
    dicts = {}
    head = []
    # 获取头部以及它的位置
    for index in range(len(query)):
        head.append(query[index][1])
    for item in rows:
        dicts.setdefault(item[0], [])
        dicts[item[0]].append([item[1], item[2], item[3]])
    total, tot = 0, 0
    count = {}
    for item in dicts.items():
        for i in item[1]:
            total += i[1] * i[2]
        dicts[item[0]].append(total)
        count[tot] = total
        tot += 1
        total = 0
    for item in dicts:
        temp = []
        for h in head:
            judge = 0
            for item2 in dicts[item][:-1]:
                if item2[0] == h:
                    judge = 1
                    temp.append(item2)
            if judge == 0:
                temp.append(['', 0, 1])
        count = dicts[item][-1]
        temp.append(['', count, 1])
        dicts[item] = temp
    content = []
    temp = []
    temp.append('学号')
    for item in query:
        temp.append(item[1])
    temp.append('总和')
    content.append(temp)
    temp = []
    for key in dicts:
        temp.append(key)
        for i in dicts[key]:
            temp.append(i[1])
        content.append(temp)
        temp = []
    print(content)
    rb = open_workbook('D:\\1.xls')
    # 通过sheet_by_index()获取的sheet没有write()方法
    rs = rb.sheet_by_index(0)
    wb = copy(rb)
    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(0)
    for i in range(len(content)):
        for j in range(len(content[0])):
            ws.write(i, j, str(content[i][j]))
    wb.save('D:\\1.xls')
    return HttpResponse("6666")


