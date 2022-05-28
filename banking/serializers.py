from rest_framework.serializers import ModelSerializer
from .models import Account, Transaction

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"