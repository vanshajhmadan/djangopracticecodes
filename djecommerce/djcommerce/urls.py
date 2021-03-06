"""djcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls # new


API_TITLE = 'ECOM API Tool'
API_DESCRIPTION = 'An Ecommerce Tool for adding and editing the orders'
schema_view = get_schema_view(title=API_TITLE)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='ECOM API Tool')),
    #path('accounts/', include('django.contrib.auth.urls')),
    
]
