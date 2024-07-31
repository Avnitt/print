from django.urls import path

from . import views

urlpatterns = [
    path('order/<slug:uuid>',views.GetOrder.as_view(), name='get-order'),
]
