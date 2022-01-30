from django.contrib import admin

# Register your models here.
from .models import StudentSubject

# admin.site.register(StudentSubject)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_time', 'update_time', 'img', 'total_points', 'category' )

    list_per_page = 5

    ordering = ('id',)
    # list_editable 设置默认可编辑字段

    #list_editable = ['machine_room_id', 'temperature']

    # 设置哪些字段可以点击进入编辑界面

    # list_display_links = ('id', 'caption')
# 在admin中注册绑定

admin.site.register(StudentSubject, SubjectAdmin)