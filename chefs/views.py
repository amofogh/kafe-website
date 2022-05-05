from django.shortcuts import render

from .models import Chef, ChefSocials


# Create your views here.

def chefsView(request):
    chefs = Chef.objects.filter(working=True)
    context = {
        'chefs': chefs,
    }

    return render(request, 'chefs.html', context)
