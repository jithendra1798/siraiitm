# Generated by Django 4.1.7 on 2023-03-30 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siraconfig', '0003_defaults_default_portal_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaults',
            old_name='default_portal_shortname',
            new_name='default_portal_shortform',
        ),
    ]