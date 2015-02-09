from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^approve/(?P<id>.*)', 'adbe.course.views.approve', name='approve_request'),
    url(r'^reject/(?P<id>.*)', 'adbe.course.views.reject', name='reject_request'),
    url(r'^get_course_files/(?P<id>.*)', 'adbe.course.views.get_uploaded_files', name='get_uploaded_files'),
    url(r'^create/$', 'adbe.course.views.create', name='create_course'),
    url(r'^check_name/$', 'adbe.course.views.check_name', name='check_name'),
)
