from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            print("hai")
            return redirect(reverse("blog:home"))
        else:
            return redirect(reverse("blog:change_password"))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {"form": form}
        return render(request, "blog/change_password.html", args)

