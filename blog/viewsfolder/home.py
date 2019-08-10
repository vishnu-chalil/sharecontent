from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from django.db.models import Q
from blog.models.post import Post
from django.contrib.auth.decorators import login_required

NUM_OF_POSTS = 5


def home(request, username=None):
    first_name = ""
    last_name = ""
    if username:
        user = User.objects.get(username=username)
        first_name = user.first_name
        last_name = user.last_name
        post_list = Post.objects.filter(user=user)
    else:
        post_list = Post.objects.all()

    post_list = post_list.order_by("-pub_date")
    paginator = Paginator(post_list, NUM_OF_POSTS)  # Show NUM_OF_PAGES posts per page
    page = request.GET.get("page")

    posts = paginator.get_page(page)
    return render(
        request,
        "blog/home.html",
        {"posts": posts, "first_name": first_name, "last_name": last_name},
    )


@login_required
def search_result(request, search_item=None):
    if request.method == "GET":  # this will be GET now
        item = request.GET.get("srch-term")  # do some research what it does
        try:
            post_list = Post.objects.filter(
                Q(title__icontains=item)
            )  # filter returns a list so you might consider skip except part
            post_list = post_list.order_by("-pub_date")
            # paginator = Paginator(
            #    post_list, NUM_OF_POSTS
            # )  # Show NUM_OF_PAGES posts per page
            # page = request.GET.get("page")
            print(post_list)
            # posts = paginator.get_page(1)
            first_name = "Search results"
            last_name = ""
            return render(
                request,
                "blog/home.html",
                {"posts": post_list, "first_name": first_name, "last_name": last_name},
            )
        except Exception as a:
            return HttpResponse(a)
