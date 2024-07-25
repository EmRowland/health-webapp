from django.shortcuts import render, redirect
import datetime, time
from front.views import department
from .models import Contacts, DoctorsDepartment
from django.contrib import messages
from .models import Appiontments
from django.db.models import Q

# Create your views here.


def myContactEmail(request):
    departments = DoctorsDepartment.objects.all()[:5]
    ctxx = {
        "departments": departments,
    }
    if request.method == "POST":
        form = Contacts()

        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        # print(name)
        # print(message)
        # print(email)
        # print(phone)
        # print(subject)
        if not name:
            messages.error = (request, "Name Field Cannot Be empty")
            return redirect(request.META.get("HTTP_REFERER"))
        elif not message:
            messages.error = (request, "Message Field Cannot Be empty")
            return redirect(request.META.get("HTTP_REFERER"))
        elif not email:
            messages.error = (request, "Email Field Cannot Be empty")
            return redirect(request.META.get("HTTP_REFERER"))
        elif not phone:
            messages.error = (request, "Phone Number Field Cannot Be empty")
            # print("This field if empty")
            return redirect(request.META.get("HTTP_REFERER"))
        elif not subject:
            messages.error = (request, "Subject Field Cannot Be empty")
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            form.fullname = name
            form.email = email
            form.phone = phone
            form.subject = subject
            form.message = message
            form.save()

            ctx = {
                "name": email.split("@")[0],
                "messages": messages,
                "departments": departments,
            }
            # then import email message function
            return render(request, "request/success_email.html", ctx)
        return render(request, "contact.html")

    return render(request, "contact.html", ctxx)


def checkIfDoctor(doctor):
    schedule = Appiontments.objects.filter(doctor=doctor).exists()
    if schedule:
        print("yes")
    else:
        print("no")


def checkDoctorTime(doctor):
    doctors_appointment = Appiontments.objects.filter(doctor=doctor)
    appointment_time = doctors_appointment.values_list("time", flat=True)
    for the_time in appointment_time:
        doctors_year = the_time.year
        doctors_month = the_time.month
        doctors_day = the_time.day
        doctors_hour = the_time.hour
        doctors_minute = the_time.minute

    print(appointment_time)
    return doctors_year, doctors_month, doctors_day, doctors_hour, doctors_minute


def makeAppointment(request):
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    curent_time = current_datetime.strftime("%H:%M")
    current_time = datetime.datetime.strptime(curent_time, "%H:%M").time()
    try:
        if request.method == "POST":
            form = Appiontments()
            doctor = request.POST["doctor"]
            doctor_department = request.POST["department"]
            date = request.POST["date"]
            time = request.POST["time"]
            name = request.POST["name"]
            contact = request.POST["contact"]
            message = request.POST["message"]
            date_main = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            schedule = Appiontments.objects.filter(doctor=doctor).exists()
            if not doctor:
                messages.error(request, "Please Fill All The Fields")
                return redirect(request.META.get("HTTP_REFERER"))
            elif not doctor_department:
                messages.error(request, "Please Fill All The Fields")
                return redirect(request.META.get("HTTP_REFERER"))
            elif not date:
                messages.error(request, "Please Fill All The Fields")
                return redirect(request.META.get("HTTP_REFERER"))
            elif not time:
                messages.error(request, "Please Fill All The Fields")
                return redirect(request.META.get("HTTP_REFERER"))
            elif not contact:
                messages.error(request, "Please Fill All The Fields")
                return redirect(request.META.get("HTTP_REFERER"))
            elif not name:
                messages.error(request, "Please Fill All The Fields")
                return redirect(request.META.get("HTTP_REFERER"))
            elif not message:
                messages.error(request, "Please Fill All The Fields")
                return redirect(request.META.get("HTTP_REFERER"))
            elif date_main <= current_date:
                messages.error(request, "Please Increase the Appointment Time")
                print("time error")
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                time_main = datetime.datetime.strptime(time, "%H:%M")

                time1 = time_main.hour * 60 + time_main.minute
                year = date_main.year
                month = date_main.month
                day = date_main.day
                hour = time_main.hour
                minute = time_main.minute
                if schedule:
                    print("in this func")
                    the_doctor_time = checkDoctorTime(doctor)
                    value1, value2, value3, value4, value5 = the_doctor_time
                    time2 = value4 * 60 + value5
                    print("##############################")
                    boolYear = year - value1
                    boolMonth = month - value2
                    boolDay = day - value3
                    boolTime = time1 - time2

                    print("##############################")
                    doctor_date = datetime.date(value1, value2, value3)
                    date_act = date_main - doctor_date
                    print(date_act)
                    if (
                        boolYear == 0
                        and boolMonth == 0
                        and boolDay == 0
                        and boolTime <= 180
                    ):
                        messages.error(
                            request, "Doctor Is Already Booked Within The Time Frame"
                        )
                        print("Doctor Is Already Booked Within The Time Frame")
                        return redirect(request.META.get("HTTP_REFERER"))
                    elif (
                        boolYear <= 0
                        or boolYear <= 0
                        and boolMonth < 0
                        or boolYear <= 0
                        and boolMonth <= 0
                        and boolDay < 0
                        or boolYear <= 0
                        and boolMonth <= 0
                        and boolDay <= 0
                        and boolTime < 0
                    ):
                        messages.error(
                            request, "Doctor Is Already Booked Within The Time Frame"
                        )
                        print("Doctor Is Already Booked Within The Time Frame")
                        return redirect(request.META.get("HTTP_REFERER"))
                    else:
                        appointment_time = datetime.datetime(
                            year, month, day, hour, minute
                        )
                        form.doctor = doctor
                        form.department = doctor_department
                        form.fullname = name
                        form.contact = contact
                        form.message = message
                        form.time = appointment_time
                        form.save()

                        print("registered in the data base")
                        return redirect(request.META.get("HTTP_REFERER"))

                else:
                    print("i dont understand")
                    return redirect(request.META.get("HTTP_REFERER"))
    except Exception:
        messages.error(request, "Please Fill The Form Correctly")
        print("Doctor Is Already Booked Within The Time Frame")
        return redirect(request.META.get("HTTP_REFERER"))

    return redirect(request.META.get("HTTP_REFERER"))
