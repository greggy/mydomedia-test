from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.SITE_MEDIA_DIR}),
    
    (r'^', include('mydomedia-test.app.urls'))
)
