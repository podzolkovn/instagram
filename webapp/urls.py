from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.PublicViews.as_view(), name='index'),
    path('post_create', views.PostCreate.as_view(), name='post_add'),
    path('like_post/', views.LikePostView.as_view(), name='like_post'),
    ]
