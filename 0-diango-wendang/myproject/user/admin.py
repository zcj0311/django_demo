from django.contrib import admin

# Register your models here.
from .models import User,Grade

# admin.site.register(StudentSubject)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'password', 'email', 'sex', 'create_time', 'update_time',)

    list_per_page = 10

    ordering = ('id',)
    # list_editable 设置默认可编辑字段

    #list_editable = ['machine_room_id', 'temperature']

    # 设置哪些字段可以点击进入编辑界面

    # list_display_links = ('id', 'caption')
# 在admin中注册绑定

admin.site.register(User, UserAdmin)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade',)

    list_per_page = 10

    ordering = ('id',)
    # list_editable 设置默认可编辑字段

    #list_editable = ['machine_room_id', 'temperature']

    # 设置哪些字段可以点击进入编辑界面

    # list_display_links = ('id', 'caption')
# 在admin中注册绑定

admin.site.register(Grade, GradeAdmin)