from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bkw.views.home', name='home'),
    # url(r'^bkw/', include('bkw.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^reviews/$', 'review.views.index'),
    (r'^reviews/h1/$', 'review.views.indexH1'),
    (r'^reviews/d1/$', 'review.views.indexD1'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
