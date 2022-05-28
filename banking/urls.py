from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("accounts", views.AccountViewSet, basename="accounts")
router.register("transactions", views.TransactionViewSet, basename="transactions")

urlpatterns = [ 
    path("", include(router.urls)),
    path("customer-deposit/", views.CustomerDepositAPIView.as_view(), name="customer-deposit"),
    path("customer-withdraw/", views.CustomerWithdrawAPIView.as_view(), name="customer-withdraw"),
    path("money-transfer/", views.MoneyTransferAPIView.as_view(), name="money-transfer"),
]