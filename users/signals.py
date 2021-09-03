from django.db.models.signals import  post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwrags):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwrags):
    instance.profile.save()
