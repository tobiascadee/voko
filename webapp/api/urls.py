from django.urls import re_path
from api import views

urlpatterns = (
    re_path(r'^orders(.json)?$', views.OrdersJSONView.as_view()),
    re_path(r'^orders.csv$', views.OrdersCSVView.as_view()),

    re_path(r'^accounts(.json)?$', views.AccountsJSONView.as_view()),
    re_path(r'^accounts.csv$', views.AccountsCSVView.as_view()),
)
