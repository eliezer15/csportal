from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from GetHired import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gethired/$', views.main),
    url(r'^gethired/post/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.get_post,name='get_post'),
    url(r'^gethired/post/new/(?P<post_type>\w+)/$',views.render_new_post_form, name='render_new_post'),
    url(r'^gethired/post/edit/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.render_new_post_form, name='render_edit_post'),
    url(r'^gethired/post/new/(?P<post_type>\w+)/(?P<post_id>\d*)/$',views.create_post,name='create_post'),
    url(r'^gethired/(?P<field_name>\w+)/(?P<field_value>[0-9A-Za-z\-]+)/$', views.get_field_posts, name='get_field_posts'),
    url(r'^gethired/filter/', views.filter_posts,name='filter_posts'),
    url(r'^gethired/post/list/(?P<post_type>\w+)/$', views.get_json_list),
    url(r'^accounts/logout/$', views.logout_view),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

urlpatterns += staticfiles_urlpatterns()
