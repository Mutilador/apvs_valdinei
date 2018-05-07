from django.urls import path

from . import views 

urlpatterns = [
    path('',views.cadastro_cliente, name='cadastro-cliente'),
    #path('/register-car/',views.register_car, name='register-car'),
]