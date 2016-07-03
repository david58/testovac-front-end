from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.static import serve

from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
import news.urls

import testovac.tasks.urls
import testovac.submit.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasks/', include(testovac.tasks.urls)),
    url(r'^news/', include(news.urls)),
    url(r'^submit/', include(testovac.submit.urls)),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
]

urlpatterns += [
    url(r'^notifications/', get_nyt_pattern()),
    url(r'', get_wiki_pattern())
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
