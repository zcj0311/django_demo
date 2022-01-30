
from rest_framework import serializers
from .models import *

# 完全没有验证的
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubject
        fields = '__all__'


