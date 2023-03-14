from django.shortcuts import render

def clientes(request):
    client=['Cliente_uno','Cliente_dos','Cliente_tres','Cliente_cuatro']
    context={'titulo':'Clientes','listado':client}
    return render(request, 'clientes.html', context)

def listado_cli(request):
    context={}
    return render(request, 'list_clientes.html', context)

