from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'adbe.core.views.home', name='home'),
    url(r'^login/', 'adbe.core.views.login', name='login'),
    url(r'^logout/', 'adbe.core.views.logout_user', name='logout'),
    url(r'^download/', 'adbe.core.views.download', name='download'),
    url(r'^task/', include('task.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^lector/', include('lector.urls')),
    url(r'^course/', include('course.urls')),
    url(r'^admin/', include(admin.site.urls))
    # Examples:
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
