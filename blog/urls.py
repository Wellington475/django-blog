# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.index', name='index'),
    url(r'^comment/$', 'core.views.cadComment', name='comment'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', 'core.views.index', name='index'),
)
