# Generated by Django 4.2.5 on 2023-10-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_photo_info_photo1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.TextField(max_length=300, verbose_name='наименование'),
        ),
    ]
