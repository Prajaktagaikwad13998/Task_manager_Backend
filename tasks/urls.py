from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('tasks/', TaskListAPIView.as_view(), name='api-task-list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),]