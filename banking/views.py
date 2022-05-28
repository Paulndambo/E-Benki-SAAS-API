from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser
from customers.models import Customer
# Create your views here.
class AccountViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CustomerTransactionAPIView(generics.GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, pk=customer_id)
        transactions = Transaction.objects.filter(customer=customer)
        serializer = self.serializer_class(instance=transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    