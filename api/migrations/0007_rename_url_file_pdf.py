# Generated by Django 5.0.7 on 2024-07-31 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_file_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='url',
            new_name='pdf',
        ),
    ]