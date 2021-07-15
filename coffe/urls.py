from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',LoginView.as_view(template_name = 'LOGIN.html'),name = 'login_url'),
    path('Register/',views.register, name = 'register'),
    path('dashboard/',views.dashboardView,name = 'dashboard'),
]
