from django.dispatch import receiver
from django.db.models.signals import post_save

from mezzanine.blog.models import BlogPost
from cadcc.telegram import send_message

@receiver(post_save, sender=BlogPost)
def my_handler(sender, instance, created, **kwargs):
    if created and instance.status==2:
        print("This code executes after the save a new published BlogPost")
        send_message(instance.get_absolute_url_with_host())
        #send_message("https://cadcc-agile-claudin.c9users.io" + instance.get_absolute_url())
