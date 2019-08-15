from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from weather import get_forecasts

updater = Updater(token="922998543:AAFi1oZ4OhGYV8K-aWixbtI3yYyjfDERvz4")

dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, welcome to worldWeather!"
                                                          "\nPlease use the command /location for weather forecast")


start_handler = CommandHandler("start", start)

dispatcher.add_handler(start_handler)


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text.upper())


echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(echo_handler)


def get_location(bot, update):
        button = [
        [KeyboardButton("Share Location", request_location=True)]
        ]
        reply_markup = ReplyKeyboardMarkup(button)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Please share your location",
                         reply_markup=reply_markup)


get_location_handler = CommandHandler("location", get_location)
dispatcher.add_handler(get_location_handler)


def location(bot, update):
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    forecasts = get_forecasts(lat, lon)
    bot.send_message(chat_id=update.message.chat_id,
                     text=forecasts,
                     reply_markup = ReplyKeyboardRemove())


location_handler = MessageHandler(Filters.location, location)
dispatcher.add_handler(location_handler)


updater.start_polling()


