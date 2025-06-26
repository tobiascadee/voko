from django.urls import re_path
from ordering import views

urlpatterns = (
    re_path(r'^supplier/(?P<pk>[0-9]+)/$', views.SupplierView.as_view(),
        name="view_supplier"),
    re_path(r'^products/$', views.ProductsView.as_view(),
        name="view_products"),
    re_path(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(),
        name="view_product"),
    re_path(r'^order/(?P<pk>[0-9]+)/finish/$', views.FinishOrder.as_view(),
        name="finish_order"),
    re_path(r'^order/(?P<pk>[0-9]+)/summary/$', views.OrderSummary.as_view(),
        name="order_summary"),
    re_path(r'^orders/$', views.OrdersDisplay.as_view(), name="view_orders"),
)
