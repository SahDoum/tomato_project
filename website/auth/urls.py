from django.urls import include, path
from .views import account_signup_view, account_login_view, account_logout_view, supplier_signup_view, supplier_login_view, supplier_logout_view

urlpatterns = [
    # override the SignupView of django-allauth
    path("signup/", view=account_signup_view, name="signup"),
    path("login/", view=account_login_view, name="login"),
    path("logout/", view=account_logout_view, name="logout"),

    path("supplier_signup/", view=supplier_signup_view, name="supplier_signup"),
    path("supplier_login/", view=supplier_login_view, name="supplier_login"),
    path("supplier_logout/", view=supplier_logout_view, name="supplier_logout"),
    # this is the default config for django-allauth
    path("", include("allauth.urls")),
]