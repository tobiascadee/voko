from django.urls import re_path
from .admin_views import OrderAdminMain, OrderAdminOrderLists, \
    OrderAdminUserOrdersPerProduct, OrderAdminUserOrders, \
    OrderAdminSupplierOrderCSV, OrderAdminUserOrderProductsPerOrderRound, \
    OrderAdminCorrection, OrderAccounts, OrderAdminMassCorrection, \
    OrderAdminCorrectionJson, UploadProductList, CreateDraftProducts, \
    CreateRealProducts, ProductAdminMain, \
    RedirectToMailingView, StockAdminView, ProductStockApiView, ProductApiView

urlpatterns = (
    re_path(r'^rounds/$', OrderAdminMain.as_view(), name="orderadmin_main"),
    re_path(r'^suppliers/$', ProductAdminMain.as_view(), name="productadmin_main"),
    re_path(r'^stock/$', StockAdminView.as_view(), name="stockadmin_main"),

    re_path(r'^api/productstock/$', ProductStockApiView.as_view(),
        name="ordering.api.productstock"),
    re_path(r'^api/product/$', ProductApiView.as_view(),
        name="ordering.api.product"),

    re_path(r'^round/(?P<pk>[0-9]+)/order_lists/$', OrderAdminOrderLists.as_view(),
        name="orderadmin_orderlists"),
    re_path(r'^round/(?P<pk>[0-9]+)/order_lists/(?P<supplier_pk>[0-9]+).csv',
        OrderAdminSupplierOrderCSV.as_view(),
        name="orderadmin_supplier_order_csv"),
    re_path(r'^round/(?P<pk>[0-9]+)/user_orders/$', OrderAdminUserOrders.as_view(),
        name="orderadmin_userorders"),
    re_path(r'^round/(?P<pk>[0-9]+)/product_orders/$',
        OrderAdminUserOrderProductsPerOrderRound.as_view(),
        name="orderadmin_orders_per_product"),
    re_path(r'^round/(?P<pk>[0-9]+)/correction/json',
        OrderAdminCorrectionJson.as_view(), name="orderadmin_correction_json"),
    re_path(r'^round/(?P<pk>[0-9]+)/correction/mass$',
        OrderAdminMassCorrection.as_view(), name="orderadmin_mass_correction"),
    re_path(r'^round/(?P<pk>[0-9]+)/correction/$', OrderAdminCorrection.as_view(),
        name="orderadmin_correction"),
    re_path(r'^round/(?P<pk>[0-9]+)/accounts/$', OrderAccounts.as_view(),
        name="orderadmin_accounts"),
    re_path(r'^round/(?P<pk>[0-9]+)/mailing/(?P<mailing_type>(round-open))/$',
        RedirectToMailingView.as_view(), name="productadmin_mailing"),
    re_path(r'^product/(?P<pk>[0-9]+)/$', OrderAdminUserOrdersPerProduct.as_view(),
        name="productorders_admin"),

    re_path(r'^supplier/(?P<supplier>[0-9]+)/$', CreateDraftProducts.as_view(),
        name="create_draft_products"),
    re_path(r'^supplier/(?P<supplier>[0-9]+)/upload/$',
        UploadProductList.as_view(), name="upload_products"),
    re_path(r'^supplier/(?P<supplier>[0-9]+)/finish/$',
        CreateRealProducts.as_view(), name="create_real_products"),
)
