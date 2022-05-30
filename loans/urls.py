from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("loans", views.LoanVieSet, basename="loans")
router.register("loan-payments", views.LoanPaymentViewSet, basename="loan-payments")

urlpatterns = [ 
    path("", include(router.urls)),
]