from django.urls import re_path
from mailing.views import PreviewMailView, ChooseTemplateView, SendMailView

urlpatterns = (
    re_path(r'^sendmail/$',
        ChooseTemplateView.as_view(),
        name="admin_choose_mail_template"),
    re_path(r'^sendmail/preview/(?P<pk>[0-9]+)/$',
        PreviewMailView.as_view(),
        name="admin_preview_mail"),
    re_path(r'^sendmail/send/(?P<pk>[0-9]+)/$',
        SendMailView.as_view(),
        name="admin_send_mail"),
)
