from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^locations/$', views.locations, name='locations'),
    url(r'^route/$', views.route, name='route'),
    url(r'^point/$', views.point, name='point'),
#    url(r'^point/id/$', views.point_id, name='point_id'),
)

