"""
Send an email to the user once their account is registered
"""
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from accounts.models import CustomUser
from django.template.loader import render_to_string


def send_email_new_user_created(instance):
    subject = "Welcome to Jibonge App"
    body = f'{instance.first_name} {instance.last_name} signed up'
    message = render_to_string(
        'accounts/welcome_new_user.html',
        {'user': instance}
    )
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [instance.email,]

    send_mail(
        subject=subject,
        message=body,
        from_email=from_email,
        recipient_list=recipient_list,
        html_message=message,
    )
