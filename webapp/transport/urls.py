from django.urls import re_path
from .views import Schedule, Ride, Cars, Groupmanager, Members

urlpatterns = (
    re_path(r'^schedule/$', Schedule.as_view(), name="schedule"),
    re_path(r'^ride/(?P<slug>[-\w]+)/$', Ride.as_view(), name="ride"),
    re_path(r'^cars/$', Cars.as_view(), name="cars"),
    re_path(r'^members/$', Members.as_view(), name="transport_members"),
    re_path(r'^groupmanager/$', Groupmanager.as_view(), name="transport_groupmanager")
)
