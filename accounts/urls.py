from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^error_page/$', views.error_page, name='error_page'),
]