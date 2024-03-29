# Generated by Django 4.2.7 on 2024-03-10 21:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='gentextures/')),
                ('prompt', models.CharField(max_length=500)),
                ('negative_prompt', models.CharField(max_length=500)),
                ('model', models.CharField(max_length=200)),
                ('seed', models.IntegerField()),
                ('date_generated', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Сгенерированное изображение',
                'verbose_name_plural': 'Сгенерированные изображения',
                'db_table': 'generated_images',
            },
        ),
        migrations.CreateModel(
            name='ThreeDModels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('path', models.FileField(upload_to='3dmodels/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('glb', 'obj'))])),
            ],
            options={
                'verbose_name': '3D модель',
                'verbose_name_plural': '3D модели',
                'db_table': 'three_d_models',
            },
        ),
    ]
