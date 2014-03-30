from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from GetHired import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^GetHired/$', views.main),
    url(r'^GetHired/post/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.get_post),
    url(r'^GetHired/post/new/(?P<post_type>\w+)/$',views.new_post),
    url(r'^GetHired/post/new/(?P<post_type>\w+)/create/$',views.create_post),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()
