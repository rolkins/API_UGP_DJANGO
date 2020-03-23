from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'task', views.TaskViewSet, base_name="task_list")
router.register(r'subtask', views.SubTaskViewSet)
router.register(r'department', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^ugp/', include(router.urls)),
    url(r'^report/$', views.LoadReportView.as_view()),
]
