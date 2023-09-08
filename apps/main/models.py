from django.db import models


class Catergory(models.Model):
    """
    Category model
    """
    name = models.CharField(
        verbose_name='наименование',
        max_length=300
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Item(models.Model):
    """
    Item model
    """
    photo1 = models.ImageField(
        verbose_name='фото1',
        upload_to='images/',
        blank=True,
        null=True
    )
    photo2 = models.ImageField(
        verbose_name='фото2',
        upload_to='images/',
        blank=True,
        null=True
    )
    photo3 = models.ImageField(
        verbose_name='фото3',
        upload_to='images/',
        blank=True,
        null=True
    )
    photo4 = models.ImageField(
        verbose_name='фото4',
        upload_to='images/',
        blank=True,
        null=True
    )
    photo5 = models.ImageField(
        verbose_name='фото5',
        upload_to='images/',
        blank=True,
        null=True
    )
    title = models.CharField(
        verbose_name='наименование',
        max_length=300
    )
    catergory = models.ForeignKey(
        verbose_name='категория',
        to=Catergory,
        on_delete=models.RESTRICT
    )
    comment = models.TextField(
        verbose_name='описание'
    )
    date_of_creation = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    date_of_change = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
