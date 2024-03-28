
from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:id>/edit', views.SimpleUserUpdateView.as_view(), name='simple_update_user'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('<int:user_id>/', views.ProfileView.as_view(), name='profile'),
    path('<int:id>/edit-buisness/', views.BusinessUserUpdateView.as_view(), name='business_update_user'),
    path('search/', views.SearchView.as_view(), name='search'),
]

