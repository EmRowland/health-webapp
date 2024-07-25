from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path("", views.blogIndex, name="blog_view"),
    path("search/", views.Search, name="blog_search"),
    path("search/results/<str:query>/", views.SearchResult, name="search_results"),
    path("<slug:slug>/", views.blog_details, name="post_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
