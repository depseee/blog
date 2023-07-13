from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main_app/index.html', )


def about(request):
    return render(request, 'main_app/about.html')
