#Settings
from telegram.ext import Updater,  CommandHandler,  MessageHandler,  Filters,  InlineQueryHandler
from telegram import InlineQueryResultArticle,  InputTextMessageContent
updater = Updater(token='624979515:AAGWfi6SYwReEoUdtBh9tAhBLjgYUGZIJKM')
dispatcher = updater.dispatcher

#Callback handling

def startCommand(bot,  update):
    bot.send_message(chat_id = update.message.chat_id,  text = 'Hi, let\'s go')

def textMessage(bot,  update):
    response = 'Got your message: ' + update.message.text
    bot.send_message(chat_id = update.message.chat_id,  text = response)
    
def caps(bot,  update,  args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id = update.message.chat_id,  text = text_caps)
    
def inline_caps(bot,  update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id = query.upper(), 
            title = 'Caps', 
            input_message_content = InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id,  results)
    
#Handlers
start_command_handler = CommandHandler('start',  startCommand)
text_message_handler = MessageHandler(Filters.text,  textMessage)
caps_handler = CommandHandler('caps',  caps,  pass_args = True)
inline_caps_handler = InlineQueryHandler(inline_caps)

#Adding handlers to dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(inline_caps_handler)

#Start seeking for updates
updater.start_polling(clean = True)

#Stop bot if Ctr+C
updater.idle()
