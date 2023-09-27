from django.db import models
from auths.models import MyUser


class Category(models.Model):
    """
    Category model
    """
    order = models.PositiveSmallIntegerField(
        verbose_name='порядковый номер',
        default=0
    )
    title = models.CharField(
        verbose_name='наименование',
        max_length=300
    )
    photo = models.ImageField(
        verbose_name='фото',
        upload_to='images/',
        blank=True,
        null=True
    )
    fields = models.JSONField(
        verbose_name='список полей',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.order} - {self.title}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('order', )


class Region(models.Model):
    """
    Region model.
    """
    title = models.CharField(
        verbose_name='наименование',
        max_length=150
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'область'
        verbose_name_plural = 'области'
        ordering = ('title', )


class District(models.Model):
    """
    District model.
    """
    title = models.CharField(
        verbose_name='наименование',
        max_length=150
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'район'
        verbose_name_plural = 'районы'
        ordering = ('title', )


class Color(models.Model):
    """
    Color model.
    """
    title = models.CharField(
        verbose_name='наименование',
        max_length=150
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'
        ordering = ('title', )


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
    category = models.ForeignKey(
        verbose_name='категория',
        to=Category,
        on_delete=models.RESTRICT
    )
    text = models.CharField(
        verbose_name='описание',
        max_length=2000
    )
    region = models.ForeignKey(
        verbose_name='область',
        to=Region,
        on_delete=models.RESTRICT,
        blank=True,
        null=True
    )
    district = models.ForeignKey(
        verbose_name='район',
        to=District,
        on_delete=models.RESTRICT,
        blank=True,
        null=True
    )
    punkt = models.CharField(
        verbose_name='населеный пункт',
        max_length=150,
        blank=True,
        null=True
    )
    date_of_action = models.DateField(
        verbose_name='дата совершения',
        blank=True,
        null=True
    )
    brand = models.CharField(
        verbose_name='Марка / Модель',
        max_length=300,
        blank=True,
        null=True
    )
    series = models.CharField(
        verbose_name='Серия',
        max_length=300,
        blank=True,
        null=True
    )
    number = models.CharField(
        verbose_name='Номер',
        max_length=300,
        blank=True,
        null=True
    )
    year_of_release = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        blank=True,
        null=True
    )
    manufacturer = models.CharField(
        verbose_name='Завод изготовитель / Страна',
        max_length=300,
        blank=True,
        null=True
    )
    color = models.ForeignKey(
        verbose_name='основной цвет',
        to=Color,
        on_delete=models.RESTRICT,
        blank=True,
        null=True
    )
    tone = models.CharField(
        verbose_name='оттенок',
        max_length=150,
        blank=True,
        null=True
    )
    v_size = models.CharField(
        verbose_name='размер',
        max_length=150,
        blank=True,
        null=True
    )
    features = models.CharField(
        verbose_name='особенности',
        max_length=300,
        blank=True,
        null=True
    )
    imei = models.CharField(
        verbose_name='IMEI код',
        max_length=150,
        blank=True,
        null=True
    )
    state_number = models.CharField(
        verbose_name='гос. номер',
        max_length=150,
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        verbose_name='инициатор',
        to=MyUser,
        on_delete=models.RESTRICT,
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
