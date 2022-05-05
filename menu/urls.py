from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('manu-items', views.menu, name='menu-items'),
]
