from django.urls import path

from kafe.views import home, main_banner, about_us
from chefs.views import chefsView

app_name = 'kafe'

urlpatterns = [
    path('', home, name='home'),
    path('main_banner', main_banner, name='main-banner'),
    path('about-us', about_us, name='about-us'),
    path('chefs', chefsView, name='chef'),
]
