from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'app_name.views.index', name='index'),
    url(r'^sv$', 'app_name.views.index_sv', name='index_sv'),
    url(r'^sv/om-sidan$', 'app_name.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
