from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . serializers import *
from .models import *
# Create your views here.
class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class WorkAttendanceViewSet(ModelViewSet):
    queryset = WorkAttendance.objects.all()
    serializer_class = WorkAttendanceSerializer


class NoticeBoardViewSet(ModelViewSet):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer