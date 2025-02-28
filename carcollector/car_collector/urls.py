from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  

    path('cars/', views.car_list, name='car_list'), 
    path('car/new/', views.car_create, name='car_create'),
    path('car/<int:car_id>/edit/', views.car_update, name='car_update'),
    path('car/<int:car_id>/delete/', views.car_delete, name='car_delete'),

    path('car/<int:car_id>/mods/', views.mod_list, name='mod_list'),
    path('car/<int:car_id>/mod/new/', views.mod_create, name='mod_create'),
    path('mod/<int:mod_id>/delete/', views.mod_delete, name='mod_delete'),

    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name='signup'),

    path('tags/', views.tag_list, name='tag_list'),
    path('tags/new/', views.tag_create, name='tag_create'),
]
