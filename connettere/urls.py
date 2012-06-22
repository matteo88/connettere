from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', 'connect.views.home', name='home'),
    url(r'^home_things/$', 'connect.views.home_things', name='home_things'),
    url(r'^home/graph/$', 'connect.views.graph', name='graph'),
    url(r'^home_things/thing_graph/$', 'connect.views.thing_graph', name='thing_graph'),
    url(r'^graph/result/([a-zA-Z\.\-\s\/\\\'\"]+)/([a-zA-Z\.\-\s\/\\\'\"]+)/([a-zA-Z0-9\.\-\s\/\\\'\"]+)$', 'connect.views.result',name="result"),
    url(r'^thing_graph/result_thing/([a-zA-Z\.\-\s\/\\\'\"]+)/([a-zA-Z0-9\.\-\s\/\\\'\"]+)$', 'connect.views.result_thing',name="result_thing"),
    #url(r'^graph/result/(?P<group>\[a-zA-Z0-9\-\.]+)/(?P<filename>\[a-zA-Z0-9\-\.]+)/$', 'connect.views.result',name="result"),
    # url(r'^connettere/', include('connettere.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
