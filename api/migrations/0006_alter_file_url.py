# Generated by Django 5.0.7 on 2024-07-31 01:57

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_file_url_file_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='url',
            field=models.FileField(upload_to=api.models.file_upload_path),
        ),
    ]
