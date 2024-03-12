from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from admin_app.models import Clients, Contacts, Classes, Certificates, Products, ClientsContacts
from admin_app.serializers import ClientSerializer, ClassSerializer, CertificateSerializer, ProductSerializer, \
    ClientContactsSerializer


class ClassesViewSet(ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer


class CertificateViewSet(ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificateSerializer


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ClientsViewSet(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, methods=["get"])
    def contacts(self, request, pk):
        client = Clients.objects.get(id=pk)
        client_contacts = ClientsContacts.objects.filter(client=client.id).only("contacts")
        serializer = ClientContactsSerializer(client_contacts, many=True)

        return Response(serializer.data)
