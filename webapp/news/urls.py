from django.urls import re_path
from news import views

urlpatterns = (
    re_path(r'^$', views.NewsitemsView.as_view(),
        name="view_newsitems"),
    re_path(r'^(?P<pk>[0-9]+)/$', views.NewsitemsView.as_view(),
        name="view_newsitem"),
)
