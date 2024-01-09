"""
URL configuration for len_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.shortcuts import redirect
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from admin_app.views import ClientsView, ClassesView, CertificateView, ProductsView, ClientContactsView
from users_app.views import LoginViewSet, RegistrationViewSet, RefreshViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'users', UserViewSet, basename='users')

router.register(r'clients', ClientsView)
router.register(r'client-contacts', ClientContactsView,  basename='client-contacts')

router.register(r'products', ProductsView)
router.register(r'classes', ClassesView)
router.register(r'certificates', CertificateView)


def index(request):
    return redirect('api/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include(router.urls)),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
]
