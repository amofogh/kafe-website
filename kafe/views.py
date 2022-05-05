from django.shortcuts import render

import re
from .models import Slides, AboutUs, AboutUsImages


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def main_banner(request):
    slides = Slides.objects.all().order_by('slide_number')
    context = {
        'slides': slides
    }

    return render(request, 'main_banner.html', context)


def about_us(request):
    about_us = AboutUs.objects.first()
    about_us_images = AboutUsImages.objects.all().order_by('image_number')

    video_link = about_us.youtube_link
    regex = r'v=(.*)'
    video_id = re.findall(regex, video_link)[0]

    context = {
        'about_us': about_us,
        'images': about_us_images,
        'video_id': video_id,
    }

    return render(request, 'about_area.html', context)

