# Generated by Django 4.1.7 on 2023-03-30 14:14

from django.db import migrations, models
import siraconfig.models
import siraiitm.utils


class Migration(migrations.Migration):

    dependencies = [
        ('siraconfig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaults',
            name='default_site_favicon',
            field=models.ImageField(storage=siraiitm.utils.OverwriteStorage, upload_to=siraconfig.models.get_default_site_favicon_image_upload_path),
        ),
        migrations.AlterField(
            model_name='defaults',
            name='default_site_logo',
            field=models.ImageField(storage=siraiitm.utils.OverwriteStorage, upload_to=siraconfig.models.get_default_site_logo_image_upload_path),
        ),
        migrations.AlterField(
            model_name='defaults',
            name='default_user_photo',
            field=models.ImageField(storage=siraiitm.utils.OverwriteStorage, upload_to=siraconfig.models.get_default_user_photo_image_upload_path),
        ),
    ]
