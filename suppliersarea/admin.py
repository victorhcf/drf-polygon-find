from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from suppliersarea.models import Provider, ServiceArea

admin.site.register(Provider)
# admin.site.register(ServiceArea)


@admin.register(ServiceArea)
class ServiceAreaAdmin(GISModelAdmin):
    list_display = ('id', 'name', 'price', 'provider', 'information')
