from django.urls import path

from . import views

urlpatterns = [
    # path('', views.master, name='master'),
    path("", views.RegisterView.as_view(), name="auth_register"),
    path("login/", views.MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("update_password/",views.UpdatePasswordView.as_view(),name="auth_update_password",),
    path("update_profile/", views.UpdateProfileView.as_view(), name="auth_update_profile"),
    path("update_account/", views.AccountUpdateView.as_view(), name="update_account"),

]
