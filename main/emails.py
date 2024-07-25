from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def sendUserEmail(email, message, subject, name):
    # Write my email functions here

    mail_subject = subject
    message = render_to_string(
        "email/contact.html",
        {
            "subject": subject,
            # "name": name,
            "username": name,
            "message": message,
        },
    )
    to_email = email
    email_send = EmailMessage(mail_subject, message, to=[to_email])
    # print("send .........")
    email_send.send()


def sendAdminEmail(email, message, subject):
    # Write my email functions here

    mail_subject = subject
    message = render_to_string(
        "email/contact.html",
        {
            "subject": subject,
            # "name": name,
            "email": email,
            "message": message,
        },
    )
    admin_mail = "admin@gmail.com"
    to_email = admin_mail
    email_send = EmailMessage(mail_subject, message, to=[to_email])
    # print("send .........")
    email_send.send()
