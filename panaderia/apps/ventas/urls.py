from django.urls import path
from .views import primera_vista,principal

app_name = 'ventas'

urlpatterns = [
    path('ventas',primera_vista,name='primera_vista'),
    path('principal',principal,name='principal')
]