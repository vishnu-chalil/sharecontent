from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
import re


class RegisterView(CreateView):
    model = User
    fields = ["username", "password", "first_name", "last_name", "email"]
    template_name = "blog/registration.html"
    success_url = reverse_lazy("login")
    model.is_active = False

    def form_valid(self, form):
        # Hash password before sending it to super
        form.instance.password = make_password(form.instance.password)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            pass_word = form.cleaned_data["password"]
            u = User.objects.create_user(
                username=user_name,
                email=email,
                password=pass_word,
                first_name=first_name,
                last_name=last_name,
            )
            u.is_active = False
            u.is_email_verified = False
            u.save()
            mail_subject = "Activate your account."
            current_site = get_current_site(self.request)
            uid = urlsafe_base64_encode(force_bytes(u.pk))
            token = default_token_generator.make_token(u)
            kwargs = {"uidb64": uid, "token": token}
            print(len(uid), ":uid")
            print(len(str(uid)), "string uid")
            uid = str(uid)[2:-1]
            # hardcodedurl
            activation_link = (
                str(current_site)
                + "/activate/"
                + str(uid)
                + "/"
                + str(token)
                + "/account"
            )
            message = "Hello {0},\n {1}".format(u.username, activation_link)
            to_email = form.cleaned_data.get("email")
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse(
                "Please confirm your email address to complete the registration"
            )
