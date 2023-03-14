from django.urls import path
from inventario.views import *
urlpatterns = [
    path('',inventario,name='inventario')
]
