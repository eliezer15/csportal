from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from registration import views as reg_views
from GetHired import views, forms
from django.contrib import admin
from django.contrib.auth.views import password_reset_confirm
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<site>\w+)/$', views.main),
    url(r'^marketplace/post/project/(?P<post_id>\d+)$',views.get_project_post, name='get_project_post'),
    url(r'^(?P<site>\w+)/post/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.get_post,name='get_post'),
    url(r'^marketplace/post/new/project/$',views.project_new_post, name='render_new_project_post'),
    url(r'^marketplace/post/project/(?P<post_id>\d+)/contact/$',views.project_send_email, name='contact_project'),
    url(r'^(?P<site>\w+)/post/new/(?P<post_type>\w+)/$',views.render_new_post_form, name='render_new_post'),
    url(r'^(?P<site>\w+)/post/edit/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.render_new_post_form, name='render_edit_post'),
    url(r'^gethired/post/new/(?P<post_type>\w+)/(?P<post_id>\d*)/$',views.create_post,name='create_post'),
    url(r'^gethired/(?P<field_name>\w+)/(?P<field_value>[0-9A-Za-z\-]+)/$', views.get_field_posts, name='get_field_posts'),
    url(r'^gethired/filter/', views.filter_posts,name='filter_posts'),
    url(r'^gethired/post/list/(?P<post_type>\w+)/$', views.get_json_list),
    url(r'^accounts/logout/$', views.logout_view),
    url(r'^accounts/profile/$', views.userprofile),
    url(r'^accounts/register/$',
        views.registrationview.as_view(),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

urlpatterns += staticfiles_urlpatterns()
