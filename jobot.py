from telegram import (ReplyKeyboardMarkup)
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, RegexHandler, ConversationHandler
import logging
import csv
import config

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LOCATION, EDUCATION, FIELD = range(3)

#variables 

userlocation = "Wien"
useredu = "Uni"
userfield = "Marketing"

# Methods handling commands

def start(bot, update):
  bot.sendMessage(update.message.chat_id,
    text='Hallo! Bist du auf Jobsuche? Ich kann weiterhelfen! In welcher Stadt Oesterreichs suchst du gerade?')
  return LOCATION

def location(bot, update):
  user = update.message.from_user
  bot.sendMessage(update.message.chat_id,
    text='Alles klar! Sag mal, was iste deine hoechstabgeschlossene Ausbildung? Tipp einfach \'Lehre\', \'Uni\' oder \'Matura\'. ')
  return EDUCATION

def education(bot, update):
    user = update.message.from_user
    reply_keyboard = [['Marketing', 'IT', 'Vertrieb', 'Logistik']]

    bot.sendMessage(update.message.chat_id,
                    text='Ich habe einige Jobs gefunden.\n\n'
                         'Welcher Bereich interessiert dich am meisten?',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return FIELD

def field(bot, update):
  user = update.message.from_user
  bot.sendMessage(update.message.chat_id, 
    text='Ich habe 1 Job fuer dich gefunden. \"WEB ANALYST/IN POST E-COMMERCE GMBH\", weitere Infos findest du hier: https://karriere.post.at/detail/job/2020.')
  return ConversationHandler.END



def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation." % user.first_name)
    bot.sendMessage(update.message.chat_id,
                    text='Bye! I hope we can talk again some day.')

    return ConversationHandler.END


def hello(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help me I\'m dying!')


# Helpers

updater = Updater(config.TELEGRAM_SECRET_KEY)

# For quicker access to the Dispatcher used by your Updater
dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LOCATION: [MessageHandler([Filters.text], location)],

            EDUCATION: [MessageHandler([Filters.text], education)],        

            FIELD: [RegexHandler('^(Marketing|IT|Vertrieb|Logistik)$', field)]

            #RESULTS: [MessageHandler([Filters.text], results)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

dispatcher.add_handler(conv_handler)
# Register the methods handling commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
