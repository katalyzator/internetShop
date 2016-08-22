from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf.urls.static import static

from InternetShop import settings
from products.api import ProductImageResource, ProductResource


urlpatterns = patterns('',

                       url(r'^jet/', include('jet.urls', 'jet')),
                       url(r'^$', 'products.views.home', name='home'),
                       url(r'^s/$', 'products.views.search', name='search'),
                       url(r'^products/$', 'products.views.all', name='products'),
                       url(r'^products/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),
                       url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
                       url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),

                       url(r'^cart/$', 'carts.views.view', name='cart'),
                       url(r'^checkout/$', 'orders.views.checkout', name='checkout'),
                       url(r'^orders/$', 'orders.views.orders', name='user_orders'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(ProductImageResource().urls)),
                       url(r'^api/', include(ProductResource().urls)),
                       url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
                       url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
                       url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register'),
                       )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
