from django.contrib import admin
from .models import *

admin.site.register(ClientTypes)
admin.site.register(ClientStatuses)
admin.site.register(Clients)
admin.site.register(ClientsGroup)

admin.site.register(Contacts)
admin.site.register(ContactsTypes)
admin.site.register(ClientsContacts)
admin.site.register(Guests)
admin.site.register(Certificates)

admin.site.register(ClassTypes)
admin.site.register(Classes)

admin.site.register(ReadyStates)
admin.site.register(Products)
admin.site.register(ProductTypes)
admin.site.register(ProductPhotos)
