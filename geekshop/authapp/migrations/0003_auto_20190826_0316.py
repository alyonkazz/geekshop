# Generated by Django 2.2.3 on 2019-08-26 00:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20190822_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='ключ подтверждения'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 28, 0, 16, 34, 755295, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='genre',
            field=models.CharField(blank=True, choices=[('f', 'фантастика'), ('b', 'боевик')], max_length=128, verbose_name='любимый жанр'),
        ),
    ]
