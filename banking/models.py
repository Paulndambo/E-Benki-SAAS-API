from django.db import models
from customers.models import Customer
from core.models import Branch, AbstractBaseModel
# Create your models here.
ACCOUNT_TYPES = (
    ("savings", "Savings Account"),
    ("checking", "Checking Account"),
)

class Account(AbstractBaseModel):
    account_number = models.CharField(max_length=200, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    account_type = models.CharField(max_length=200, choices=ACCOUNT_TYPES)
    balance = models.FloatField(default=0)


    def __str__(self):
        return self.account_number

TRANSACTION_TYPES = (
    ("deposit", "Deposit"),
    ("withdraw", "Withdraw"),
)

class Transaction(AbstractBaseModel):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=200, choices=TRANSACTION_TYPES)
    amount = models.FloatField(default=0)


    def __str__(self):
        return self.account.account_number
