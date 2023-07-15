from django.contrib import admin
from django.urls import include, path
from django.contrib.gis.admin import GISModelAdmin
from .models import Provider, ServiceArea
from django.template.response import TemplateResponse

#admin.site.register(Provider)

#@admin.register(ServiceArea)
class ServiceAreaAdmin(GISModelAdmin):
    list_display = ('id', 'name', 'price','provider', 'information')

from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):   
    site_header = "Mozio Searching Provider By Location"  
    index_template = "admin/custom_index.html"
    def custom_page(self, request):
        context = {"text": "Test finding provider by location", 
                   "page_name": "Test Search Page",
                    "app_list": self.get_app_list(request),
                    **self.each_context(request),}
        return TemplateResponse(request,"admin/custom_page.html", context)

    def get_urls(self):
        custom_urls = [
            path("custom_page/", self.admin_view(self.custom_page), name="custom_page",),
        ]
        admin_urls = super().get_urls()
        return custom_urls + admin_urls  # custom urls must be at the beginning


site = CustomAdminSite()
site.register(Provider, admin.ModelAdmin)
site.register(ServiceArea, ServiceAreaAdmin)