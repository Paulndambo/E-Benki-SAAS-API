from django.shortcuts import render
from .models import Loan, LoanPayment
from .serializers import LoanPaymentSerializer, LoanSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class LoanVieSet(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanPaymentViewSet(ModelViewSet):
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer