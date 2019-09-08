from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

User._meta.get_field("email")._unique = True


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, unique=True)
    link = models.CharField(max_length=500, blank=True, default=None)
    imgdata = models.ImageField(upload_to="media", blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"pk": self.pk})

    def __str__(self):
        return '"{title}" by {username}'.format(
            title=self.title, username=self.user.username
        )
