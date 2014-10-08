from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cs654.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^logout/$', 'myapp.views.logout_view'),
    url(r'^$', 'myapp.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'myapp.views.register'),
    url(r'^login/$', 'myapp.views.user_login'),
    url(r'^home/$', 'myapp.views.home'),
    url(r'^train/$', 'myapp.views.train'),
    url(r'^order/$', 'myapp.views.order'),
    url(r'^confirm/$', 'myapp.views.confirm'),
    url(r'^final/$', 'myapp.views.final'),
) + static(settings.STATIC_URL)# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
