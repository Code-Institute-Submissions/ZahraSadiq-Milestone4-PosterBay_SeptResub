from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add/', views.add_post, name='add_post'),
]
