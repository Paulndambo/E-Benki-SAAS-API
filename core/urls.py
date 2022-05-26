from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register("branches", views.BranchViewSet, basename="branches")
router.register("departments", views.DepartmentViewSet, basename="departments")
router.register("positions", views.PositionViewSet, basename="positions")
router.register("employees", views.EmployeeViewSet, basename="employees")
router.register("work-attendances", views.WorkAttendanceViewSet, basename="work-attendances")
router.register("notice-boards", views.NoticeBoardViewSet, basename="notice-boards")
router.register("tasks", views.TaskViewSet, basename="tasks")

urlpatterns = [ 
    path("", include(router.urls)),
]