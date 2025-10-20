from idlelib.pyparse import trans
from django.contrib import admin

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_details, product_list
from django.conf import settings
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product_details/", product_details, name="product_details"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
