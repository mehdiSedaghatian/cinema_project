from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.SignUpView.as_view(), name='sign_up'),
    path('sign-in', views.SignInView.as_view(), name='sign_in'),
    path('sign-out', views.SignOutView.as_view(), name='sign_out'),
    path('profile', views.Profile.as_view(), name='profile'),
    path('edit-prfile', views.EditUserProfilePage.as_view(), name='edit_profile'),
    path('change-password', views.ChangePasswordPage.as_view(), name='change_password'),

]
