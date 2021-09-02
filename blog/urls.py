from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add-post/', views.add_post, name='add_post'),
    url(r'^edit-post/(?P<pk>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^delete-post/(?P<pk>\d+)/$', views.delete_post, name='delete_post'),
]
