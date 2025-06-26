from django.urls import re_path
from django.views.generic import RedirectView
from finance import views, admin_views

urlpatterns = (
    re_path(r'^pay/cancel/$',
        views.CancelPaymentView.as_view(),
        name="finance.cancelpayment"),
    re_path(r'^pay/transaction/create/$',
        views.CreateTransactionView.as_view(),
        name="finance.createtransaction"),
    re_path(r'^pay/transaction/confirm/$',
        views.ConfirmTransactionView.as_view(),
        name="finance.confirmtransaction"),
    re_path(r'^pay/transaction/callback/$',
        views.PaymentWebHook.as_view(),
        name="finance.callback"),


    # Admin views
    re_path(r'^admin/(?P<year>[0-9]+)/specified/$',
        RedirectView.as_view(pattern_name='finance.admin.year.overview',
                             permanent=True)),
    re_path(r'^admin/json/round/(?P<round_id>[0-9]+)/$',
        admin_views.JsonRoundOverview.as_view(),
        name="finance.admin.round.overview.json"),
    re_path(r'^admin/round/(?P<round_id>[0-9]+)/$',
        admin_views.RoundOverview.as_view(),
        name="finance.admin.round.overview"),
    re_path(r'^admin/year/(?P<year>[0-9]+)/$',
        admin_views.YearOverview.as_view(),
        name="finance.admin.year.overview"),
)
