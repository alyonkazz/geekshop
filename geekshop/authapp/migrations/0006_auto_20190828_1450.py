# Generated by Django 2.2.3 on 2019-08-28 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20190827_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuserprofile',
            name='lang',
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 30, 11, 50, 8, 351296, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
