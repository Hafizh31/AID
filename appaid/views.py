from django.shortcuts import render
from .models import Penyakit

def hasilanalisis(request, jenispenyakit):
    hasil = Penyakit.objects.all()
    context = {'hasil': hasil}
    return render(request, 'analisis.html', context)

    if 'q' in request.GET:
        q=request.GET['q']
        post=Post.objects.filter(title__icontains=q)
    else:
        post: Post.objects.all()

def search_bar(request):
    if request.method == "POST":
        searched = request.POST['searched']
        return render(request, 'search_bar.html', {'searched':searched})
    else:
        return render(request, 'search_bar.html', {})
