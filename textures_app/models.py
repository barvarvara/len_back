from django.core.validators import FileExtensionValidator
from django.db import models


class GeneratedImages(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(max_length=100, upload_to='gentextures/')
    prompt = models.CharField(max_length=500)
    negative_prompt = models.CharField(max_length=500)
    model = models.CharField(max_length=200)
    seed = models.IntegerField()
    date_generated = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.image

    class Meta:
        db_table = 'generated_images'
        verbose_name = 'Сгенерированное изображение'
        verbose_name_plural = 'Сгенерированные изображения'


class ThreeDModels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    path = models.FileField(max_length=100,
                            upload_to='3dmodels/',
                            validators=[FileExtensionValidator(allowed_extensions=('glb', 'obj'))]
                            )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'three_d_models'
        verbose_name = '3D модель'
        verbose_name_plural = '3D модели'
