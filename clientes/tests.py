from tienda.wsgi import *
from clientes.models import *

# user=Cliente()
# user.nombre='Yoiner'
# user.direccion='cra 2b #12-53'
# user.email='yoiner@gmail.com'
# user.telefono='+57 3148743538'
# user.save()

print(Cliente.objects.all())

# Create your tests here.
