from telegram import ReplyKeyboardMarkup, KeyboardButton


def send_main_menu(context, chat_id):
    buttons = [
        [KeyboardButton(text="Regions"),
         KeyboardButton(text="Jobs")
         ]
    ]
    context.bot.send_message(
        chat_id=chat_id,
        text="Menu:",
        reply_markup=ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    )
