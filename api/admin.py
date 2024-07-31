from django.contrib import admin
from .models import Order, File, Payment


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'day', 'time', 'payment_status']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['pdf', 'order', 'page_count']
