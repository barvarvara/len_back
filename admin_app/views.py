from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from admin_app.models import Clients, Contacts, Classes, Certificates, Products
from admin_app.serializers import ClientSerializer, ClassSerializer, CertificateSerializer, ProductSerializer


class ClientsView(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


class ClassesView(ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer


class CertificateView(ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificateSerializer


class ProductsView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
