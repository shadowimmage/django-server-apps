from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'rttApp'
urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
]