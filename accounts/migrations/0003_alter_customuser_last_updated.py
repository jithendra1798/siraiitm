# Generated by Django 4.1.7 on 2023-03-30 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 30, 13, 7, 8, 739077, tzinfo=datetime.timezone.utc), null=True, verbose_name='Last updated'),
        ),
    ]