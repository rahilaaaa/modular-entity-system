from django.contrib import admin
from django.urls import path, include

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Modular Entity API",
        default_version="v1",
        description="Vendor Product Course Certification Mapping APIs",
    ),
    public=True,
    permission_classes=[AllowAny],
)


urlpatterns = [

    # Admin
    path("admin/", admin.site.urls),

    # Master entity APIs
    path("api/", include("vendor.urls")),
    path("api/", include("product.urls")),
    path("api/", include("course.urls")),
    path("api/", include("certification.urls")),

    # Mapping APIs
    path("api/", include("vendor_product_mapping.urls")),
    path("api/", include("product_course_mapping.urls")),
    path("api/", include("course_certification_mapping.urls")),

    # Swagger Documentation
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),

    # ReDoc Documentation
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
]