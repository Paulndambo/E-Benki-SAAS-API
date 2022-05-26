from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("customers", views.CustomerViewSet, basename="customers")
router.register("customers-employment", views.CustomerEmploymentViewSet, basename="customers-employment")

urlpatterns = [ 
    path("", include(router.urls)),
]