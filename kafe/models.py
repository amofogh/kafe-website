from os import path

from django.db import models


# Create your models here.


class Slides(models.Model):
    slide_number = models.IntegerField(default=1, unique=True)
    picture = models.ImageField(upload_to='slides/')

    class Meta:
        verbose_name = 'slide'
        verbose_name_plural = 'slides'

    def __str__(self):
        return str(self.slide_number)


class AboutUs(models.Model):
    title = models.CharField(max_length=250, default='We Leave A Delicious Memory For You')
    description = models.TextField()
    youtube_link = models.URLField(verbose_name='Youtube Video Link')

    class Meta:
        verbose_name = 'About-us'
        verbose_name_plural = 'About-us'

    def __str__(self):
        return self.title


class AboutUsImages(models.Model):
    image_number = models.IntegerField(default=1, unique=True)
    picture = models.ImageField(upload_to='about-us/')

    class Meta:
        verbose_name = 'About-us Image'
        verbose_name_plural = 'About-us Images'

    def __str__(self):
        return str(self.image_number)
