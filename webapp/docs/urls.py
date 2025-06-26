from django.urls import re_path
from .views import DocumentOverview, DocumentDownload

urlpatterns = (
    re_path(r'^download/(?P<slug>[a-z0-9\-]+)/$',
        DocumentDownload.as_view(),
        name="docs.document_download"),
    re_path(r'^', DocumentOverview.as_view(),
        name="docs.document_overview"),
)
