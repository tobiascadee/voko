from django.urls import re_path
from .views import Schedule, Shift
from distribution.views import Members, Groupmanager

urlpatterns = (
    re_path(r'^schedule/$', Schedule.as_view(), name="distribution_schedule"),
    re_path(r'^shift/(?P<slug>[-\w]+)/$', Shift.as_view(), name="shift"),
    re_path(r'^members/$', Members.as_view(), name="distribution_members"),
    re_path(r'^groupmanager/$', Groupmanager.as_view(), name="distribution_groupmanager")
)
