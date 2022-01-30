from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('grade', GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),

]