from django.urls import path
from App_login import views

app_name = 'App_login'

urlpatterns = [
    path('sign_up/', views.SignUp, name="sign_up"),
    path('login/', views.UserLogin, name="login"),
    path('logout/', views.UserLogout, name="logout"),
    path('user_profile/', views.UserProfile, name="user_profile"),
    path('change_profile/', views.UserChangeProfile, name="change_profile"),
    path('password/', views.ChangePassword, name="password"),

    path('add-pro-pic/', views.Add_Profile_Pic, name="add_pro_pic"),
    path('change_pro_pic/', views.Change_Profile_Pic, name="change_pro_pic"),
]
