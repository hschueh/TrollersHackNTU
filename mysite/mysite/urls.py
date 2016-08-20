"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

from charge.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^index/$',index),
    url(r'^accounts/login/$',login,{'template_name':'login.html'}),
    url(r'^accounts/logout/$',logout,{'template_name':'logout.html'}),
    url(r'^accounts/register/$',register),
    url(r'^accounts/profile/$',profile),
    url(r'^accounts/setting/$',setting),
    url(r'^charge/$',charge),
    url(r'^missions/$',missions),
    url(r'^statistic/(?P<chargestate>.+)/$',statistic),
    url(r'^battle/$',battle),
    url(r'^setting/$', setting),
    url(r'^income/$', income),
    url(r'^calculator/(?P<chargestate>.+)/$', calculator),
    url(r'^create_record/$',create_record),
    url(r'^create_category/$',create_category),
    url(r'^statistic_data/(?P<chargestate>.+)/$',statistic_data),
    url(r'^create_user/$',create_user),
    url(r'^create_user_submit/$',create_user_submit)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



