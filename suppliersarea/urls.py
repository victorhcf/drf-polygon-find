"""
URL configuration for suppliersarea project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from suppliersarea import admin, views_findprovider
from suppliersarea import views_provider, views_servicearea, views_testsearch

schema_view = get_schema_view(
    openapi.Info(
        title="Mozio Provider`s API",
        default_version='v1',
        description="This service provides an API to manage providers and service areas and has a function to return what providers can serve a location.",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [

    path('admin/', admin.site.urls),

    path('providers/', views_provider.ProviderListView.as_view()),
    path('providers/<int:pk>/', views_provider.ProviderDetailView.as_view()),
    path('serviceareas/', views_servicearea.ServiceAreaListView.as_view()),
    path('serviceareas/<int:pk>/',
         views_servicearea.ServiceAreaDetailView.as_view()),
    path('findarea/', views_findprovider.FindAreaView.as_view()),
    path('custom_page/', views_testsearch.FindProviderView.as_view(), name='custompage'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
]
