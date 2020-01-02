from django.shortcuts import render
from django.db import connection
from SMM.models import Student
import json
def SpecialView(request):

    return render(request, 'Special.html', locals())

def special_process(request):
    print(request.POST)
    choice = request.POST['choice']
    if choice[0] == 1:
        Student.objects.filter(学号=request.POST['num1']).update(状态='休学')
    if choice[0] == 2:
        Student.objects.filter(学号=request.POST['num1']).update(状态='留级')
    if choice[0] == 3:
        Student.objects.filter(学号=request.POST['num1']).update(状态='正常')
    return render(request, 'Special.html', locals())
# Create your views here.
