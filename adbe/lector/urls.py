from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^upload/$', 'adbe.lector.views.upload', name='upload'),
    url(r'^delete/$', 'adbe.lector.views.delete', name='delete'),
    url(r'^signup/$', 'adbe.lector.views.signup', name='signup_lector'),
    url(r'^profile/$', 'adbe.lector.views.profile', name='lector_profile'),
)
