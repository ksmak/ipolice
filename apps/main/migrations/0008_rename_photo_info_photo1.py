# Generated by Django 4.2.5 on 2023-09-29 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='photo',
            new_name='photo1',
        ),
    ]
