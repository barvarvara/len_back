from rest_framework import serializers
from admin_app.models import Clients, Contacts, Certificates, Classes, Products, ClientsContacts


class ClientSerializer(serializers.ModelSerializer):
    # contact_fcs = serializers.CharField(source='contacts.get_fcs')
    # phone = serializers.CharField(source='contacts.phone')
    # , 'contact_fcs', 'phone'

    class Meta:
        model = Clients
        fields = ('id', 'name', 'fcs', 'client_type', 'client_status')
        depth = 1


class ContactsSerializer(serializers.ModelSerializer):
    fcs = serializers.CharField(source='get_fcs')

    class Meta:
        model = Contacts
        fields = ('id', 'fcs', 'phone', 'birthday', 'ban_on_spam')
        depth = 1


class ClientContactsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='contacts.id')
    fcs = serializers.CharField(source='contacts.get_fcs')
    type = serializers.CharField(source='contacts_type.name')
    phone = serializers.CharField(source='contacts.phone')
    client = ClientSerializer

    class Meta:
        model = ClientsContacts
        fields = ('id', 'fcs', 'phone', 'type', 'client')
        depth = 1


class ClassSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='class_type.name')

    class Meta:
        model = Classes
        fields = ('id', 'date', 'time', 'type_name', 'next_date', 'comment')


class CertificateSerializer(serializers.ModelSerializer):
    class_type_name = serializers.CharField(source='class_type.name')

    class Meta:
        model = Certificates
        fields = (
            'id', 'client_buyer', 'client_recipient', 'purchase_date', 'receiving_date', 'cost', 'cost_used',
            'class_type_name',
            'comment')
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='product_type.name')
    ready_state_name = serializers.CharField(source='ready_state.name')

    class Meta:
        model = Products
        fields = ('id', 'name', 'definition', 'cost', 'type_name', 'first_class', 'ready_state_name')
        depth = 1
