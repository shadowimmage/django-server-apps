"""djangoServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from graphene_django.views import GraphQLView
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^', include('dashboard.urls')),
    url(r'^djangoServer/admin/', admin.site.urls),
    url(r'^djangoServer/', RedirectView.as_view(url='/')),
    url(r'^keysApp/', include('keysApp.urls')),
    url(r'^rttApp/', include('rttApp.urls')),
    url(r'^graphql/', login_required(ensure_csrf_cookie(GraphQLView.as_view(graphiql=True)))),
    url(r'^accounts/', include('accounts.urls')),
    url('', include('social_django.urls', namespace='social')),
]
