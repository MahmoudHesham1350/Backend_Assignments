from django.urls import include,path
from . import views


urlpatterns = [
    path('register/',views.RegisterForm.as_view(),name = 'Register_Form'),
    path('login/',views.LoginForm.as_view(),name = 'Login_Form'),
    path('logout/',views.LogoutForm.as_view(),name='Logout_Form'),
    path('account/',views.Account.as_view(),name='My_Account'),
]