from send_buttons import send_countries,send_regions
from database import Database
db = Database("sample-database.db")

def inline_handler(update, context):
    query = update.callback_query
    print(query.data)
    data_sp = str(query.data).split("_")
    if data_sp[0] == "region":
        if data_sp[1].isdigit():
            countries = db.get_countries_by_region(int(data_sp[1]))
            send_countries(context=context, countries=countries, chat_id=query.message.chat_id,
                           message_id=query.message.message_id)

        elif data_sp[1] == 'back':
            regions = db.get_all_regions()
            send_regions(context=context, regions=regions, chat_id=query.message.chat_id,
                         message_id=query.message.message_id)

    if data_sp[0] == "country":
        pass
    if data_sp[0] == 'close':
        msg = query.message.edit_text(
            text="🕓",
            reply_markup=None,
        )
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=msg.message_id)