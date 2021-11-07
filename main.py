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
    TOKEN = "Enter your token"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("photo", photo_handler))
    dp.add_handler(MessageHandler(Filters.photo, photo_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
