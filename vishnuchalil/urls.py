from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.viewsfolder.register import RegisterView
from blog.viewsfolder.activate_user_account import activate_user_account
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
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
    url(
        r"^.*$",
        RedirectView.as_view(url=settings.LOGIN_REDIRECT_URL, permanent=False),
        name="index",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
