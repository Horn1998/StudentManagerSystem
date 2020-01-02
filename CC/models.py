from django.db import models
#班级表
class Class(models.Model):
    班级 = models.CharField(primary_key=True, max_length=20)
    最高人数 = models.IntegerField(blank=True, null=True)
    专业 = models.CharField(max_length=50, blank=True, null=True)
    状态 = models.CharField(max_length=2, blank=True, null=True)
    年级 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '班级表'

#课程类型表
class CourseType(models.Model):
    课程类型 = models.CharField(max_length=10, blank=True, null=True)
    课程号 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '课程类型表'

#班级选课表
class CCC(models.Model):
    班级 = models.CharField(max_length=20, blank=True, null=True)
    课程号 =  models.CharField(max_length=10, blank=True, null=True)
    平均分 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '班级课程表'

class Semster(models.Model):
    学期号 = models.CharField(max_length=20, blank=True, null=True)
    序号 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '学期序号表'



#课程表
class Course(models.Model):
    课程号 = models.CharField(max_length=10, blank=True, null=True)
    课程名 = models.CharField(max_length=20, blank=True, null=True)
    学分 = models.FloatField(blank=True, null=True)
    类型 = models.ForeignKey(CourseType, models.DO_NOTHING, db_column='类型', blank=True, null=True)
    学期序号 = models.ForeignKey(Semster, models.DO_NOTHING, db_column='学期序号', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '课程表'

# Create your models here.
