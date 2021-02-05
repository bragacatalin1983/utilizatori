# Generated by Django 3.0.6 on 2021-02-05 12:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utilizatori', '0002_auto_20210205_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizatori',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='utilizatori',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 5, 14, 39, 29, 364992)),
        ),
    ]
