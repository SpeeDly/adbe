from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^signup/$', 'adbe.student.views.signup', name='signup_student'),
    url(r'^profile/$', 'adbe.student.views.profile', name='student_profile'),
)
