from django.conf.urls import include, url
from .views import *

urlpatterns = [

    url(r'^compartir/telegram/$' , share_on_telegram , name="compartir-telegram"),
]
