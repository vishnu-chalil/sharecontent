from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.viewsfolder.register import RegisterView
from blog.viewsfolder.activate_user_account import activate_user_account
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse, reverse_lazy


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    url(r"^$", RedirectView.as_view(url="blog/")),
    url(r"^auth/", include("social_django.urls", namespace="social")),  # <- Here
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="blog:home"), name="logout"
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "activate/<uidb>/<token>/account/",
        activate_user_account,
        name="activate_user_account",
    ),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            success_url="/password_reset_done",
            template_name="reset/password_reset_form.html",
        ),
        name="password_reset",
    ),
    path(
        "password_reset_done/",
        PasswordResetDoneView.as_view(template_name="reset/password_reset_done.html"),
    ),
    url(
        r"password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        auth_views.PasswordResetConfirmView.as_view(
            success_url="/password_reset_complete/",
            template_name="reset/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        PasswordResetCompleteView.as_view(
            template_name="reset/password_reset_complete.html"
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
