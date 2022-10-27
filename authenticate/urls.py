from django.urls import path,include
from authenticate.views import dashboard, logout_view, register, signin

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("signin/", signin, name="signin"),
    path("logout/", logout_view, name="logout"),
]