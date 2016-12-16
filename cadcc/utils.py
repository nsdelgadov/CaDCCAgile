from cadcc.google import google_url_shorten

#Set BlogPost url_short if not defined
def set_short_url(bp):
    if not bp.url_short:
        url = google_url_shorten(bp.get_absolute_url_with_host())
        bp.url_short = url
        bp.save()

#Set Telegram Msg    
def generateMsgTelegram(bp):
    msg = bp.meta_title() + '\n\n'
    msg = msg + bp.url_short + '\n\n'
    if not bp.gen_description:
        msg = msg + bp.description_from_content()
    else:    
        msg = msg + bp.description
    return msg
