from rest_framework.serializers import ModelSerializer
from .models import *

class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class WorkAttendanceSerializer(ModelSerializer):
    class Meta:
        model = WorkAttendance
        fields = "__all__"


class NoticeBoardSerializer(ModelSerializer):
    class Meta:
        model = NoticeBoard
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"