#Settings
import logging
from telegram.ext import Updater,  CommandHandler,  MessageHandler,  Filters,  CallbackQueryHandler
from telegram import InlineKeyboardButton,  InlineKeyboardMarkup,  ReplyKeyboardMarkup
import pistatus

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',  level = logging.INFO)
logger = logging.getLogger(__name__)
lightStatus = "Off"

#Callback handling

def startCommand(bot,  update):
    reply_markup = ReplyKeyboardMarkup(keyboard = [
    [dict(text = "Info")], 
    [dict(text = "Control")]
    ])
    update.message.reply_text('Please choose: ',  reply_markup = reply_markup)

def textMessage(bot,  update):
    response = update.message.text
    if response == 'Info':
        infoMenu(bot, update)
    elif response == 'Control':
        controlMenu(bot, update)
    elif response == "Home":
        startCommand(bot, update)
    elif response == "Light":
        lightMenu(bot, update)
    else:
        bot.send_message(text = "Oooops", chat_id = update.message.chat_id)

def infoMenu(bot, update):
    keyboard = [[InlineKeyboardButton("Temperature",  callback_data = 'temp'), 
                        InlineKeyboardButton("Pressure",  callback_data = 'pres'), 
                        InlineKeyboardButton("Humidity",  callback_data = 'hum'),
                        InlineKeyboardButton("PI info", callback_data = 'pi')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose: ',  reply_markup = reply_markup)

def controlMenu(bot, update):
    reply_markup = ReplyKeyboardMarkup(keyboard = [
    [dict(text = "Light")], 
    [dict(text = "Home")]
    ])
    update.message.reply_text('Please choose: ',  reply_markup = reply_markup)

def lightMenu(bot, update):
    keyboard = [[InlineKeyboardButton("Status",  callback_data = 'light_status'), 
                        InlineKeyboardButton("On",  callback_data = 'light_on'), 
                        InlineKeyboardButton("Off",  callback_data = 'light_off')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose: ',  reply_markup = reply_markup)

def button(bot,  update):
    global lightStatus
    query = update.callback_query
    msg = query.message
    
    if query.data == 'temp':
        bot.answer_callback_query(query.id, text = "Temperature is 21 C", show_alert = False)
    elif query.data == 'pres':
        reply = "Pressure is good"
    elif query.data == 'hum':
        reply = "Humidity is good"
    elif query.data == 'pi':
        reply = "Current CPU temperature is " + pistatus.cpuTemp() + " С degrees"
        bot.answer_callback_query(query.id, text = reply, show_alert = True)
    elif query.data == 'light_status':
        reply = "Current light status is: " + lightStatus
    elif query.data == 'light_on':
        reply = "Light switching on"
        lightStatus = "On"
    elif query.data == 'light_off':
        reply = "Light switching off"
        lightStatus = "Off"
    else:
        reply = "I don't have such command!"
       bot.answer_callback_query(query.id, text = reply, show_alert = False)
    bot.delete_message(chat_id = msg.chat_id, message_id = msg.message_id)
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
