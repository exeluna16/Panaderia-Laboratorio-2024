from django.urls import path
from .views import principal

app_name = 'ventas'

urlpatterns = [
    path('principal',principal,name='principal'),
]