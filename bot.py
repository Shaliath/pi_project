#Settings
import logging
from telegram.ext import Updater,  CommandHandler,  MessageHandler,  Filters,  CallbackQueryHandler
from telegram import InlineKeyboardButton,  InlineKeyboardMarkup,  ReplyKeyboardMarkup

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',  level = logging.INFO)
logger = logging.getLogger(__name__)
#Callback handling

def startCommand(bot,  update):
    #keyboard = [[InlineKeyboardButton("Option 1",  callback_data = '1'), 
                        #InlineKeyboardButton("Option 2",  callback_data = '2'), 
                        #InlineKeyboardButton("Option 3",  callback_data = '3')]]
    #reply_markup = InlineKeyboardMarkup(keyboard)
    reply_markup = ReplyKeyboardMarkup(keyboard = [
    [dict(text = "Option 1")], 
    [dict(text = "Option 2")], 
    [dict(text = "Option 3")]
    ])
    update.message.reply_text('Please choose: ',  reply_markup = reply_markup)

def textMessage(bot,  update):
    #response = 'Got your message: ' + update.message.text
    #bot.send_message(chat_id = update.message.chat_id,  text = response)
    response = update.message.text
    if response == '1':
        answer = "One"
    elif response == '2':
        answer = "Number two"
    else:
        answer = "Oooops"
    bot.edit_message_text(text = answer, chat_id = update.message.chat_id, message_id = update.message.message_id)

def button(bot,  update):
    query = update.callback_query
    msg = query.message
    
    if query.data == '1':
        answer = "One"
    elif query.data == '2':
        answer = "Number two"
    else:
        answer = "Oooops"
    bot.edit_message_text(text = answer, chat_id = msg.chat_id, message_id = msg.message_id)
    #bot.edit_message_text(text = "Selected option: {}".format(query.data), chat_id = msg.chat_id, message_id = msg.message_id)

def help(bot,  update):
    update.message.reply_text("Use /start to begin")
    
def error(bot,  update,  error):
    logger.warning('Update "%s" caused error "%s"',  update,  error)

def unknown(bot, update):
    bot.send_message(chat_id = update.message.chat_id,  text = "Sorry, I didn't understand that command.")

def main():
    updater = Updater(token='624979515:AAGWfi6SYwReEoUdtBh9tAhBLjgYUGZIJKM')
    dispatcher = updater.dispatcher
    
    #Handlers
    start_command_handler = CommandHandler('start',  startCommand)
    help_command_handler = CommandHandler('help',  help)
    text_message_handler = MessageHandler(Filters.text,  textMessage)
    button_handler = CallbackQueryHandler(button)
    unknown_handler = MessageHandler(Filters.command,  unknown)
    
    #Adding handlers to dispatcher
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(help_command_handler)
    dispatcher.add_handler(text_message_handler)
    dispatcher.add_handler(button_handler)
    dispatcher.add_handler(unknown_handler)

    #Start seeking for updates
    updater.start_polling(clean = True)

    #Stop bot if Ctr+C
    updater.idle()

if __name__ == '__main__':
    main()
