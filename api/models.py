import uuid as uuid_lib
import PyPDF2

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
        'BS': 'Binding Service',
        'PB': 'Printing + Binding',
        'OE': 'Other Essentials',
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
    note = models.TextField(null=True, blank=True)

    payment_status = models.BooleanField(default=False)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def count_amount(self):
        total_pages = 0
        for file in self.files.all():
            total_pages += file.page_count

        if self.service_type == 'BW':
            self.amount = total_pages * 2
        elif self.service_type == 'CD':
            self.amount = total_pages * 10
        else:
            self.amount = total_pages * 20
        self.save()


class Payment(models.Model):
    order = models.OneToOneField(Order,
                                 on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255)
    razorpay_payment_id = models.CharField(max_length=255)
    razorpay_signature = models.CharField(max_length=255)


def file_upload_path(instance, filename):
    return "files/{0}/{1}".format(instance.order.name, str(instance.uuid) + '.pdf')

class File(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    pdf = models.FileField(upload_to=file_upload_path)
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name='files')
    page_count = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.pdf:
            self.pdf.open('rb')
            pdf_file = PyPDF2.PdfReader(self.pdf)
            self.page_count = len(pdf_file.pages)
        super().save(*args, **kwargs)
