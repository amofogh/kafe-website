from django.contrib import admin

from .models import ChefSocials, Chef


# Register your models here.

class ChefAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'position']
    search_fields = ['name', 'position']

    class Meta:
        model = Chef


class SocialChefAdmin(admin.ModelAdmin):

    # def save_model(self, request, obj, form, change):
    #     if change == False and obj.chef.chefsocials_set.count():
    #         raise ValidationError('Item already booked for those dates')
    #     super().save_model(request, obj, form, change)

    def chef_name(self, obj):
        return obj.chef.name

    list_display = ['__str__', 'chef_name']
    search_fields = ['chef__name']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            # search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(chef_name__icontains=search_term)
        except:
            pass
        return queryset, use_distinct

    class Meta:
        model = Chef


admin.site.register(Chef, ChefAdmin)
admin.site.register(ChefSocials, SocialChefAdmin)
