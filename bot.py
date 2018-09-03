#Settings
import logging
from telegram.ext import Updater,  CommandHandler,  MessageHandler,  Filters
updater = Updater(token='624979515:AAGWfi6SYwReEoUdtBh9tAhBLjgYUGZIJKM')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  level=logging.INFO)

#Callback handling

def startCommand(bot,  update):
    bot.send_message(chat_id=update.message.chat_id,  text='Hi, let\'s go')

def textMessage(bot,  update):
    response = 'Got your message: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id,  text=response)
    
#Handlers
start_command_handler = CommandHandler('start',  startCommand)
text_message_handler = MessageHandler(Filters.text,  textMessage)

#Adding handlers to dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

#Start seeking for updates
updater.start_polling(clean=True)

#Stop bot if Ctr+C
updater.idle()
