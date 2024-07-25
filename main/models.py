from email.policy import default
from pyexpat import model
from django.db import models
from autoslug import AutoSlugField


# Create your models here.


class DoctorsInit(models.Model):
    full_name = models.CharField(
        blank=False, null=False, max_length=500, verbose_name="Doctors Name"
    )
    work = models.CharField(
        blank=False, null=False, max_length=1000, verbose_name="Area of Speciality"
    )
    image = models.ImageField(
        blank=False,
        null=False,
        upload_to="doctors",
        verbose_name="Add doctors Image",
        default="default.png",
    )
    about = models.TextField(blank=False, null=False, verbose_name="About The Doctor")

    class Meta:
        verbose_name = "Add Doctors Detail"

    def __str__(self) -> str:
        return self.full_name


class DoctorsQualifications(models.Model):
    doctor = models.ForeignKey(DoctorsInit, on_delete=models.CASCADE)
    year = models.CharField(
        blank=False, null=False, max_length=50, verbose_name="Schooling Period"
    )
    qualification_school = models.CharField(
        blank=False,
        null=False,
        max_length=300,
        verbose_name="Add qualification and School",
    )
    description = models.TextField(
        blank=False, null=False, verbose_name="write Description"
    )
    skills = models.TextField(blank=False, null=False, verbose_name="write About Skill")

    class Meta:
        verbose_name = "Add Doctors Qualification"

    def __str__(self) -> str:
        return self.doctor


DAYS = (
    ("Monday - Friday", "Monday - Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)
TIME = (
    ("7:00 - 6:00", "7:00 - 6:00"),
    ("7:00 - 4:30", "7:00 - 4:30"),
    ("closed", "closed"),
)


class DoctorsDAys(models.Model):
    days = models.CharField(choices=DAYS, verbose_name="Day", max_length=20)

    class Meta:
        verbose_name = "Add Work Day"

    def __str__(self) -> str:
        return self.days


class DoctorsTime(models.Model):
    days = models.OneToOneField(DoctorsDAys, on_delete=models.CASCADE)
    time = models.CharField(choices=TIME, verbose_name="Time", max_length=20)

    class Meta:
        verbose_name = "Add Work Time"

    def __str__(self) -> str:
        return self.time


class DoctorsWorkHours(models.Model):
    doctor = models.ForeignKey(DoctorsInit, on_delete=models.CASCADE)
    work_time = models.ManyToManyField(DoctorsTime)

    class Meta:
        verbose_name = "set Doctors Work Time"

    def __str__(self):
        return self.doctor


class DoctorsDepartment(models.Model):
    department = models.CharField(
        null=False, blank=False, max_length=100, verbose_name="doctors Department"
    )
    slug = AutoSlugField(populate_from="department")
    created_at = models.TimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = "Add Doctors Department"

    def __str__(self):
        return self.department


class departmentDetails(models.Model):
    department = models.OneToOneField(
        DoctorsDepartment, on_delete=models.CASCADE, related_name="details"
    )
    details = models.TextField(null=False, blank=False)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Department Detail"

    def __str__(self):
        return f"Details For {self.department.department}"


class DoctorsAndDepartment(models.Model):
    doctors = models.ForeignKey(DoctorsInit, on_delete=models.CASCADE)
    department = models.ManyToManyField(DoctorsDepartment)

    class Meta:
        verbose_name = "Merge Doctors Department"

    def __str__(self):
        return self.doctors.full_name


class subscription(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)
    subed_at = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name = "subscribed User"

    def __str__(self):
        return self.email


# Non Editable Fields By Admin Users (View Only)


class Appiontments(models.Model):
    doctor = models.ForeignKey(DoctorsInit, on_delete=models.CASCADE)
    department = models.ForeignKey(DoctorsDepartment, on_delete=models.CASCADE)
    time = models.DateTimeField(
        null=False, blank=False, verbose_name="Appiontment Time"
    )
    fullname = models.CharField(
        null=False, blank=False, max_length=150, verbose_name="Full Name"
    )
    contact = models.EmailField(
        null=False,
        blank=False,
        verbose_name="Contact",
    )
    message = models.TextField(null=False, blank=False, verbose_name="Message")

    class Meta:
        verbose_name = "Appointment"

    def __str__(self):
        return f"Appiontments With {self.doctor}"


class Contacts(models.Model):
    fullname = models.CharField(
        blank=False, null=False, max_length=300, verbose_name="Full Name"
    )
    email = models.EmailField(blank=False, null=False, verbose_name="Email")
    phone = models.IntegerField(blank=False, null=False, verbose_name="Phone Number")
    subject = models.CharField(
        blank=False, null=False, max_length=1000, verbose_name="Subject"
    )
    message = models.TextField(blank=False, null=False, verbose_name="Message")

    class Meta:
        verbose_name = "Contact Form Message"

    def __str__(self):
        return f"Messages From {self.fullname}"


# End Of View Only Field


class Testimoney(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50, verbose_name="testifier's name"
    )
    service = models.CharField(
        null=False, blank=False, max_length=50, verbose_name="subject"
    )
    testimoney = models.TextField(null=False, blank=False, verbose_name="testimoney")

    class Meta:
        verbose_name = "Add Testimoney"

    def __str__(self):
        return f"{self.name}'s Testimoney"
