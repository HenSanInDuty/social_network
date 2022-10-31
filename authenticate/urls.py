from django.urls import path,include
from authenticate.views import dashboard, logout_view, register, signin, ProfileDetail,profile_update

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("signin/", signin, name="signin"),
    path("",signin, name="signin"),
    path("logout/", logout_view, name="logout"),
    path("profile/<int:id>/",ProfileDetail.as_view(), name="detail-profile"),
    path("updateProfile/",profile_update,name='update-profile')
]