from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth.views import LoginView



# Schema view for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API",
        default_version='v1',
        description="API for managing users, projects, tasks, and comments",
        contact=openapi.Contact(email="dkkundu00@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('v1/', include("project_management.urls")),
    

    # Swagger documentation
    path('documentations/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
     # JWT Token Authentication routes
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
