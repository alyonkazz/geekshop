# Generated by Django 2.2.3 on 2019-08-29 15:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20190828_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 31, 15, 54, 43, 94486, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
