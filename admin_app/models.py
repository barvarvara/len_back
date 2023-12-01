from django.db import models


class ClientStatuses(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    definition = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'client_statuses'
        verbose_name = "Статус клиента"
        verbose_name_plural = 'Статусы клиентов'


class ClientTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    definition = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'client_types'
        verbose_name = "Тип клиента"
        verbose_name_plural = "Типы клиентов"


class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    fcs = models.CharField(max_length=120)
    client_type = models.ForeignKey("ClientTypes", on_delete=models.CASCADE)
    contacts = models.ForeignKey("Contacts", on_delete=models.CASCADE, related_name='+')
    client_status = models.ForeignKey("ClientStatuses", on_delete=models.CASCADE)

    def get_fcs(self):
        if self.fcs is None:
            return ''
        return ''.join(self.fcs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'clients'
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class ClassTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    definition = models.CharField(max_length=200)
    start_cost = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'class_types'
        verbose_name = 'Тип занятий'
        verbose_name_plural = 'Типы занятий'


class Classes(models.Model):
    id = models.IntegerField(primary_key=True)
    class_type = models.ForeignKey("ClassTypes", on_delete=models.CASCADE, verbose_name='Тип занятия')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    next_date = models.DateField(verbose_name='Дата следующего занятия')
    comment = models.CharField(max_length=500, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.date} {self.time} {self.class_type.name}'

    class Meta:
        db_table = 'classes'
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'


class ProductTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    start_cost = models.IntegerField()
    definition = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_types'
        verbose_name = 'Тип изделия'
        verbose_name_plural = 'Типы изделий'


class ReadyStates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ready_states'
        verbose_name = 'Состояние готовности'
        verbose_name_plural = 'Состояния готовности'


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    definition = models.CharField(max_length=400)
    cost = models.IntegerField()
    product_type = models.ForeignKey("ProductTypes", on_delete=models.CASCADE)
    first_class = models.ForeignKey("Classes", on_delete=models.CASCADE)
    ready_state = models.ForeignKey("ReadyStates", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'


class ActivityType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'activity_types'
        verbose_name = 'Тип активностей'
        verbose_name_plural = 'Типы активностей'


class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    activity_type = models.ForeignKey('ActivityType', on_delete=models.CASCADE)
    client = models.ForeignKey('Clients', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)

    class Meta:
        db_table = "activities"
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'


class Certificates(models.Model):
    id = models.IntegerField(primary_key=True)
    client_buyer = models.ForeignKey("Clients", on_delete=models.CASCADE, related_name='+')
    client_recipient = models.ForeignKey("Clients", on_delete=models.CASCADE)
    purchase_date = models.DateField()
    receiving_date = models.DateField()
    cost = models.IntegerField()
    cost_used = models.IntegerField()
    class_type = models.ForeignKey("ClassTypes", on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)

    class Meta:
        db_table = 'certificates'
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Cheques(models.Model):
    id = models.IntegerField(primary_key=True)
    field_class = models.ForeignKey('Classes', models.DO_NOTHING, db_column='class_id')
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    name = models.CharField(max_length=200)
    sum = models.IntegerField()
    comment = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name} {self.sum}'

    class Meta:
        db_table = 'cheques'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счеты'


class ContactsTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'contacts_types'
        verbose_name = "Тип контактов"
        verbose_name_plural = "Типы контактов"


class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40, verbose_name="Имя")
    last_name = models.CharField(max_length=40, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=40, verbose_name="Отчество")
    phone = models.CharField(max_length=10, verbose_name="Номер телефона")
    birthday = models.DateField(null=True, blank=True)
    ban_on_spam = models.BooleanField()
    client = models.ForeignKey("Clients", on_delete=models.CASCADE, related_name='+')

    def get_fcs(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def get_initials(self):
        return f'{self.first_name[0]}. {self.middle_name[0]}.'

    def __str__(self):
        return self.get_fcs()

    class Meta:
        db_table = 'contacts'
        verbose_name = "Контактные данные"
        verbose_name_plural = "Контактные данные"


class ClientsContacts(models.Model):
    contacts = models.ForeignKey("Contacts", on_delete=models.CASCADE)
    client = models.ForeignKey("Clients", on_delete=models.CASCADE)
    contacts_type = models.ForeignKey("ContactsTypes", on_delete=models.CASCADE, verbose_name='Тип контактного лица')

    class Meta:
        # UniqueConstraint(fields=['contacts', 'client'], name='client_contacts_name')
        unique_together = ('contacts', 'client')

        db_table = 'clients_contacts'
        verbose_name = 'Контактные данные клиентов'
        verbose_name_plural = 'Контактные данные клиентов'


class ClientsGroup(models.Model):
    is_leader = models.BooleanField()
    client_group = models.ForeignKey("Clients", on_delete=models.CASCADE)
    client = models.ForeignKey("Clients", on_delete=models.CASCADE, related_name='+')

    class Meta:
        db_table = 'clients_group'
        unique_together = [('client_group', 'client')]
        # constraints = [
        #     models.UniqueConstraint(fields=['client_group', 'client'])  # client_and_group
        # ]
        verbose_name = "Группа клиентов"
        verbose_name_plural = "Группы клиентов"


class ContactsMedia(models.Model):
    id = models.IntegerField(primary_key=True)
    media = models.IntegerField(db_column="media_id")
    nickname = models.CharField(max_length=100)
    is_main = models.BooleanField()
    contacts = models.ForeignKey("Contacts", on_delete=models.CASCADE)

    class Meta:
        db_table = 'contacts_media'
        verbose_name = 'Соц сети контактов'
        verbose_name_plural = 'Соц сети контактов'


class Media(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    site = models.CharField(max_length=30)
    is_legal = models.BooleanField()
    use_phone = models.BooleanField()

    class Meta:
        db_table = 'media'
        verbose_name = 'Соц сети'
        verbose_name_plural = 'Соц сети'


class PaidType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'paid_types'
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'


class Payments(models.Model):
    id = models.IntegerField(primary_key=True)
    sum_paid = models.IntegerField()
    paid_type = models.ForeignKey("PaidType", on_delete=models.CASCADE)
    certificate = models.ForeignKey("Certificates", on_delete=models.CASCADE)
    cheque = models.ForeignKey("Cheques", on_delete=models.CASCADE)

    class Meta:
        db_table = 'payments'
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class PhotoTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'photo_types'
        verbose_name = 'Тип фото'
        verbose_name_plural = 'Типы фото'


class ProductPhotos(models.Model):
    id = models.IntegerField(primary_key=True)
    photo = models.CharField(max_length=400)
    product_class = models.ForeignKey(Classes, on_delete=models.CASCADE, db_column='class_id')
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    photo_type = models.ForeignKey("PhotoTypes", on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_photos'
        verbose_name = 'Фото изделия'
        verbose_name_plural = 'Фото изделий'


class Guests(models.Model):
    id = models.IntegerField(primary_key=True)
    quest_class = models.ForeignKey("Classes", on_delete=models.CASCADE, db_column='class_id')
    client = models.ForeignKey("Clients", on_delete=models.CASCADE)
    contacts = models.ForeignKey("Contacts", on_delete=models.CASCADE)

    class Meta:
        db_table = 'guests'
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'
