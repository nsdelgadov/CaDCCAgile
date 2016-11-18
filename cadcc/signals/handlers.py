from django.dispatch import receiver
from django.db.models.signals import post_save

from mezzanine.blog.models import BlogPost

@receiver(post_save, sender=BlogPost)
def my_handler(sender, **kwargs):
    print("This code executes after the save of any BlogPost")
    print("sender", sender)
    print("kwargs", kwargs)
