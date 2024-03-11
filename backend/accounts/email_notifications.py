"""
Send an email to the user once their account is registered
"""
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from django.template.loader import render_to_string

def send_email_new_user_created():
    subject = "Welcome to Jibonge App"
    body = 'Hi there'
    message = render