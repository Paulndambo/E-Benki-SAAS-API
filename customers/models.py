from django.db import models
from core.models import AbstractBaseModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
    ("binary", "Binary"),
)

class Customer(AbstractBaseModel):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    phone_number = PhoneNumberField(unique=True)
    id_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    country = CountryField()
    photo = models.ImageField(upload_to="customer_images")
    scanned_id = models.ImageField(upload_to="scanned_ids")
    branch = models.ForeignKey(to="core.Branch", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

SECTOR_CHOICES = (
    ("private", "Private"),
    ("public", "Public"),
    ("other", "Other"),
)

WORK_TYPES = (
    ("full_time", "Full Time"),
    ("part_time", "Part Time"),
    ("freelance", "Freelance"),
    ("self_employed", "Self-Employed"),
    ("remote", "Remote"),
)

class CustomerEmployment(AbstractBaseModel):
    title = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    employer = models.CharField(max_length=200)
    sector = models.CharField(max_length=200, choices=SECTOR_CHOICES)
    work_type = models.CharField(max_length=200, choices=WORK_TYPES)
    salary = models.FloatField(default=0)

    def __str__(self):
        return self.title

    