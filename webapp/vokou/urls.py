from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
import accounts.urls
import docs.urls
import transport.urls
import finance.urls
import mailing.urls
import ordering.urls
import ordering.admin_urls
import api.urls
import distribution.urls
import groups.urls
import news.urls
from vokou.views import HomeView, PrivacyStatementView, RegulationsView

urlpatterns = [
    re_path(r"^admin/mailing/", include(mailing.urls)),
    path("admin/", admin.site.urls),
    re_path(r"^accounts/", include(accounts.urls)),
    re_path(r"^ordering/admin/", include(ordering.admin_urls)),
    re_path(r"^ordering/", include(ordering.urls)),
    re_path(r"^finance/", include(finance.urls)),
    re_path(r"^docs/", include(docs.urls)),
    re_path(r"^transport/", include(transport.urls)),
    re_path(r"^groups/", include(groups.urls)),
    re_path(r"^news/", include(news.urls)),
    re_path(r"^api/", include(api.urls)),
    re_path(r"^distribution/", include(distribution.urls)),
    re_path(r"^tinymce/", include("tinymce.urls")),
    re_path(r"^hijack/", include("hijack.urls")),
    re_path(r"^regulations/", RegulationsView.as_view(), name="regulations"),
    re_path(r"^privacy/", PrivacyStatementView.as_view(), name="privacy"),
    re_path(r"^$", HomeView.as_view(), name="home"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
    ]
