# Generated by Django 4.0.3 on 2023-02-23 02:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('abogados', '0004_alter_abogado_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 2, 16, 28, 315360, tzinfo=utc), verbose_name='Fecha de publicaion '),
        ),
    ]