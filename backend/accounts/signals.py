from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.email_notifications import send_email_new_user_created
from accounts.models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_email_new_user(sender, created, instance, **kwargs):
    """
    Send an email to the user once their account is registered
    """
    if created:
        print(f"{instance.first_name} was created successfully")
        send_email_new_user_created(instance=instance)
        
    return instance