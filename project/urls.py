from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import home

admin.site.site_header = 'Hamro Dokan'
admin.site.index_title = 'Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),


    #orders
    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
