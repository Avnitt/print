import uuid as uuid_lib

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Order(models.Model):
    BLOCKS = {
        'B1': 'B1',
        'B2': 'B2',
        'B3': 'B3',
        'B4': 'B4',
        'C1': 'C1',
        'C2': 'C2',
        'C3': 'C4',
    }

    TYPES = {
        'PS': 'Printing Service',
        'PS': 'Printing Service',
        'PS': 'Printing Service',
        'PS': 'Printing Service',
    }

    OPTIONS = {
        'BW': 'Black & White',
        'CD': 'Colored',
        'CB': 'Colored + B&W',
        'GP': 'Glossy Paper',
    }

    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    block = models.CharField(max_length=2,
                            choices=BLOCKS)
    service_type = models.CharField(max_length=2,
                                    choices=TYPES)
    option = models.CharField(max_length=2,
                            choices=OPTIONS)
    day = models.DateField()
    time = models.TimeField()
    note = models.TextField()

    payment_status = models.BooleanField(default=False)


class File(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    file_url = models.FileField(upload_to='files/')
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name='files')
