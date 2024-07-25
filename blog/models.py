from distutils.command.build import show_compilers
from django.utils import timezone
from email.policy import default
from autoslug import AutoSlugField
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Tags(models.Model):
    tag = models.CharField(blank=False, null=False, max_length=200, verbose_name="Tag")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Add Blog Tag"

    def __str__(self):
        return self.tag


class Categories(models.Model):
    blog_category = models.CharField(
        blank=False, null=False, max_length=200, verbose_name="Category", unique=True
    )
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Add Blog Category"

    def __str__(self):
        return self.blog_category


class Blog(models.Model):
    image = models.ImageField(
        null=False, blank=False, upload_to="blogs", verbose_name="blog image"
    )
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        blank=False, null=False, max_length=500, verbose_name="Blog Title"
    )
    blog_category = models.ManyToManyField(Categories)
    tags = models.ManyToManyField(Tags)
    blog_content = models.TextField(
        null=False, blank=False, verbose_name="Blog content"
    )
    slug = AutoSlugField(populate_from="title")

    class Meta:
        verbose_name = "Add Blog"

    def __str__(self):
        return self.title


class comments(models.Model):
    author = models.CharField(
        max_length=150, null=False, blank=False, verbose_name="commentors Name"
    )
    email = models.EmailField(null=False, blank=False, verbose_name="Commentor's Email")
    comment = models.TextField(null=False, blank=False, verbose_name="Comment")
    country = models.CharField(null=False, blank=False, max_length=100, verbose_name="Country", default="Nigeria")
    created = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        verbose_name = "Add Comment"

    def __str__(self):
        return f"{self.author}'s Comment On {self.blog.title}"


class HealthTips(models.Model):
    content = models.TextField(null=False, blank=False, verbose_name="Health Tips")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Add Daily Tip"

    def __str__(self):
        current_date = timezone.localdate()

        if self.created_at.date() == current_date:
            show = "Today's Health Tip"
            return show
        else:
            show = f"{self.created_at.date()}'s Health Tip"
            return show
        return show
