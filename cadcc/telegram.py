import telepot

#Credentials
ID_BOT = "266039242:AAHfHojkbgRyhmGmLuSl1l9z5Vk3mAh4akY"
ID_CHANNEL = "@testcadcc"

def send_message(message, parse=None):
    """Telegram bot sends the message to the telegram channel"""
    bot = telepot.Bot(ID_BOT)
    if parse is None:
        bot.sendMessage(ID_CHANNEL, message)
    else:
        bot.sendMessage(ID_CHANNEL, message, parse)
    
#todo: complete with another methods     