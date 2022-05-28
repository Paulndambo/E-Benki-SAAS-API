from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Account, Transaction
from django.utils import timezone

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class WithdrawSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"



class DepositSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class TransferSerializer(serializers.Serializer):
    account_from = serializers.IntegerField(required=True)
    account_to = serializers.IntegerField(required=True)
    amount = serializers.FloatField(required=True)
    transacted_at = serializers.DateTimeField(default=timezone.now)