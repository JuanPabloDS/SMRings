from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def aneis(request):
    return render(request, 'aneis.html')
