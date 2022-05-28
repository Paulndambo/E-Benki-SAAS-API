from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer, WithdrawSerializer, DepositSerializer, TransferSerializer
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



class CustomerDepositAPIView(generics.GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = DepositSerializer


    def post(self, request):
        type = request.data['type']
        account = get_object_or_404(Account, pk=request.data['account'])
        if type == 'deposit':
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                account.balance = account.balance + serializer.data['amount']
                account.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"failed": "This can only be a deposit transaction"}, status=status.HTTP_400_BAD_REQUEST)
        

class CustomerWithdrawAPIView(generics.GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = WithdrawSerializer


    def post(self, request):
        type = request.data['type']
        account = get_object_or_404(Account, pk=request.data['account'])
        if type == 'withdraw':
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                balance = account.balance
                if balance > request.data['amount']:
                    serializer.save()
                    account.balance = account.balance - serializer.data['amount']
                    account.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response({"failed": "You cannot withdraw more than your balance, try a lower amount please"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"failed": "This can only be a withdraw transaction"}, status=status.HTTP_400_BAD_REQUEST)
 
    
class MoneyTransferAPIView(generics.GenericAPIView):
    serializer_class = TransferSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        account_to = request.data['account_to']
        account_from = request.data['account_from']
        amount = request.data['amount']
        
        sender = get_object_or_404(Account, pk=account_from)
        receiver = get_object_or_404(Account, pk=account_to)
        serializer.is_valid(raise_exception=True)

        #update sender's balance
        sender.balance = sender.balance - amount
        sender.save()

        #update receiver's balance
        receiver.balance = receiver.balance + amount
        receiver.save()

        return Response(serializer.data)