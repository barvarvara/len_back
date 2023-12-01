from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from admin_app.models import Clients, Contacts, Products, Classes, Certificates
from admin_app.serializers import ClientSerializer, ProductSerializer, ClassSerializer, CertificateSerializer


class ClientsView(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


class ProductsView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ClassesView(ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer


class CertificateView(ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificateSerializer
