from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^', include('shop.urls', namespace='shop')),
    url(r'^order/', include('orders.urls', namespace='orders')),
    # url(r'^paypal/', include('paypal.standard.ipn.urls')),
    # url(r'^payment/', include('payment.urls', namespace='payment')),
    # url(r'^', views.base, name='base'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 