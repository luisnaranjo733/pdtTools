from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('core.views',
    url(r'^login/$', 'logIn'),
    url(r'^logout/$', 'logOut'),
)

urlpatterns += patterns('roomDoctor.views',
    url(r'^$', 'index'),
    url(r'^startSelection/$', 'startSelection'),
    url(r'^stopSelection/$', 'stopSelection'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)