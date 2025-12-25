import telebot
from telebot import types

# -----------------------------------------------------------------------
# SOZLAMALAR (SETTINGS)
# Bu yerga BotFather dan olgan tokeningizni qo'ying
# Masalan: '123456789:AAH...'
BOT_TOKEN = '8484942275:AAHZTcqpkUQyz1RuIwawm4Pd2jxHcCTDDPI'
# -----------------------------------------------------------------------

bot = telebot.TeleBot(BOT_TOKEN)

# /start komandasi uchun handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Tugmalarni yaratamiz
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📞 Biz bilan bog'lanish")
    item2 = types.KeyboardButton("📍 Manzil")
    item3 = types.KeyboardButton("🌐 Saytga o'tish")
    markup.add(item1, item2, item3)

    welcome_text = (
        f"Assalomu alaykum, {message.from_user.first_name}!\n"
        "Doni Granit rasmiy botiga xush kelibsiz.\n\n"
        "Biz sizga sifatli granit va marmar mahsulotlarini taklif etamiz.\n"
        "Quyidagi tugmalar orqali ma'lumot olishingiz mumkin."
    )
    
    bot.reply_to(message, welcome_text, reply_markup=markup)

# Matnli xabarlar uchun handler
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == "📞 Biz bilan bog'lanish":
        bot.reply_to(message, "Bizning raqamlarimiz:\n+998 90 123 45 67\n+998 99 987 65 43\n\nAdministrator: @tommysamiyyusuf")
    
    elif message.text == "📍 Manzil":
        bot.reply_to(message, "Bizning manzil: Toshkent shahri, Chilonzor tumani, Bunyodkor ko'chasi 1-uy.")
        # Lokatsiya yuborish (ixtiyoriy)
        # bot.send_location(message.chat.id, 41.2858, 69.2040)
        
    elif message.text == "🌐 Saytga o'tish":
        bot.reply_to(message, "Bizning veb-saytimiz: https://donigranit.uz (Demo)")
        
    else:
        bot.reply_to(message, "Iltimos, quyidagi tugmalardan birini tanlang.")

# Botni ishga tushirish
if __name__ == '__main__':
    print("Bot ishga tushdi...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
