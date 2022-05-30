from django.db import models
from banking.models import Account
from customers.models import Customer
# Create your models here.
CARD_TYPES = (
    ("visa", "Visa"),
    ("mastercard", "Mastercard"),
    ("ebenkicard", "E-Benki Card"),
)

class Card(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=50)
    cve = models.CharField(max_length=20)
    expiry = models.CharField(max_length=5)
    balance = models.FloatField(default=0)
    type = models.CharField(max_length=200, choices=CARD_TYPES)