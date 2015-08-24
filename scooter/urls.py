from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from app.api.views import *

router = routers.DefaultRouter()
router.register(r'owner', OwnerViewSet, base_name='drivers')
router.register(r'vehicle', VehicleViewSet, base_name='vehicles')
router.register(r'position', PositionViewSet, base_name='positions')

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home', name="home"),#

    #AJAX_calls
    url(r'^get_vehicle/$', 'app.views.get_vehicle', name='get_vehicle'),


    #REST
    url(r'^', include(router.urls)), # Include router urls into our urlpatterns
    url(r'^app-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^position/(?P<long>\d+\.\d{6})/(?P<lat>\d+\.\d{6})/(?P<vehicle_id>[0-9]+)/$', 'app.api.views.post_long_lat'),

    #USER HANDLING
    url(r'^register/$', 'app.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),


    #SIDES
    url(r'^profile/$', 'app.views.profile', name='profile'),
    url(r'^update/$', 'app.views.update', name='update'),
    url(r'^route/(?P<id>[\w\-]+)/$', 'app.views.route', name='route'),
    url(r'^position/(?P<vehicle>\d+)/(?P<from_date>\d{4}-\d{2}-\d{2})/(?P<to_date>\d{4}-\d{2}-\d{2})/$',
        'app.views.position_list'),
    url(r"^csv/route/(?P<id>[\w\-]+)/$",
        "app.views.export_csv", name='export_csv'), # Return a CSV file for this model
    url(r"^csv/position/(?P<vehicle>\d+)/(?P<from_date>\d{4}-\d{2}-\d{2})/(?P<to_date>\d{4}-\d{2}-\d{2})/$",
        "app.views.export_csv_date", name='export_csv_date'), # Return a CSV file for this model


    )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)