from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

    url(r'^compartir/telegram/$' , share_on_telegram , name="compartir-telegram"),
    )
