from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import *
from .serializers import GetUserSerializer, PutUserSerializer, GradeSerializer
from rest_framework.views import APIView
# from django_filters.rest_framework import DjangoFilterBackend
# import django_filters
from rest_framework import viewsets
from rest_framework import views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters   # 过滤搜索
import hashlib
#  分页
from rest_framework.pagination import PageNumberPagination
# 集成封装好的


def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

class Pagesize(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500
    page_query_param = "page"

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    filter_fields = ['id', 'name', 'sex', 'grade']  # 过滤 'subjects', 'grade'
    # filter_backends = (filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)   # 搜索排序
    search_fields = ('id', 'name', 'sex', 'subjects__name', 'grade__grade')
    ordering_fields = ('id', 'name', 'sex', )
    # 分页
    pagination_class = Pagesize

    def get_serializer_class(self):
        method = self.request.method
        if method == 'GET':
            return GetUserSerializer
        else:
            return PutUserSerializer

    # @action(methods=['put'], detail=True)
    # def put_data(self, request, pk):
    #     # print(pk)
    #     # return JsonResponse({'text': pk})
    #
    #     try:
    #         qs = User.objects.get(pk=pk)
    #     except User.DoseNotExist:
    #         return Response({'message':'此数据为空'})
    #
    #     data = requset.data
    #     print('ks')
    #     print(qs)
    #
    #     serializer = SubjectSerializer(instance=qs, data=data, partial=True)
    #
    #     print('put数据')
    #     print(serializer)
    #     print(serializer.is_valid())
    #     print("数据")
    #     # print(serializer.data)
    #     # print(serializer.data)
    #
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

class Login(APIView):
    queryset = None
    serializer_class = None

    def post(self, request):
        print("post函数")
        # print(request.data)
        # print(request.data.get('username'))
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        print(password)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'message': '此用户不存在'})

        if user.password == password:
            print("哈希值")
            qs = hash_code(password)
            print(qs)
            sq = hash_code(qs)
            print("中间过程")
            print(sq)
            return JsonResponse({'message': '登录成功'})

        # serializer = SubjectSerializer(qs)
        # return Response(serializer.data)
        print(user)
        serializer = GetUserSerializer(instance=user)
        return JsonResponse({'message': '密码不正确'})

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_fields = ['id', 'grade']  # 过滤
    # filter_backends = (filters.SearchFilter, filters.OrderingFilter,)   # 搜索排序
    search_fields = ('id', 'grade')
    ordering_fields = ('id', 'grade')
    # 分页
    pagination_class = Pagesize

