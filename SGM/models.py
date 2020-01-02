from django.db import models
class Grade(models.Model):
    学号 = models.CharField(max_length=20, blank=True, null=True)
    课程名 = models.CharField(max_length=20, blank=True, null=True)
    成绩 = models.FloatField(blank=True, null=True)
    班级 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '成绩表'
# Create your models here.
