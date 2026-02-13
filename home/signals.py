from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import Murojaat
from home.telegram import send_to_admins

@receiver(post_save, sender=Murojaat)
def notify(sender, instance, created, **kwargs):
    if created:
        msg = (
            "📨 Yangi murojaat!\n\n"
            f"👤 {instance.firstname} {instance.lastname}\n"
            f"📧 {instance.email}\n"
            f"📝 {instance.murojaat}\n"
            f"⏰ {instance.created_at.strftime('%d-%m-%Y %H:%M')}\n\n"
        )
        send_to_admins(msg)
