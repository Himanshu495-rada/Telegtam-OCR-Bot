import telegram
from telegram import bot
from telegram.bot import Bot
from telegram.ext import *
import numpy as np
from PIL import Image
import pytesseract
from telegram.update import Update

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def start_command(update, context):
    name = update.message.chat.first_name

    update.message.reply_text("Hello " + name + "😃😃")
    update.message.reply_text("Please share your image to extract the text")


def photo_handler(update, context):
    try:
        file = update.message.photo[2].file_id
        print(update.message.photo)
        print("file", file)
        obj = context.bot.get_file(file)

        obj.download("file.jpg")
        update.message.reply_text("Processing")

        file_path = "file.jpg"
        img = np.array(Image.open(file_path))
        text = pytesseract.image_to_string(img)
        update.message.reply_text("Got the text")
        # print(text)
        update.message.reply_text(text)
    except:
        update.message.reply_text("Error to load your file 🙄😶")


def main():
    print("Bot is on fire")
    TOKEN = "1939345888:AAF6i2t2hzVnCuEvrvzPZu_01m6iUa318Nk"
    updater = Updater(TOKEN, use_context=True)
    # Bot.delete_webhook()
    # Bot.set_webhook(url)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("photo", photo_handler))
    dp.add_handler(MessageHandler(Filters.photo, photo_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


# telegram token and username of pythonanywhere account
# from flask import Flask, request
# from telegram import Bot, Update
# from telegram.ext import CommandHandler, Dispatcher, MessageHandler, Filters
# import json
# import pytesseract
# import numpy as np
# from PIL import Image

# # handlers


# def start(update, context):
#     name = update.message.chat.first_name

#     update.message.reply_text("Hello " + name + "😃😃🙏🙏")
#     update.message.reply_text("Please share your image to extract the text")


# def help(update, context):
#     """Send a message when the command /help is issued."""
#     update.message.reply_text(
#         'Please send any image from which you want to extract the Text.')
#     update.message.reply_text('Or you can contact my developer @himyaa702')


# def echo(update, context):
#     """Echo the user message."""
#     update.message.reply_text(
#         "I cannot do conversation, please send me any Image😊😊")


# def photo_handler(update, context):
#     try:
#         file = update.message.photo[2].file_id
#         print(update.message.photo)
#         print("file", file)
#         obj = context.bot.get_file(file)

#         obj.download("file.jpg")
#         update.message.reply_text("Processing")

#         file_path = "file.jpg"
#         img = np.array(Image.open(file_path))
#         text = pytesseract.image_to_string(img)
#         update.message.reply_text("Got the text")
#         # print(text)
#         update.message.reply_text(text)
#     except:
#         update.message.reply_text("Error to load your file 🙄😶")


# app = Flask(__name__)


# def main():

#     TOKEN = "1939345888:AAF6i2t2hzVnCuEvrvzPZu_01m6iUa318Nk"
#     bot = Bot(TOKEN)
#     dp = Dispatcher(bot, None, workers=0, use_context=True)
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#     # add handlers
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("help", help))
#     dp.add_handler(MessageHandler(Filters.photo, photo_handler))
#     dp.add_handler(MessageHandler(Filters.text, echo))
#     # start webhook
#     bot.delete_webhook()
#     url = f"https://Himya702.pythonanywhere.com/{TOKEN}"
#     bot.set_webhook(url=url)

#     # process updates
#     @app.route('/' + TOKEN, methods=['POST'])
#     def webhook():
#         json_string = request.stream.read().decode('utf-8')
#         update = Update.de_json(json.loads(json_string), bot)
#         dp.process_update(update)
#         return 'ok', 200


# # make sure you've inserted your app.py name
# if __name__ == "main":
#     main()
