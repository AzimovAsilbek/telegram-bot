# from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
# from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Update
# import requests
# from dotenv import load_dotenv
# import os
#
# # Tokenni yuklash
# load_dotenv()
# TOKEN = os.getenv("TOKEN")
#
#
# # Anime qidirish funksiyasi
# def search_anime(query):
#     url = 'https://graphql.anilist.co'
#     query_string = '''
#     query ($search: String) {
#         Media(type: ANIME, search: $search) {
#             title {
#                 romaji
#                 english
#             }
#             description
#             coverImage {
#                 large
#             }
#             trailer {
#                 site
#                 id
#             }
#         }
#     }
#     '''
#     variables = {"search": query}
#     response = requests.post(url, json={"query": query_string, "variables": variables})
#     if response.status_code == 200:
#         data = response.json()
#         if "data" in data and "Media" in data["data"]:
#             anime = data["data"]["Media"]
#             desc = anime['description']
#             desc = desc.replace("<br>", "\n").replace("<br/>", "\n")
#             desc = (desc[:4000] + "...") if len(desc) > 4000 else desc
#
#             # Treyler URL-ni aniqlash
#             trailer_url = None
#             if anime.get('trailer') and anime['trailer']['site'] == "youtube":
#                 trailer_url = f"https://www.youtube.com/watch?v={anime['trailer']['id']}"
#
#             return {
#                 "text": f"🎬 {anime['title']['romaji']} ({anime.get('title').get('english', 'No English Title')})\n\n{desc}\n",
#                 "image": anime['coverImage']['large'],
#                 "trailer_url": trailer_url
#             }
#         return {"text": "❌ Hech qanday natija topilmadi.", "image": None, "trailer_url": None}
#     return {"text": "❌ API bilan bog'lanishda xatolik yuz berdi.", "image": None, "trailer_url": None}
#
#
# # Anime qidiruv handler
# def anime_search_handler(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("🔍 Qaysi animeni qidiryapsiz? Ismini kiriting:")
#     context.user_data['search_mode'] = True
#
#
# # Foydalanuvchi xabarlarini boshqarish
# def text_handler(update: Update, context: CallbackContext) -> None:
#     if context.user_data.get('search_mode'):
#         query = update.message.text
#         anime_info = search_anime(query)
#
#         # Matn va rasmni yuborish
#         update.message.reply_text(anime_info["text"], parse_mode="HTML")
#         if anime_info["image"]:
#             update.message.reply_photo(photo=anime_info["image"])
#
#         # Treyler uchun tugma qo'shish
#         if anime_info["trailer_url"]:
#             buttons = [
#                 [InlineKeyboardButton(text="🎥 Tomosha qilish", url=anime_info["trailer_url"])]
#             ]
#             reply_markup = InlineKeyboardMarkup(buttons)
#             update.message.reply_text("Treylerni tomosha qiling:", reply_markup=reply_markup)
#
#         context.user_data['search_mode'] = False
#     else:
#         update.message.reply_text("Menyudan biror tugmani tanlang yoki /menu ni yozing.")
#
#
# # Start buyrug'i
# def start(update, context):
#     update.message.reply_text(f"🚀 Assalomu alaykum, {update.effective_user.first_name}. Botimizga xush kelibsiz!")
#
#
# # Menyu ko'rsatish
# def show_menu(update, context):
#     buttons = [
#         [KeyboardButton(text="🔍Anime qidiruv"),
#          KeyboardButton(text="💎Premium"),
#          KeyboardButton(text="🎬Anime filmlar"),
#          KeyboardButton(text="🔄Ongoin Animelar")],
#         [KeyboardButton(text="🖥️Anime ma'lumot qidiruv")],
#         [KeyboardButton(text="💣Premium Animelar"),
#          KeyboardButton(text="📚Barcha Animelar"),
#          KeyboardButton(text="🔴Shorts"),
#          KeyboardButton(text="📞Murojaat")]
#     ]
#     update.message.reply_text(
#         text="Menyu:",
#         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
#     )
#
#
# # Asosiy funksiya
# def main():
#     updater = Updater(token="8030328457:AAHhaV3RvXN9wD-nMeAHO3-E6gykWFobbmQ")
#     dispatcher = updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler('start', start))
#     dispatcher.add_handler(CommandHandler('menu', show_menu))
#     dispatcher.add_handler(MessageHandler(Filters.regex('^🔍Anime qidiruv$'), anime_search_handler))
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_handler))
#
#     updater.start_polling()
#     updater.idle()
#
#
# if __name__ == "__main__":
#     main()

# from telegram.ext import Updater, Filters, MessageHandler, CallbackContext, CommandHandler, CallbackQueryHandler
# from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
# import requests
#
# TOKEN = "8030328457:AAHhaV3RvXN9wD-nMeAHO3-E6gykWFobbmQ"
# REQUIRED_CHANNEL = "@Orbiyaedit1"  # Kanal username yoki chat_id
#
# # Kod va video ma'lumotlari
# CODE_TO_VIDEO = {
#     "NARUTO123": "https://example.com/naruto_video.mp4",
#     "ONEPIECE456": "https://example.com/onepiece_video.mp4",
# }
#
# def check_subscription(user_id):
#     """Obuna holatini tekshiradi."""
#     try:
#         url = f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={REQUIRED_CHANNEL}&user_id={user_id}"
#         response = requests.get(url).json()
#         print(f"Obuna tekshiruvi natijasi: {response}")  # Debug maqsadida
#         if response.get("ok"):
#             status = response['result']['status']
#             return status in ['member', 'administrator', 'creator']
#     except Exception as e:
#         print(f"Xatolik: {e}")
#     return False
#
# def start(update: Update, context: CallbackContext):
#     """Boshlang‘ich xabar va obuna uchun tugmalar."""
#     keyboard = InlineKeyboardMarkup([
#         [InlineKeyboardButton("✅ Obuna bo‘lish", url=f"https://t.me/{REQUIRED_CHANNEL[1:]}")],
#         [InlineKeyboardButton("Tasdiqlash", callback_data="verify_subscription")]
#     ])
#     update.message.reply_text(
#         f"🎉 Assalomu alaykum, {update.effective_user.first_name}!\n"
#         f"Botdan foydalanish uchun kanalga obuna bo‘ling: {REQUIRED_CHANNEL}\n\n"
#         "Obuna bo‘lganingizdan keyin 'Tasdiqlash' tugmasini bosing.",
#         reply_markup=keyboard
#     )
#
# def verify_subscription(update: Update, context: CallbackContext):
#     """Foydalanuvchi obunasini tasdiqlash."""
#     query = update.callback_query
#     query.answer()
#     user_id = query.from_user.id
#
#     if check_subscription(user_id):
#         query.edit_message_text(
#             "✅ Obuna tasdiqlandi! Endi anime kodini yuboring."
#         )
#         context.user_data['access_granted'] = True
#     else:
#         query.edit_message_text(
#             "❌ Obuna tasdiqlanmadi. Iltimos, avvalo kanalga obuna bo‘ling."
#         )
#
# def handle_code(update: Update, context: CallbackContext):
#     """Kodga mos videoni yuborish."""
#     if not context.user_data.get('access_granted'):
#         update.message.reply_text(
#             "❌ Obuna tasdiqlanmagan. Avval /start komandasini yuboring va tasdiqlashni bajaring."
#         )
#         return
#
#     user_code = update.message.text.strip()
#     video_url = CODE_TO_VIDEO.get(user_code)
#
#     if video_url:
#         update.message.reply_video(video_url, caption="🎬 Mana sizning so‘ralgan anime videosi!")
#     else:
#         update.message.reply_text("❌ Noto‘g‘ri kod. Iltimos, to‘g‘ri kodni yuboring.")
#
# def main():
#     updater = Updater(token="8030328457:AAHhaV3RvXN9wD-nMeAHO3-E6gykWFobbmQ")
#     dispatcher = updater.dispatcher
#
#     # Komandalar
#     dispatcher.add_handler(CommandHandler('start', start))
#     dispatcher.add_handler(CallbackQueryHandler(verify_subscription, pattern="^verify_subscription$"))
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_code))
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == "__main__":
#     main()

import sqlite3
from telegram.ext import Updater, Filters, MessageHandler, CallbackContext, CommandHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
import requests

# Bot token
TOKEN = "8030328457:AAHhaV3RvXN9wD-nMeAHO3-E6gykWFobbmQ"
REQUIRED_CHANNEL = "@Orbiyaedit1"  # Kanal username
DATABASE = "anime_videos.db"  # Ma'lumotlar bazasi fayli

def init_db():
    """Ma'lumotlar bazasini yaratish."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            file_id TEXT NOT NULL,
            title TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_video(code, file_id, title=None):
    """Ma'lumotlar bazasiga yangi video qo'shish (mavjudligini tekshiradi)."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM videos WHERE code = ?", (code,))
    exists = cursor.fetchone()
    if exists:
        print(f"❌ Video '{code}' kodi bilan allaqachon mavjud!")
    else:
        cursor.execute("INSERT INTO videos (code, file_id, title) VALUES (?, ?, ?)", (code, file_id, title))
        conn.commit()
        print(f"✅ Video '{code}' muvaffaqiyatli qo'shildi!")
    conn.close()

def fetch_video_by_code(code):
    """Kod bo'yicha video ma'lumotlarini olish."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT file_id, title FROM videos WHERE code = ?", (code,))
    result = cursor.fetchone()
    conn.close()
    return result

def check_subscription(user_id):
    """Foydalanuvchining kanalga obuna bo‘lganligini tekshiradi."""
    url = f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={REQUIRED_CHANNEL}&user_id={user_id}"
    response = requests.get(url).json()
    if response.get("ok"):
        status = response['result']['status']
        return status in ['member', 'administrator', 'creator']
    return False

def start(update: Update, context: CallbackContext):
    """Start komandasini ishlovchi funksiyasi."""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Obuna bo‘lish", url=f"https://t.me/{REQUIRED_CHANNEL[1:]}")],
        [InlineKeyboardButton("Tasdiqlash", callback_data="verify_subscription")]
    ])
    update.message.reply_text(
        "🎉 Assalomu alaykum! Anime botga xush kelibsiz!\n"
        f"Videoni olishdan oldin quyidagi kanalga obuna bo‘ling: {REQUIRED_CHANNEL}\n"
        "Obuna bo‘lganingizdan keyin 'Tasdiqlash' tugmasini bosing.",
        reply_markup=keyboard
    )

def verify_subscription(update: Update, context: CallbackContext):
    """Foydalanuvchining obuna bo‘lganligini tekshiradi."""
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id

    if check_subscription(user_id):
        query.edit_message_text(
            "✅ Obuna tasdiqlandi! Endi istalgan kodni yuboring."
        )
        context.user_data['access_granted'] = True
    else:
        query.edit_message_text(
            "❌ Obuna tasdiqlanmadi. Iltimos, avvalo kanalga obuna bo‘ling."
        )

def handle_code(update: Update, context: CallbackContext):
    """Foydalanuvchining yuborgan kodiga mos video yoki xabarni qaytaradi."""
    if not context.user_data.get('access_granted', False):
        update.message.reply_text(
            "❌ Obuna tasdiqlanmagan. Avval /start komandasini yuboring va tasdiqlashni bajaring."
        )
        return

    user_code = update.message.text.strip()
    video = fetch_video_by_code(user_code)

    if video:
        file_id, title = video
        try:
            update.message.reply_video(
                video=file_id,
                caption=f"🎬 Mana sizning {user_code}-raqamli videongiz!\n{title or ''}"
            )
        except Exception as e:
            update.message.reply_text(f"❌ Video yuborishda xatolik yuz berdi: {e}")
    else:
        update.message.reply_text("❌ Noto‘g‘ri kod. Iltimos, to‘g‘ri kodni yuboring.")

def main():
    """Botni ishga tushirish uchun asosiy funksiya."""
    init_db()

    # Ma'lumotlar bazasiga namuna videolarni qo'shish
    insert_video("1", "https://youtu.be/aDuXkxXssGM?si=3jRC7OPmyHb_C1Kc", "Naruto Episode 1")
    insert_video("2", "https://www.youtube.com/watch?v=-1hI9WSqTxU", "One Piece Episode 1")

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(verify_subscription, pattern="^verify_subscription$"))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_code))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
