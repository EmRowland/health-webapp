from django.shortcuts import get_object_or_404, render, redirect
from main.models import (
    DoctorsAndDepartment,
    DoctorsInit,
    DoctorsDepartment,
    subscription,
    Appiontments,
    departmentDetails,
)
from django.http import HttpResponse, JsonResponse
from blog.models import Tags, Categories, Blog, comments


def index(request):
    departments = DoctorsDepartment.objects.all()[:5]

    #

    ctx = {
        "departments": departments,
        #
    }

    return render(request, "index.html", ctx)


def about(request):
    departments = DoctorsDepartment.objects.all()[:5]

    ctx = {
        "departments": departments,
    }

    return render(request, "about.html", ctx)


def service(request):
    departments = DoctorsDepartment.objects.all()[:5]

    ctx = {
        "departments": departments,
    }

    return render(request, "services.html", ctx)


def department(request):
    departments = DoctorsDepartment.objects.all()[:5]
    department = DoctorsDepartment.objects.select_related("details")
    # department_detail = departmentDetails.objects.all()

    ctx = {
        "departments": departments,
        "department": department,
    }

    return render(request, "department.html", ctx)


def appiontment(request):
    departments = DoctorsDepartment.objects.all()[:5]

    ctx = {
        "departments": departments,
    }

    return render(request, "appiontment.html", ctx)


def get_doctors(request):
    department_id = request.GET.get("department_id")
    # print("successfully done")
    doctors = DoctorsAndDepartment.objects.filter(department=department_id).values(
        "doctors__id", "doctors__full_name"
    )
    # print(doctors)
    doctor_data = {
        doctor["doctors__id"]: doctor["doctors__full_name"] for doctor in doctors
    }
    # print(doctor_data)
    return JsonResponse({"doctors": doctor_data})


def successfullAppiontment(request):
    departments = DoctorsDepartment.objects.all()[:5]

    ctx = {
        "departments": departments,
    }

    return render(request, "request/appointment.html", ctx)


def doctors(request):
    departments = DoctorsDepartment.objects.all()[:5]

    ctx = {
        "departments": departments,
    }

    return render(request, "doctors.html", ctx)


def contactUs(request):
    departments = DoctorsDepartment.objects.all()[:5]

    ctx = {
        "departments": departments,
    }

    return render(request, "contact.html", ctx)


def getAppiontment(request):
    query = DoctorsAndDepartment.objects.all()
    doctors_id = request.Get.get("doctors_id")
    department = DoctorsAndDepartment.objects.get(id=doctors_id).department.all()

    response = HttpResponse("Query Done Successfully")

    return response


def subscribe(request):
    if request.method == "POST":
        email = request.POST["email"]
        email_exists = subscription.objects.filter(email=email)
        try:
            form = subscription()
            if email_exists:
                messages = "You are already Subscribed to this service"
                return redirect(request.META.get("HTTP_REFERER"))
            elif email is None:
                messages = "Please Type In your Email"
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                form.email = email
                form.save()
                return redirect(request.META.get("HTTP_REFERER"))

        except Exception:
            messages = "Please Type In your Email Correctly"
            return redirect(request.META.get("HTTP_REFERER"))

    response = HttpResponse("Query Done Successfully")
    return response


def myErrorPage(request, exception):
    return render(request, "errors/404.html", status=404)


def departmentDetails(request, slug):
    department = DoctorsDepartment.objects.get(slug=slug)
    departments = DoctorsDepartment.objects.all()[:5]
    departments_full = DoctorsDepartment.objects.all()
    department_detail = department.details
    ctx = {
        "details": department_detail,
        "departments": departments,
        "full": departments_full,
    }
    return render(request, "details/department.html", ctx)
