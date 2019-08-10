from django.contrib import admin
from django.urls import path, include
from .viewsfolder import register, home, post, comment
from blog.viewsfolder.change_password import change_password


app_name = "blog"
urlpatterns = [
    path("", home.home, name="home"),
    path("<str:username>", home.home, name="user_posts"),
    path("post/create/", post.PostCreate.as_view(), name="create_post"),
    path("post/<int:pk>/", post.PostView.as_view(), name="post"),
    path("post/create/<int:pk>/update", post.PostUpdate.as_view(), name="update_post"),
    path("post/<int:pk>/delete/", post.PostDelete.as_view(), name="delete_post"),
    path(
        "post/<int:pk>/comment/", comment.CommentCreate.as_view(), name="create_comment"
    ),
    path("change_password/", change_password, name="change_password"),
    path("search/", home.search_result, name="search"),
]

