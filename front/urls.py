"""
URL configuration for front project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("doctors/", views.doctors, name="doctors"),
    # path("contact/", views.contactUs, name="contact_us"),
    path("appointment/", views.appiontment, name="appointment"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("get_doctors/", views.get_doctors, name="get_doctors"),
    path("deparment/", views.department, name="department"),
    path("error/", views.myErrorPage, name="not-found"),
    path("blog/", include("blog.urls")),
    path("contact/", include("main.urls")),
    path("<slug:slug>/", views.departmentDetails, name="department_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = "views.myErrorPage"
