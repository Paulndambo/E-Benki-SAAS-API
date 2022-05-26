from rest_framework.serializers import ModelSerializer
from .models import *

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerEmploymentSerializer(ModelSerializer):
    class Meta:
        model = CustomerEmployment
        fields = "__all__"