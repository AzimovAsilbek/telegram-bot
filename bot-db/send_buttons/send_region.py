from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def send_regions(context, regions, chat_id, message_id=None):
    buttons = []
    for region in regions:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"{region['region_name']}",
                    callback_data=f"region_{region['region_id']}")
            ]
        )
    buttons.append([InlineKeyboardButton(text="Close", callback_data="close")])

    if message_id:
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<b>Choose regions</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text="<b>Choose regions</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )
