# Generated by Django 5.0.7 on 2024-07-30 17:10

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='page_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='file',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(max_length=255)),
                ('razorpay_payment_id', models.CharField(max_length=255)),
                ('razorpay_signature', models.CharField(max_length=255)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
    ]
