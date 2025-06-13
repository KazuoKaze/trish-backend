"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic.base import RedirectView
from django.http import JsonResponse, HttpResponse

import packages.urls as package

def health_check(request):
    return JsonResponse({"status": "healthy"})

@api_view(['GET'])
def root_view(request):
    return Response({
        "message": "Welcome to the API",
        "version": "1.0",
        "status": "running"
    })

# Favicon handler
def favicon_view(request):
    return HttpResponse(status=204)

urlpatterns = [
    path('', root_view, name='api-root'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(package)),
    path('health/', health_check, name='health_check'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)