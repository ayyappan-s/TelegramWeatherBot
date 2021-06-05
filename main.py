from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from WeatherUpdate import getForecasts

updater = Updater(token="Telegram-Bot-Token")

dispatcher = updater.dispatcher


def getLocation(update, context):
    button = [
        [KeyboardButton("Share Location", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(button)
    context.bot.send_message(chat_id=update.message.chat_id, text="Please Share Your Location",
                             reply_markup=reply_markup)


def location(update, context):
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    forecasts = getForecasts(lat, lon)

    context.bot.send_message(chat_id=update.message.chat_id,
                             text=forecasts,
                             reply_markup=ReplyKeyboardRemove())


locationhandler = MessageHandler(Filters.location, location)
dispatcher.add_handler(locationhandler)
getLocation_handler = CommandHandler("start", getLocation)
dispatcher.add_handler(getLocation_handler)

updater.start_polling()
