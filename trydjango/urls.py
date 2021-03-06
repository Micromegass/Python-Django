"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


from django.urls import path

from pages.views import home_view
from pages.views import contact_view
from pages.views import about_view
from pages.views import social_view
from products.views import product_detail_view, product_create_view


urlpatterns = [
    url(r'^home', home_view , name='home'),
    url(r'^contact', contact_view, name='contact'),
    url(r'^about', about_view, name='about'),
    url(r'^social', social_view, name='social'),
    url(r'^create', product_create_view, name='product_create_view'),
    url(r'^product', product_detail_view, name='product'),
    url(r'^admin/', admin.site.urls),
]
