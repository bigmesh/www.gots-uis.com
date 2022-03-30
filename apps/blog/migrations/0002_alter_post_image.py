# Generated by Django 3.2 on 2021-06-02 03:23

import apps.blog.models
import config.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(storage=config.storage.OverwriteStorage(), upload_to=apps.blog.models.post_image_filename, verbose_name='Imagen (1200x400)'),
        ),
    ]
