from django.conf.urls import patterns, url,include
from Tutor import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        
        url(r'^tutor/$', views.index, name='index'),
        url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()