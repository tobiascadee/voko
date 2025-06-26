from django.urls import re_path
from .views import Members

urlpatterns = (
    re_path(r'^members/$', Members.as_view(), name="groups_members"),
)
