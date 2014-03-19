from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from GetHired.views import main
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^GetHired/$', main),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

)

urlpatterns += staticfiles_urlpatterns()
