from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<slug>', views.post, name="post"),
    path('profile/', views.profile, name="profile"),

    ## CRUD Paths
    path('post_form/', views.post_form, name="post_form"),
    path('update_form/<slug>', views.update_form, name="update_form"),
    path('delete_post/<slug>', views.deletePost, name="delete_post"),
]
