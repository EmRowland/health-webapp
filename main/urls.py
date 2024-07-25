from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path("", views.myContactEmail, name="contact_form"),
    path("appointment/", views.makeAppointment, name="make_appointment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
