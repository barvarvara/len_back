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
from django.urls import path
from rest_framework import routers
from admin_app.views import ClientsView, ProductsView, ClassesView, CertificateView

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'api/clients', ClientsView)
router.register(r'api/clients/<int:pk>', ClientsView)

router.register(r'api/products', ProductsView)
router.register(r'api/products/<int:pk>', ProductsView)

router.register(r'api/classes', ClassesView)
router.register(r'api/classes/<int:pk>', ClassesView)

router.register(r'api/certificates', CertificateView)
router.register(r'api/classes/<int:pk>', CertificateView)

urlpatterns += router.urls
