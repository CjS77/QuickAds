from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # Only admins can create new user profiles
    # path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('dashboard', views.Dashboard.as_view(), name="dashboard"),
    path('update/profile', views.UpdateProfile.as_view(), name="update_profile"),
    path('change-password/', views.ChangePassword.as_view(),
         name="change_password"),
    path('my-product/', views.MyProduct.as_view(),
         name="my_products"),


    path('logout/', views.LogoutView.as_view(), name='logout'),




]
