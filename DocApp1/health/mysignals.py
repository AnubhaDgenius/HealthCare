from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from health.models import Patient
from django.contrib.auth.signals import user_logged_in
from health.myctxproc import set_st
# from health.myctxproc import set_st

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance, name=instance.username)

@receiver(user_logged_in)
def get_pat_details(sender, user, request, **kwargs):
    if user.is_staff:
        st=None
    else:    
        st = Patient.objects.filter(user=request.user.id)[0]
    set_st(st)
# user_logged_in.connect(get_stu_details)