
from rest_framework import serializers
from .models import *


# 完全没有验证的
class PutUserSerializer(serializers.ModelSerializer):
    # grade = serializers.SerializerMethodField()
    # subjects = serializers.SerializerMethodField()
    #
    # def get_grade(self, obj):
    #     if obj.grade:
    #         return obj.grade.grade
    #     return None
    #
    # def get_subjects(self, obj):
    #     if obj.subjects:
    #         subject_list = []
    #         for dept in obj.subjects.values():
    #             # 自定义关联表查询
    #             # print("循序数据")
    #             # print(dept)
    #             # print(dept['name'])
    #             subject_list.append(dept)
    #         return subject_list
    #     return None

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ['password']
        # depth = 2
        # extra_kwargs = {
        #     'grade': {
        #         'read_only': False
        #     }
        # }

class GetUserSerializer(serializers.ModelSerializer):
    # grade = serializers.SerializerMethodField()
    # subjects = serializers.SerializerMethodField()
    #
    # def get_grade(self, obj):
    #     if obj.grade:
    #         return obj.grade.grade
    #     return None
    #
    # def get_subjects(self, obj):
    #     if obj.subjects:
    #         subject_list = []
    #         for dept in obj.subjects.values():
    #             # 自定义关联表查询
    #             # print("循序数据")
    #             # print(dept)
    #             # print(dept['name'])
    #             subject_list.append(dept)
    #         return subject_list
    #     return None

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password']
        depth = 2
        # extra_kwargs = {
        #     'grade': {
        #         'read_only': False
        #     }
        # }


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

