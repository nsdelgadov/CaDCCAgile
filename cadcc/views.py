import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from mezzanine.blog.models import BlogPost
from cadcc.telegram import send_message
from cadcc.utils import *

#Receive BlogPost ID and sent a telegram message    
def share_on_telegram(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        #BlogPost
        bp = get_object_or_404(BlogPost, pk=data['pk'])
        #Save short url if not exist
        set_short_url(bp)
        #Send msg
        msg = generateMsgTelegram(bp)
        send_message(msg)
        
        return HttpResponse("ok")
        
    return HttpResponse("error")
