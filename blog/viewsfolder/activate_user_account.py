from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


def activate_user_account(request, uidb=None, token=None):
    try:
        uid = force_text(urlsafe_base64_decode(uidb))
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        user = None
    if user and default_token_generator.check_token(user, token):
        user.is_email_verified = True
        user.is_active = True
        user.save()
        return redirect("login")
    else:
        return HttpResponse("Activation link has expired")
