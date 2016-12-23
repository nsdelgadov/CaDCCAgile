import telepot
from cadcc_agile.settings import ID_BOT, ID_CHANNEL

def send_message(message, parse=None):
    """Telegram bot sends the message to the telegram channel"""
    bot = telepot.Bot(ID_BOT)
    if parse is None:
        bot.sendMessage(ID_CHANNEL, message)
    else:
        bot.sendMessage(ID_CHANNEL, message, parse)
    
#todo: complete with another methods     