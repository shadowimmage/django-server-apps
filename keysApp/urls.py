from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'keysApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customer/$', views.customer_info_page, name='customer'),
    url(r'^action/$', views.action_page, name='action'),
    url(r'^checkout/$', views.checkout_page, name='checkout'),
    url(r'^renew/$', views.renew_page, name='renew'),
    url(r'^return/$', views.return_page, name='return'),
    url(r'^confirmation/$', views.confirmation_page, name='confirmation'),
]