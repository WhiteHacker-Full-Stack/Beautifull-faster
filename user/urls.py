from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from rest_framework.reverse import reverse_lazy

from .views import register,profile,profile_edit, password_change,password_reset_view,verify_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('password_change/', PasswordChangeView.as_view(template_name='user/password_change.html',
                                                        success_url = reverse_lazy('profile')), name='password_change'),
    path('password_change2/', password_change, name='password_change2'),
    path('password_reset/', password_reset_view, name='password_reset'),
    path('verify/', verify_view, name='verify_view'),
]