from django.db import models
from core.models import AbstractBaseModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
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
    scanned_id = models.FileField(upload_to="scanned_ids")
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


@receiver(post_save, sender=Customer)
def create_customer_user(sender, instance, **kwargs):
    if instance.email:
        email = instance.email
        username = instance.id_number
        password = "1234"
        user = User()
        user.email = email
        user.username = username
        user.set_password(password)
        user.save()
