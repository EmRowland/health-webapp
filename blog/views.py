from itertools import count
import random
from tkinter import Label
from turtle import title
from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Tags, Categories, comments, HealthTips
from django.core.paginator import Paginator, Page
from django.db.models import Count
from .forms import BlogSearchForm

# Create your views here.


def blogIndex(request):
    tags = Tags.objects.all()
    categories = Categories.objects.annotate(blog_count=Count("blog"))
    blog_posts = Blog.objects.annotate(comment_count=Count("comments")).order_by(
        "-created"
    )
    blog_recents = Blog.objects.all()[:3]
    paginator = Paginator(blog_posts, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    num_pages = paginator.num_pages
    current_page = page.number
    page_paginator_num_pages = page.paginator.num_pages - 2
    page_range = range(max(1, current_page - 2), min(current_page + 3, num_pages) + 1)
    ctx = {
        "page": page,
        "page_range": page_range,
        "page_paginator_num_pages": page_paginator_num_pages,
        "tags": tags,
        "categories": categories,
        "blog_recents": blog_recents,
    }
    return render(request, "blog.html", ctx)


def SearchResult(request, query):
    tags = Tags.objects.all()
    categories = Categories.objects.annotate(blog_count=Count("blog"))
    count_com = Blog.objects.annotate(comment_count=Count("comments"))
    blog_recents = Blog.objects.all()[:3]
    results = Blog.objects.filter(title__icontains=query)
    paginator = Paginator(results, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    num_pages = paginator.num_pages
    current_page = page.number
    page_paginator_num_pages = page.paginator.num_pages - 2
    page_range = range(max(1, current_page - 2), min(current_page + 3, num_pages) + 1)

    ctx = {
        "results": results,
        "tags": tags,
        "categories": categories,
        "blog_recents": blog_recents,
        "page": page,
        "page_range": page_range,
        "page_paginator_num_pages": page_paginator_num_pages,
    }
    return render(request, "blog_result.html", ctx)


def Search(request):
    tags = Tags.objects.all()
    count_com = Blog.objects.annotate(comment_count=Count("comments"))
    blog_recents = Blog.objects.all()[:3]
    categories = Categories.objects.annotate(blog_count=Count("blog"))
    if request.method == "GET":
        form = BlogSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"].strip()
            if query:
                return redirect("search_results", query=query)
            else:
                return redirect(request.META.get("HTTP_REFERER"), {"form": form})
    return redirect(request.META.get("HTTP_REFERER"), {"form": form})


def blog_details(request, slug):
    tags = Tags.objects.all()
    categories = Categories.objects.annotate(blog_count=Count("blog"))
    count_com = Blog.objects.annotate(comment_count=Count("comments"))
    blog_recents = Blog.objects.all()[:3]
    tips = HealthTips.objects.all()[:5]
    daily_tips = list(tips)
    day_tips = random.choice(daily_tips)
    blog_recents = Blog.objects.all()[:3]
    blog_post = get_object_or_404(Blog, slug=slug)
    comment_here = comments.objects.filter(blog=blog_post)
    if request.method == "POST":
        form = comments()
        try:
            message = request.POST["comment"]
            name = request.POST["name"]
            email = request.POST["mail"]

            if not message:
                message_comments = "Please Fill All The Field"
                print("Emptrhuhfdzydbhcb zhvb dhfbshbc")
                return redirect(request.META.get("HTTP_REFERER"))
            elif not name:
                message_comments = "Please Fill All The Field"
                print("Namehuhfdzydbhcb zhvb dhfbshbc")
                return redirect(request.META.get("HTTP_REFERER"))
            elif not email:
                message_comments = "Please Fill All The Field"
                print("Emailhuhfdzydbhcb zhvb dhfbshbc")
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                form.author = name
                form.email = email
                form.comment = message
                form.blog = blog_post
                form.save()
                return redirect(request.META.get("HTTP_REFERER"))
        except Exception:
            message_comments = "Please Fill All The Fields Correctly"
            return redirect(request.META.get("HTTP_REFERER"))
        return redirect(request.META.get("HTTP_REFERER"))

    ctx = {
        "blog_posts": blog_post,
        "tags": tags,
        "categories": categories,
        "comments": comment_here,
        "day_tips": day_tips,
        "blog_recents": blog_recents,
    }

    return render(request, "details/blog-single.html", ctx)


def comment_func(request, blog):
    if request.method == "POST":
        blog = request.POST["blog"]
        form = comments(blog=blog)
        try:
            message = request.POST["comment"]
            name = request.POST["name"]
            email = request.POST["mail"]
            country = request.POST["country"]
            if not message or email or name:
                message_comments = "Please Fill All The Field"
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                form.author = name
                form.email = email
                form.comment = message
                form.country = country
                form.save()
                return redirect(request.META.get("HTTP_REFERER"))
        except Exception:
            message_comments = "Please Fill All The Fields Correctly"
            return redirect(request.META.get("HTTP_REFERER"))
        return redirect(request.META.get("HTTP_REFERER"))
