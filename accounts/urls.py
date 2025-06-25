from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import edit_profile,home,admin_data_view

urlpatterns = [
        path('', home, name='home'),  # This is the homepage

    path('dashboard/', views.dashboard, name='dashboard'),  # Keep this one

    path('admin-only/', views.admin_only_view, name='admin_only'),
    path('manager-only/', views.manager_only_view, name='manager_only'),
    path('user-only/', views.user_only_view, name='user_only'),
    # accounts/urls.py
    path('role-data/', views.team_data_view, name='role_data'),

    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit-profile/', edit_profile, name='edit_profile'),
path('team-access/', views.team_data_view, name='role_data'),
    path('admin-data/', admin_data_view, name='admin_data'),
    path('admin-data/', views.team_data_view, name='role_data'),


]
