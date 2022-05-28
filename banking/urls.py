from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("accounts", views.AccountViewSet, basename="accounts")
router.register("transactions", views.TransactionViewSet, basename="transactions")

urlpatterns = [ 
    path("", include(router.urls)),
]