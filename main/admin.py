from django.contrib import admin
from .models import (
    DoctorsTime,
    DoctorsDAys,
    DoctorsInit,
    DoctorsQualifications,
    DoctorsWorkHours,
    DoctorsAndDepartment,
    DoctorsDepartment,
    subscription,
    Contacts,
    Appiontments,
    departmentDetails,
    Testimoney,
)

# Register your models here.
admin.site.register(DoctorsWorkHours)
admin.site.register(DoctorsQualifications)
admin.site.register(DoctorsDAys)
admin.site.register(DoctorsInit)
admin.site.register(DoctorsTime)
admin.site.register(DoctorsDepartment)
admin.site.register(DoctorsAndDepartment)
admin.site.register(departmentDetails)
admin.site.register(Appiontments)
admin.site.register(model_or_iterable=Testimoney)


class ContactsAdmin(admin.ModelAdmin):
    readonly_fields = ("fullname", "email", "phone", "subject", "message")


admin.site.register(Contacts, ContactsAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    readonly_fields = ("email", "subed_at")


admin.site.register(subscription, SubscribeAdmin)
