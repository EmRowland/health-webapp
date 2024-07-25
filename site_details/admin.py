from django.contrib import admin
from django.http.request import HttpRequest
from .models import SiteDetails 

# Register your models here.


class Adminsitedetails(admin.ModelAdmin):
    def has_add_permission(self, request):
        existing_instances_count = SiteDetails.objects.count()
        
        return existing_instances_count == 0
    
admin.site.register(SiteDetails, Adminsitedetails)