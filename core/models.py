from audioop import maxpp
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Branch(AbstractBaseModel):
    code = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    country = CountryField()
    
    def __str__(self):
        return self.name


GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
    ("binary", "Binary"),
)

class Department(AbstractBaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


class Position(AbstractBaseModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Employee(AbstractBaseModel):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    phone_number = PhoneNumberField()
    id_number = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    email = models.EmailField()
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    country = CountryField()
    date_employed = models.DateField(auto_now=True)
    contract_end_date = models.DateField(null=True)
    salary = models.FloatField(default=0)

    def __str__(self):
        return self.name


class WorkAttendance(AbstractBaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(null=True)
    check_out_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.employee.name


class NoticeBoard(AbstractBaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField()
    date_due = models.DateTimeField()

    def __str__(self):
        return self.title

TASK_STAGES = (
    ("todo", "Todo"),
    ("in_progress", "In Progress"),
    ("review", "Review"),
    ("done", "Done")
)

class Task(AbstractBaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    stage = models.CharField(max_length=200, choices=TASK_STAGES)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="task_creators")
    assigned_to = models.ForeignKey(Employee, related_name="assignees", on_delete=models.CASCADE)
    date_due = models.DateTimeField()

    def __str__(self):
        return self.title
