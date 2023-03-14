from django.shortcuts import render

def inventario(request):
    context = {'titulo':'Inventario'}
    return render(request, 'inventario.html', context)
