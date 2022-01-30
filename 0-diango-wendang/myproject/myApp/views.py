from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import *
from .serializers import SubjectSerializer
from rest_framework import viewsets

# from rest_framework.filters import OrderingFilter
from rest_framework import filters   # 过滤搜索

#  分页
from rest_framework.pagination import PageNumberPagination

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import json
import django_filters.rest_framework

# 集成封装好的

#  分页
class Pagesize(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500
    page_query_param = "page"

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = StudentSubject.objects.all()  #.order_by('-pk')
    serializer_class = SubjectSerializer


    # filter_backends = (filters.SearchFilter, filters.OrderingFilter,django_filters.rest_framework.DjangoFilterBackend,)   # 搜索排序
    search_fields = ('name', 'id',)
    ordering_fields = ('id', 'name')
    filter_fields = ['id', 'name', 'category']  # 过滤
    # 分页
    pagination_class = Pagesize
#
class TestViewSet(viewsets.ViewSet):

    def list(self, request):
        qs = StudentSubject.objects.all()
        serializer = SubjectSerializer(qs, many=True)
        return Response(serializer.data)

    def retrieve(self,requset,pk):
        try:
            qs = StudentSubject.objects.get(pk=pk)
        except StudentSubject.DoesNotExist:
            return Response({'message':'此数据为空'})

        serializer = SubjectSerializer(qs)
        return Response(serializer.data)

    def updata(self,requset,pk):
        try:
            qs = StudentSubject.objects.get(pk=pk)
        except StudentSubject.DoesNotExist:
            return Response({'message':'此数据为空'})

        data = requset.data
        print('ks')
        print(qs)

        serializer = SubjectSerializer(instance=qs, data=data, partial=True)

        print('put数据')
        print(serializer)
        print(serializer.is_valid())
        print("数据")
        # print(serializer.data)
        # print(serializer.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# class test(SubjectViewSet):
#     queryset = None
#     serializer_class = None
#     def __init__(self,queryset,serializer_class):
#         self.queryset = queryset
#         self.serializer_class = serializer_class
#
# a = test(StudentSubject.objects.all(),SubjectSerializer)
