from django.shortcuts import render

def home(request):
    context={'titulo':'Principal'}
    return render(request, 'home.html',context)