from django.conf.urls import include, url
from authenticate.views import dashboard, logout_view, register, signin

urlpatterns = [
    url("accounts/", include("django.contrib.auth.urls")),
    url("dashboard/", dashboard, name="dashboard"),
    url("register/", register, name="register"),
    url("signin/", signin, name="signin"),
    url("logout/", logout_view, name="logout"),
]