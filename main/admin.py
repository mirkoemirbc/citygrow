from django.contrib import admin

from main.models import WDMCityMapItemType, WDMCityType, WDMCity, WDMCityMap

# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        # disabled, because delete_selected ignoring delete model method
        actions = super(BaseModelAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class CityMapItemTypeAdmin(BaseModelAdmin):
    list_display = ['name', 'image_name']


class CityTypeAdmin(BaseModelAdmin):
    list_display = ['name', 'description']


class CityAdmin(BaseModelAdmin):
    list_display = ['name']
    raw_id_fields = ['city_type_id']


class CityMapAdmin(BaseModelAdmin):
    list_display = ['city_x', 'city_y']
    raw_id_fields = ['city_id', 'cmit_id']


admin.site.register(WDMCityMapItemType, CityMapItemTypeAdmin)
admin.site.register(WDMCityType, CityTypeAdmin)
admin.site.register(WDMCity, CityAdmin)
admin.site.register(WDMCityMap, CityMapAdmin)
