from django.urls import re_path
from accounts import views

urlpatterns = (
    re_path(r"^login/$", views.LoginView.as_view(), name="login"),
    re_path(r"^logout/$", views.LogoutView.as_view(), name="logout"),
    re_path(r"^register/$", views.RegisterView.as_view(), name="register"),
    re_path(r"^register/thanks/$", views.RegisterThanksView.as_view(), name="register_thanks"),
    re_path(r"^register/confirm/(?P<pk>[0-9a-zA-Z\-]+)$", views.EmailConfirmView.as_view(), name="confirm_email"),
    re_path(
        r"^register/finish/(?P<pk>[0-9a-zA-Z\-]+)$", views.FinishRegistration.as_view(), name="finish_registration"
    ),
    re_path(r"^passwordreset/$", views.RequestPasswordResetView.as_view(), name="password_reset"),
    re_path(r"^passwordreset/done/$", views.PasswordResetRequestDoneView.as_view()),
    re_path(r"^passwordreset/finished/$", views.PasswordResetFinishedView.as_view()),
    re_path(r"^passwordreset/reset/(?P<pk>[0-9a-zA-Z\-]+)$", views.PasswordResetView.as_view(), name="reset_pass"),
    re_path(r"^welcome/$", views.WelcomeView.as_view()),
    re_path(r"^overview/$", views.OverView.as_view(), name="overview"),
    re_path(r"^profile/$", views.ProfileView.as_view(), name="profile"),
    re_path(r"^updateProfile/$", views.EditProfileView.as_view(), name="update_profile"),
    re_path(r"^contact/$", views.Contact.as_view(), name="contact"),
    re_path(r"^orderHistory/$", views.OrderHistory.as_view(), name="order_history"),
    re_path(
        r"^profile/remarks/(?P<pk>[0-9a-zA-Z\-]+)$",
        views.EditCoordinatorRemarksView.as_view(),
        name="coordinator_remarks",
    ),
)
