from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from SMM.models import Student
import os
import xlrd
import pymysql
def SMMView(request):
    print('SMM执行成功')
    return render(request, 'SMM.html', locals())


#录入学生信息
@csrf_exempt #增加装饰器，作为跳过csrf中间件的保护
def insert_message(request):
    request.encoding = 'utf-8'
    try:
        file_name = request.POST['inputfile']
        if file_name:
            print(os.getcwd() + '\\assets' + '\\' + file_name)
            path = os.getcwd() + '\\assets' + '\\' + file_name
            ex_file = xlrd.open_workbook(path)
            sheet = ex_file.sheet_by_name('Sheet1')
            for item in range(1, sheet.nrows):
                print(sheet.row_values(item))
                content = sheet.row_values(item)
                student = Student()
                student.姓名 = content[1]
                student.学号 = content[0]
                student.年龄 = content[3]
                student.性别 = content[2]
                student.状态 = '正常'
                student.save()
        else:
            student = Student()
            student.姓名 = request.POST['name']
            student.学号 = request.POST['num']
            student.年龄 = request.POST['age']
            student.性别 = request.POST['sex']
            student.状态 = '正常'
            student.save()
    except Exception:
        print(Exception)
    return render(request, 'SMM.html', locals())

#删除学生信息
@csrf_exempt #增加装饰器，作为跳过csrf中间件的保护
def delete_message(request):
    try:
        request.encoding = 'utf-8'
        stunum = request.POST["del_first"]
        Student.objects.filter(学号=stunum).delete()
        print("删除" + stunum + "成功")
    except Exception:
        print(repr(Exception))
    return render(request, 'SMM.html', locals())



#修改学生信息
@csrf_exempt #增加装饰器，作为跳过csrf中间件的保护
def change_message(request):
    try:
        student = Student()
        student.姓名 = request.POST['oname']
        student.学号 = request.POST['onum']
        student.年龄 = request.POST['oage']
        student.性别 = request.POST['osex']
        student.状态 = request.POST['ostatus']
        student.save()
        context = {'target':2, 'ans':'修改成功'}
        return render(request, 'SMM.html', context)
    except Exception:
        print(repr(Exception))
        context = {'target':2, 'ans': '修改失败'}
        return render(request, 'SMM.html', context)


#查找学生信息
@csrf_exempt #增加装饰器，作为跳过csrf中间件的保护
def find_message(request):
    try:
        stunum = request.POST["mul"]
        student = Student.objects.get(学号 = stunum)
        context = {'target':1, 'name':student.姓名, 'age':student.年龄, 'sex':student.性别, 'status':student.状态, 'num':student.学号}
        return render(request, 'SMM.html', context)
    except Exception:
        print(repr(Exception))
        context = {'target': 0}
        return render(request, 'SMM.html', context)
