from django.db import models

# Create your models here.
from myApp.models import StudentSubject

# class StudentSubject(models.Model):
#     username = models.CharField(max_length=30, unique=True, db_column='username', verbose_name="用户名")


class Grade(models.Model):
    grade = models.CharField(max_length=30,unique=True,)
    def __str__(self):
        return self.grade

    class Meta:
        db_table = 'grade'
        ordering = ['id']
        verbose_name = '名次'

class User(models.Model):

    gender = (
        ('男', '男'),
        ('女', '女'),
    )
    username = models.CharField(max_length=30, unique=True, db_column='username', verbose_name="用户名")
    name = models.CharField(max_length=128, db_column='name', verbose_name="姓名", blank=True, null=True)
    password = models.CharField(max_length=256, db_column='password', verbose_name="密码")
    email = models.EmailField(unique=True, blank=True, null=True, db_column='email', verbose_name="电子邮箱")
    sex = models.CharField(max_length=32, choices=gender, default='男', db_column='sex', verbose_name="性别", blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, db_column='update_time', verbose_name="更新时间")  # 更新时间
    subjects = models.ManyToManyField(to=StudentSubject, related_name="subjects", blank=True, null=True, )
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True, related_name="user")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'
        ordering = ['id']
        verbose_name = '用户'
