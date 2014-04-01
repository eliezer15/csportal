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
    url(r'^GetHired/post/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.get_post,name='get_post'),
    url(r'^GetHired/post/new/(?P<post_type>\w+)/$',views.render_new_post_form, name='render_new_post'),
    url(r'^GetHired/post/edit/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.render_new_post_form, name='render_edit_post'),
    url(r'^GetHired/post/update/(?P<post_type>\w+)/(?P<post_id>\d*)/$',views.create_post,name='create_post'),
    url(r'^GetHired/company/(?P<company_name>\w+)/$', views.get_company_posts),
    url(r'^GetHired/filter/', views.filter_posts,name='filter_posts'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()
