from django.db import models
from customers.models import Customer
from core.models import AbstractBaseModel
# Create your models here.
LOAN_STATUSES = (
    ("awarded", "Awarded"),
    ("declined", "Declined"),
    ("defaulted", "Defaulted"),
    ("paid", "Paid"),
)

class Loan(AbstractBaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount_applied = models.FloatField(default=0)
    amount_awarded = models.FloatField(default=0)
    status = models.CharField(max_length=50, choices=LOAN_STATUSES)
    decline_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.customer.name


class LoanPayment(AbstractBaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

    def __str__(self):
        return self.customer.name
