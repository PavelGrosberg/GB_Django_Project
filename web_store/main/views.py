from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'main/index.html', context)
