from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def send_countries(context, countries, chat_id, message_id=None):
    buttons = []
    for country in countries:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"{country['country_name']}",
                    callback_data=f"country_{country['country_id']}")
            ]
        )
    buttons.append([InlineKeyboardButton(text="Back", callback_data="region_back")])

    if message_id:
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<b>Choose countries</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text="<b>Choose countries</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )
