from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from pentathlon.views import CreateTeamView, CreateParticipationView

import os

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/')}),
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),
    url(r'^$', CreateTeamView.as_view(), name='create_team'),
    url(r'^team/(?P<pk>\d+)/$', CreateParticipationView.as_view(), name='create_participation'),
)
