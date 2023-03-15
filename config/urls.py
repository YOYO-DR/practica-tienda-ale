from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('clientes/', include('clientes.urls')),
    path('productos/', include('productos.urls')),
    path('inventario/', include('inventario.urls')),
]
