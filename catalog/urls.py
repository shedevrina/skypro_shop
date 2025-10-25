from idlelib.pyparse import trans
from django.contrib import admin

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, contacts, product_detail
from django.conf import settings
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list,name="products_list" ),
    path("contacts/", contacts, name="contacts"),
    path("products/<int:pk>", product_detail, name="product_detail"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
