# Generated by Django 3.0.6 on 2021-02-05 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilizatori', '0003_auto_20210205_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizatori',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 5, 14, 44, 51, 558956)),
        ),
    ]
