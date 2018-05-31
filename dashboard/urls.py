from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', views.index, name='home'),
]