from django.conf.urls.defaults import *


urlpatterns = patterns('mydomedia-test.app.views',
    url(r'^$', 'index', name='index'),
    url(r'^add/$', 'add', name='add'),
    #url(r'^account/(?P<vdg_id>\d+)/$', '', name=''),
)
