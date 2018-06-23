from django.urls import path

from . import views 

urlpatterns = [
    path('',views.cadastro_cliente, name='cadastro_cliente'),
    path('cadastro_cliente/',views.cadastro_cliente, name='cadastro_cliente'),
    path('fipe_register/',views.fipe_register, name='fipe_register'),
    path('seguro_detail/',views.seguro_detail, name='seguro_detail'),
]