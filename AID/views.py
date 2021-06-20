from django.http import HttpResponse
from django.shortcuts import render
from appaid.models import Penyakit

def artikel(request):
    return render(request, 'artikel.html')

def analisis(request):
    return render(request, 'analisis.html')

def homepage(request):
    return render(request, 'homepage.html')

def hasilanalisis(request):
    hasil = Penyakit.objects.all()
    context = {'hasil': hasil}
    return render(request, 'analisis.html', context)

def search_bar(request):
    if request.method  == "POST":
        searched = request.POST['searched']
        disease = Penyakit.objects.filter(jenispenyakit__contains=searched)
        return render(request, 'search_bar.html',
        {'searched':searched,
        'disease':disease})
    else:
        return render(request, 'search_bar.html',
        {})
