from django.contrib import admin
from django.urls import include, path, re_path
from shop import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls','cart' ), namespace='cart')),
    path('orders/', include(('orders.urls','orders'), namespace='orders')),
    path('', include(('shop.urls', 'shop'), namespace='shop')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)