import os
import re
import time
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import yt_dlp

# التوكن المدمج الخاص بك
BOT_TOKEN = "8769909121:AAFpYlnGqoHEux7sBIoFa3hB_QJvvUzrn0I"
bot = telebot.TeleBot(BOT_TOKEN)

# معرف المطور الخاص بك
DEVELOPER_USERNAME = "X_glvn"

# --- تصميم لوحة أزرار واحدة ضخمة تشمل جميع الأوامر ---

def get_all_commands_menu():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    # المجموعة 1
    markup.row(KeyboardButton("🎮 لعبة XO"))
    markup.row(KeyboardButton("🧠 الذكاء الاصطناعي"), KeyboardButton("⚪ معرفة رقم الضحية"))
    markup.row(KeyboardButton("🟢 رسالة فك حظر واتساب"), KeyboardButton("🤣 أعطيني نكتة"))
    markup.row(KeyboardButton("💬 رسالة فك حظر تيك توك"), KeyboardButton("🚫 رسالة حظر تيك توك"))
    markup.row(KeyboardButton("📱 رسالة فك حظر انستجرام"), KeyboardButton("🕵️‍♂️ كيف أصبح هاكر"))
    markup.row(KeyboardButton("🖼️ توليد الصور"), KeyboardButton("👤 معرفة شبيهك"))
    markup.row(KeyboardButton("📹 تحميل فيديوهات"), KeyboardButton("💥 الهجوم على IP الضحية"))
    markup.row(KeyboardButton("📺 اختراق قنوات التلفزيون"), KeyboardButton("😈 Worm GPT"))
    markup.row(KeyboardButton("🪪 هويات مزوره"), KeyboardButton("💳 فيزات مسربه"))
    
    # المجموعة 2
    markup.row(KeyboardButton("🔲 قراءة باركود"), KeyboardButton("💳 كروت جوجل ابلاي"))
    markup.row(KeyboardButton("🪓 ضرب بلاغ تويتر X"), KeyboardButton("🔲 إنشاء باركود"))
    markup.row(KeyboardButton("▶️ ضرب بلاغ يوتيوب"), KeyboardButton("👻 ضرب بلاغ سناب"))
    markup.row(KeyboardButton("🔸 ضرب بلاغ تيك توك"), KeyboardButton("🗳️ ضرب بلاغ تلجرام"))
    markup.row(KeyboardButton("🎬 استخراج صورة يوتيوب"), KeyboardButton("🗡️ ضرب بلاغ انستجرام"))
    markup.row(KeyboardButton("☠️ اختراق المواقع"), KeyboardButton("🔗 اختصار روابط"))
    markup.row(KeyboardButton("🌍 تتبع IP"))
    
    # المجموعة 3
    markup.row(KeyboardButton("📷 اختراق الكاميرا الخلفية"), KeyboardButton("📸 اختراق الكاميرا الأمامية"))
    markup.row(KeyboardButton("🎤 تسجيل صوت الضحيه"), KeyboardButton("📍 اختراق الموقع"))
    markup.row(KeyboardButton("🎥 تصوير الضحية فيديو"), KeyboardButton("🎥 اختراق كاميرات المراقبة"))
    markup.row(KeyboardButton("📱 اختراق انستجرام"), KeyboardButton("🟢 اختراق واتساب"))
    markup.row(KeyboardButton("🔫 اختراق ببجي"), KeyboardButton("👤 اختراق فيسبوك"))
    markup.row(KeyboardButton("⭐️ اختراق سناب شات"), KeyboardButton("🔥 اختراق فري فاير"))
    markup.row(KeyboardButton("🤖 الذكاء الاصطناعي 2"), KeyboardButton("🔸 اختراق تيك توك 2"))
    markup.row(KeyboardButton("🔮 تفسير الأحلام"), KeyboardButton("📱 جمع معلومات الجهاز"))
    markup.row(KeyboardButton("🔞 اختراق الهاتف كاملاً"), KeyboardButton("⚠️ تلغيم رابط"))
    markup.row(KeyboardButton("🧞‍♂️ لعبة المارد الأزرق"), KeyboardButton("🧠 لعبة الأذكياء"))
    
    # المجموعة 4
    markup.row(KeyboardButton("🖼️ تصوير بدقه عاليه"), KeyboardButton("💳 صيد فيزات"))
    markup.row(KeyboardButton("🚨 الارقام وهميه"), KeyboardButton("📱 معرفة رقم الضحيه 2"))
    markup.row(KeyboardButton("🔎 البحث عن صور"), KeyboardButton("🪄 فحص الروابط"))
    markup.row(KeyboardButton("📻 اختراق بث الراديو"))
    markup.row(KeyboardButton("🎵 تحويل النص إلى صوت"), KeyboardButton("🔤 زخرفة الاسماء"))
    markup.row(KeyboardButton("🔑 صيد يوزرت تلجرام"), KeyboardButton("🔮 تفسير الأحلام 2"))
    markup.row(KeyboardButton("🎁 جمع نقاط"), KeyboardButton("💰 رصيدي"))
    
    # زر المطور البرمجي المميز في الأسفل
    markup.row(KeyboardButton("↗️ التواصل مع المطور البرمجي"))
    
    return markup

# --- معالجة الأوامر والرسائل ---

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = f"مرحباً بك في بوت الخدمات الشامل الذكي!\nالمطور البرمجي للبوت: @{DEVELOPER_USERNAME}\n\nجميع الأوامر متاحة الآن في صفحة واحدة بالأسفل، أو يمكنك إرسال أي رابط فيديو لتحميله فوراً."
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_all_commands_menu())

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text
    chat_id = message.chat.id

    # 1. فحص روابط التحميل التلقائي أولاً
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F]))+')
    if url_pattern.search(text):
        bot.reply_to(message, "🔄 جاري فحص الرابط وتحميل الفيديو ذكياً... يرجى الانتظار.")
        download_and_send_video(message, text)
        return

    # 2. تشغيل الأوامر والردود المخصصة لكل زر
    if text == "↗️ التواصل مع المطور البرمجي":
        bot.send_message(chat_id, f"👑 المطور البرمجي للبوت هو المبدع:\n\nusername: @{DEVELOPER_USERNAME}")
    
    elif text == "🎮 لعبة XO":
        bot.send_message(chat_id, "⚙️ أمر [لعبة XO] شغال... ضع كود الأداة الخاص بك هنا.")
        
    elif text == "🧠 الذكاء الاصطناعي" or text == "🤖 الذكاء الاصطناعي 2":
        bot.send_message(chat_id, "⚙️ أمر [الذكاء الاصطناعي] شغال... ضع كود الربط بـ ChatGPT هنا.")
        
    elif text == "🖼️ توليد الصور":
        bot.send_message(chat_id, "⚙️ أمر [توليد الصور] شغال... ضع أداة التوليد هنا.")
        
    elif text == "🟢 رسالة فك حظر واتساب":
        bot.send_message(chat_id, "⚙️ كود فك حظر واتساب جاهز للاستخدام.")
        
    elif text == "😈 Worm GPT":
        bot.send_message(chat_id, "⚙️ أداة Worm GPT قيد التحضير.")
        
    # يمكنك تكرار elif لكل زر ترغب في تفعيل كود برمي خاص به بشكل مباشر
    else:
        # رد تلقائي عام لبقية الأزرار لكي لا يقف البوت حتى تضع أكوادها المخصصة بنفسك
        bot.reply_to(message, f"لقد قمت باختيار خدمة: **{text}**\n\n⚙️ الأداة مجهزة وشغالة داخل السكريبت وجاهزة لربطها بملفاتك البرمجية الخاصة.")

# --- دالة التحميل الذكي المستقر من جميع المنصات ---

def download_and_send_video(message, url):
    chat_id = message.chat.id
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            with open(filename, 'rb') as video:
                bot.send_video(chat_id, video, caption=f"✨ تم التحميل بنجاح!\nBy: @{DEVELOPER_USERNAME}")
            
            os.remove(filename)
            
    except Exception as e:
        bot.send_message(chat_id, f"❌ تعذر تحميل الفيديو. تأكد من صحة الرابط أو جرب لاحقاً.")
        print(f"Error downloading: {e}")

# --- كود الحماية المطور لمنع توقف السكريبت نهائياً ---

print("البوت شغال بكافة الأوامر في صفحة واحدة...")
while True:
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"البوت وقع، هرجع اشغله تاني... {e}")
        time.sleep(5)

