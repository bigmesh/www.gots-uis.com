# Generated by Django 3.2 on 2021-05-06 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='abstract',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
