from django.dispatch import receiver
from django.db.models.signals import post_save

from mezzanine.blog.models import BlogPost
from cadcc.telegram import send_message

@receiver(post_save, sender=BlogPost)
def my_handler(sender, **kwargs):
    print("This code executes after the save of any BlogPost")
    #send_message("This code executes after the save of any BlogPost. Hi telegram!")
    print("sender", sender)
    print("kwargs", kwargs)
