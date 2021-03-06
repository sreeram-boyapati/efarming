from django.conf.urls import patterns, include, url
from crops import urls as crops_urls
from users import urls as users_urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'efarming.views.home', name='home'),
    # url(r'^efarming/', include('efarming.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += crops_urls.urlpatterns
urlpatterns += users_urls.urlpatterns