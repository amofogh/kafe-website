from django.contrib import admin

from .models import Slides, AboutUs, AboutUsImages


# Register your models here.

class AboutUsImageAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() < 3:
            return True
        return False


class AboutUsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() == 0:
            return True
        return False


admin.site.register(Slides)
admin.site.register(AboutUsImages, AboutUsImageAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
