"""
URL configuration for merrimacknextjs project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from .views import home, gallery, request, about, ProxyView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

admin.site.site_url = 'https://9djns7kv-3000.use.devtunnels.ms/'  # Removes the 'View Site' link
admin.site.site_header = 'NextJs site'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('django_nextjs.urls')),
    # path('', home, name='home'),
    # path('gallery', gallery, name='gallery'),
    # path('request', request, name='request'),
    # path('about', about, name='about'),
    # path('dashboard', about, name='dashboard'),
    # re_path(r'^api/auth/(?P<path>.+)$', csrf_exempt(ProxyView.as_view())),
    path('api/', include('api.urls')),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)