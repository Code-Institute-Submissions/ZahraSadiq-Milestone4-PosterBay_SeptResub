from django.urls import path
from . import views
from .views import add_post


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add-post/', views.add_post, name='add_post'),
]
