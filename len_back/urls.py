from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.shortcuts import redirect
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from admin_app.views import ClientsViewSet, ClassesViewSet, CertificateViewSet, ProductsViewSet
from users_app.views import LoginViewSet, RegistrationViewSet, RefreshViewSet, UserViewSet, me_view

router = routers.DefaultRouter()

router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
# router.register(r'users', UserViewSet, basename='users')

router.register(r'clients', ClientsViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'certificates', CertificateViewSet)


def index(request):
    return redirect('api/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/auth/user/', me_view),
]

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

