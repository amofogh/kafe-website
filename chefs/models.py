from django.db import models

# Create your models here.
from django.db.models import Q


class Chef(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150, verbose_name='chef position')
    picture = models.ImageField(upload_to='chefs/', verbose_name='Chef profile photo', null=True)
    working = models.BooleanField(default=True, verbose_name='Is chef working?')

    def get_social_chef(self):
        return self.chefsocials_set.all()

    class Meta:
        verbose_name = 'chef'
        verbose_name_plural = 'chefs'

    def __str__(self):
        return self.name


class ChefSocials(models.Model):
    social_name = models.CharField(max_length=100,
                                   verbose_name='Social account name '
                                                '(this use for icon if is not showing icon search in'
                                                ' www.fontawesome.com )')
    link = models.URLField(verbose_name="user link")
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Chef social'
        verbose_name_plural = 'Chef socials'

    def __str__(self):
        return self.social_name
