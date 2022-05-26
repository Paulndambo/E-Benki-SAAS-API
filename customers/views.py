from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from . models import *
# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerEmploymentViewSet(ModelViewSet):
    queryset = CustomerEmployment.objects.all()
    serializer_class = CustomerEmploymentSerializer