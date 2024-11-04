from django.urls import path
from .views import login_view,logout_view,menu_principal

app_name = 'usuario'

urlpatterns = [
    path('login',login_view,name='login'),
    path('logout',logout_view,name='logout'),
    path('menu_principal',menu_principal,name='menu_principal')
]