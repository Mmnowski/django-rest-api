from django.conf.urls import url, include
from django.conf import settings

urlpatterns = [
    url(r'^', include('snippets.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
