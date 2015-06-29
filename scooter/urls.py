from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from app.api.views import *

router = routers.DefaultRouter()
router.register(r'driver', DriverViewSet, base_name='drivers')
router.register(r'scooter', ScooterViewSet, base_name='scooters')
router.register(r'trip', TripViewSet, base_name='trips')
router.register(r'position', PositionViewSet, base_name='positions')

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home', name="home"),#

    #AJAX_calls
    url(r'^get_scooter/$', 'app.views.get_scooter', name='get_scooter'),

    #REST
    url(r'^', include(router.urls)), # Include router urls into our urlpatterns
    url(r'^app-auth/', include('rest_framework.urls', namespace='rest_framework')),
    )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)