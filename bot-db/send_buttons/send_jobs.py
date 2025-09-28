from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def send_jobs(context, jobs, chat_id, message_id=None):
    buttons = []
    for job in jobs:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"{job['job_title']}",
                    callback_data=f"job_{job['job_id']}")
            ]
        )
    buttons.append([InlineKeyboardButton(text="Close", callback_data="close")])

    if message_id:
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<b>Choose jobs</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text="<b>Choose jobs</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )
