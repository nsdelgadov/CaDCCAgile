from django.dispatch import receiver
from django.db.models.signals import post_save

from mezzanine.blog.models import BlogPost
from cadcc.telegram import send_message
from cadcc.utils import generateMsgTelegram, set_short_url

@receiver(post_save, sender=BlogPost)
def my_handler(sender, instance, created, **kwargs):
    if created and instance.status==2:
        set_short_url(instance)
        msg = generateMsgTelegram(instance)
        send_message(msg)
        #send_message("https://cadcc-agile-claudin.c9users.io" + instance.get_absolute_url())
