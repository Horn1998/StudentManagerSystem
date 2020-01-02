from django.shortcuts import render
from CC.models import Class, Course, CCC
from django.http import HttpResponse
import json
def CCView(request):
    #表示未选课班级
    clist = Class.objects.filter(状态='0').values('班级', '年级')
    return render(request, 'CC.html', {'clist': list(clist)})


#获取课程列表
def get_Courses(request):
    cla = request.POST['class']

    scale = Class.objects.filter(班级 =cla.strip()).values('年级')[0]['年级']
    print(scale)
    scale = [int(scale) * 2 - 1, int(scale) * 2]
    course_up = Course.objects.filter(学期序号='0'+str(scale[1])).values('课程名','课程号')
    course_down =  Course.objects.filter(学期序号='0'+str(scale[0])).values('课程名','课程号')
    context = {'course':list(course_down) + list(course_up)}
    print(context)
    return HttpResponse(context.values())


#班级选课
def CCS(request):
    print(request.POST)
    ccc = CCC()
    ccc.课程号 = request.POST['CCO']
    ccc.班级 = request.POST['CCL']
    ccc.save()
    return render(request, 'CC.html', locals())
# Create your views here.
