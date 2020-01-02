from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from SGM.models import Grade
from SMM.models import Student
import os
import xlrd
from django.db import connection
def SGMView(request):
    print('SGM执行成功')
    return render(request, 'SGM.html', locals())


#录入学生信息
@csrf_exempt #增加装饰器，作为跳过csrf中间件的保护
def insert_message(request):
        print('insert_message执行成功')
        print(request.POST)
        request.encoding = 'utf-8'
        file_name = request.POST['inputfile']
        if file_name:
            print('批量插入')
            print(os.getcwd() + '\\assets' + '\\' + file_name)
            path = os.getcwd() + '\\assets' + '\\' + file_name
            ex_file = xlrd.open_workbook(path)
            sheet = ex_file.sheet_by_name('Sheet1')
            for item in range(1, sheet.nrows):
                print(sheet.row_values(item))
                content = sheet.row_values(item)
                print(content)
                grade = Grade()
                grade.班级 = content[0]
                grade.学号 = content[1]
                grade.成绩 = content[2]
                grade.课程名 = content[3]
                grade.save()
        else:
            print('单条插入')
            print(request.POST)
            grade = Grade()
            grade.学号 = request.POST['num'].strip()
            grade.班级 = request.POST['num'][0:7].strip()
            grade.成绩 = float(request.POST['grade'])
            grade.课程名 = request.POST['CG']
            grade.save()

        return render(request, 'SMM.html', locals())

# #删除学生信息
@csrf_exempt #增加装饰器，作为跳过csrf中间件的保护
def delete_message(request):
    try:
        request.encoding = 'utf-8'
        stunum = request.POST["del_first"]
        course = request.POST["CD"]
        Grade.objects.filter(学号=stunum, 课程名=course).delete()
        print("删除" + stunum + course + "成功")
    except Exception:
        print(repr(Exception))
    return render(request, 'SMM.html', locals())



#查找学生选修课程
def get_class(request):
    num = request.POST['num']
    print(num[0:7], request.POST)       #学号字典
    cursor = connection.cursor()
    query = "select 班级课程表.课程号,课程表.课程名 from 课程表,班级课程表 where 课程表.课程号=班级课程表.课程号 and 班级课程表.班级 =" + num[0:7]
    cursor.execute(query)
    rows = cursor.fetchall()
    lists = []
    for i in range(len(rows)):
        lists.append(rows[i])
    ans = {'ans': lists}
    return HttpResponse(ans.values())
    #根据学号查找学生所在班级，根据班级查找班级所选课程



#获取学生成绩
def get_grade(request):
    num = request.POST['num']
    course = request.POST['course']
    grade = Grade.objects.filter(学号=num, 课程名=course).values('成绩')
    ans = {'ans':list(grade)}
    return HttpResponse(ans.values())




#获取可以删除成绩的科目
def get_delete(request):
    print('get_delete 运行成功')
    print(request.POST)
    num = request.POST['num']
    projects = Grade.objects.filter(学号= num).values('课程名')
    print(projects)
    ans = {'ans':list(projects)}
    return HttpResponse(ans.values())