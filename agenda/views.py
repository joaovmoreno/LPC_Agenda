from django.shortcuts import render

# Create your views here.

def showAgenda(request):
    return render(request, 'template.html', context=None)