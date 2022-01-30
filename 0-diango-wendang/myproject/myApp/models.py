from django.db import models

# Create your models here.


class StudentSubject(models.Model):

    sub_category = (
        ('w', '文科'),
        ('l', '理科'),
        ('t', '通用'),
    )
    name = models.CharField(max_length=30, unique=True, db_column='name', verbose_name="科目名称" )  # lable="科目名称"
    create_time = models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name="创建时间")   # 创建时间
    update_time = models.DateTimeField(auto_now=True, db_column='update_time', verbose_name="更新时间")  # 更新时间
    img = models.ImageField(upload_to='StudentSubject', default=None,  db_column='img', verbose_name="封面", blank=True, null=True)
    total_points = models.DecimalField(max_digits=4, decimal_places=1, blank=False, verbose_name="总分")
    category = models.CharField(max_length=30,  choices=sub_category, verbose_name="分类")

    class Meta:
        db_table = 'student_subject'
        ordering = ['id']
        verbose_name = '学生科目'

    def __str__(self):
        return self.name



