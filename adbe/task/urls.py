from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^create/$', 'adbe.task.views.create', name='create_task'),
)
