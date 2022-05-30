from rest_framework.serializers import ModelSerializer
from .models import Loan, LoanPayment

class LoanSerializer(ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"


class LoanPaymentSerializer(ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = "__all__"