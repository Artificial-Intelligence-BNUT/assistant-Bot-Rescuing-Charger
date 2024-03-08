import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from TConsts import *
from TConsts import __token as TOKEN
import random
from BatterySaverbot import BatterySaverBot


MODES = {1: "Chat Mode", 2: "Battery Saver Mode choose origin", 3: "Battery Saver Mode choose destination", 4: "Ended"}
current_mode = MODES[1]
n = 0
origin_i = -1
origin_j = -1

destination_i = -1
destination_j = -1

battery_saver_bot = BatterySaverBot()


def find_appropriate_answer(text):
    if text.isnumeric():
        return int(text)
    global current_mode
    text = text.lower()
    for intense in dictionary["intense"]:
        for pattern in intense["patterns"]:
            if pattern in text:
                if intense["tag"] == "BatterySaverBot":
                    current_mode = MODES[2]
                    return intense["response"][random.randint(0, len(intense["response"]) - 1)] + "\n یک عدد انتخاب کن"
                return intense["response"][random.randint(0, len(intense["response"]) - 1)]
    return text + " خودتی"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if current_mode == MODES[2]:
        keyboard = []
        if text.isnumeric():
            global n
            n = int(text)
            for i in range(n):
                keys = []
                for j in range(n):
                    keys.append(InlineKeyboardButton(i * n + j+1, callback_data=f"{[i, j]}"))
                keyboard.append(keys)
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("مبدا را انتخاب کنید:", reply_markup=reply_markup)

    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=find_appropriate_answer(text))


async def battery_saver(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    global origin_i
    global origin_j
    global destination_i
    global destination_j

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    keyboard = []
    global current_mode

    if current_mode == MODES[3]:
        for i in range(n):
            keys = []
            for j in range(n):
                if str([i, j]) == query.data:
                    destination_i = j
                    destination_j = i
                    battery_saver_bot.find_path(origin_i, origin_j, destination_i, destination_j)
                if (j == origin_i and i == origin_j) or (j == destination_i and i == destination_j):
                    keys.append(InlineKeyboardButton(text="❌", callback_data=f"{[i, j]}"))

                else:
                    keys.append(InlineKeyboardButton(i * n + j + 1, callback_data=f"{[i, j]}"))
        for i in range(n):
            keys = []
            for j in range(n):
                place = [i, j]
                if (j == origin_i and i == origin_j) or (j == destination_i and i == destination_j):
                    keys.append(InlineKeyboardButton(text="❌", callback_data=f"{[i, j]}"))

                elif place in battery_saver_bot.places:
                    keys.append(InlineKeyboardButton(text="✅", callback_data=f"{[i, j]}"))

                else:
                    keys.append(InlineKeyboardButton(i * n + j + 1, callback_data=f"{[i, j]}"))

            keyboard.append(keys)


        current_mode = MODES[4]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text=f"مسیر شما:", reply_markup=reply_markup)



    if current_mode == MODES[2]:
        for i in range(n):
            keys = []
            for j in range(n):
                if str([i, j]) == query.data:
                    keys.append(InlineKeyboardButton(text="❌", callback_data=f"{[i, j]}"))
                    origin_i = j
                    origin_j = i
                else:
                    keys.append(InlineKeyboardButton(i * n + j + 1, callback_data=f"{[i, j]}"))

            keyboard.append(keys)

        current_mode = MODES[3]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text=f"مقصد خود را انتخاب کنید:", reply_markup=reply_markup)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="سلام به چت بات آریانور خیلی خوش اومدی")


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    message_handler = MessageHandler(filters.TEXT, send_message)
    application.add_handler(message_handler)

    application.add_handler(CallbackQueryHandler(battery_saver))
    application.run_polling()