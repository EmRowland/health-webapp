from email import message
from django.db import models

# Create your models here.


class SiteDetails(models.Model):
    logo = models.ImageField(null=False, blank=False, upload_to="sites")
    site_number = models.IntegerField(
        null=False, blank=False, verbose_name="Phone Number"
    )
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    facebook = models.URLField(null=False, blank=False, verbose_name="Face Book")
    twitter = models.URLField(null=False, blank=False, verbose_name="Twitter")
    linkedin = models.URLField(null=False, blank=False, verbose_name="LikedIn")
    instagram = models.URLField(null=False, blank=False, verbose_name="Instagram")
    address = models.CharField(
        null=False, blank=False, verbose_name="Hospital Address", max_length=500
    )
    butter_combs = models.ImageField(null=False, blank=False, upload_to="header_images")

    class Meta:
        verbose_name = "Site Social"

    def __str__(self):
        return "Site Detail"


class SiteCounter(models.Model):
    happy_client = models.IntegerField(
        null=False, blank=False, default=100, verbose_name="Happy Clients"
    )
    completed_surgery = models.IntegerField(
        null=False, blank=False, default=100, verbose_name="Surgery Completed"
    )
    expert_doctors = models.IntegerField(
        null=False, blank=False, default=100, verbose_name="Doctors"
    )
    branches = models.IntegerField(
        null=False, blank=False, default=100, verbose_name="Branches"
    )

    class Meta:
        verbose_name = "Website Counter"

        def __str__(self):
            return "Site Counter"


class SiteTestimony(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, verbose_name="Name")
    work = models.CharField(
        null=False, blank=False, max_length=100, verbose_name="Work"
    )
    message = models.TextField(
        null=False, blank=False, max_length=50, verbose_name="Message"
    )
    image = models.ImageField(
        null=False,
        blank=False,
        default="default.png",
        upload_to="testimoies",
        verbose_name="image",
    )

    class Meta:
        verbose_name = "Add Testimonie"

    def __str__(self):
        return f"{self.name}'s Testimony"


class SiteSayAbout(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, verbose_name="Name")
    work = models.CharField(
        null=False, blank=False, max_length=100, verbose_name="Work"
    )
    message = models.TextField(
        null=False, blank=False, max_length=50, verbose_name="Message"
    )

    class Meta:
        verbose_name = " Add Words About Us"

    def __str__(self):
        return f"What {{name}} Said"
