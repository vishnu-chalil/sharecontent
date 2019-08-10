from django.contrib import admin
from .models.comment import Comment
from .models.post import Post


admin.site.register(Comment)
admin.site.register(Post)


# Register your models here.
