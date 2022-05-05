from django.shortcuts import render

from .models import MenuItems, ItemCategories


# Create your views here.

def menu(request):
    # menu_items = MenuItems.objects.filter(type__category__icontains='Breakfast')
    menu_items = MenuItems.objects.filter(active=True, show_menu=True)

    context = {
        'menu_items': menu_items,
    }

    return render(request, 'menu.html', context)


def special_offers(request):
    special_foods = MenuItems.objects.filter(active=True)

    context = {

    }

    return render(request, 'special_offers.html', context)
