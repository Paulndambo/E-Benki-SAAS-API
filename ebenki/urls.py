from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="E-BENKI SERVICE API",
      default_version='v1',
      description="e-Benki is a banking a service platform😂",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("users.urls")),
    path("core/", include("core.urls")),
    path("customer/", include("customers.urls")),
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "E-BENKI SERVICE API"
admin.site.site_title = "E-BENKI SERVICE API"
admin.site.index_title = "E-BENKI SERVICE API"