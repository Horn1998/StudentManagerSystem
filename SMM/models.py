from django.db import models
#python manage.py inspectdb
#学生信息基本表
class Student(models.Model):
    学号 = models.CharField(primary_key=True, max_length=30)
    姓名 = models.CharField(max_length=30, blank=True, null=True)
    性别 = models.CharField(max_length=5, blank=True, null=True)
    年龄 = models.IntegerField(blank=True, null=True)
    状态 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '基本信息表'



# Create your models here.
