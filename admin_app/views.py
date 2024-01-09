from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from admin_app.models import Clients, Contacts, Classes, Certificates, Products, ClientsContacts
from admin_app.serializers import ClientSerializer, ClassSerializer, CertificateSerializer, ProductSerializer, \
    ContactsSerializer


class ClientsView(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


class ClientContactsView(ViewSet):
    queryset = Clients.objects.all()

    def retrieve(self, request, pk):
        client = Clients.objects.get(id=pk)
        clientContacts = ClientsContacts.objects.filter(client=client.id).only("contacts")
        contacts = [item.contacts for item in clientContacts]

        serializer = ContactsSerializer(contacts, many=True)
        return Response(serializer.data)


class ClassesView(ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer


class CertificateView(ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificateSerializer


class ProductsView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
