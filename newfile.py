import os
import telebot
from yt_dlp import YoutubeDL

# আপনার বটের HTTP API টোকেন
BOT_TOKEN = "8457949071:AAFVE5mm22E0EjWp8PcdWT6DR1Vhu3MPHUY"
bot = telebot.TeleBot(BOT_TOKEN)

print("🚀 Premium Media Bot চালু হচ্ছে...")

# /start এবং /help কমান্ড হ্যান্ডলার
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🌟 *Welcome to Premium Media Bot* 🌟\n\n"
        "আমি আপনাকে যেকোনো লিংক থেকে মিউজিক এবং ভিডিও ডাউনলোড করে দিতে পারি।\n\n"
        "*প্রধান কমান্ডসমূহ:*\n"
        "🎵 /play `[গানের নাম/লিংক]` - মিউজিক প্লে/ডাউনলোড\n"
        "🎥 /video `[লিংক]` - ভিডিও ডাউনলোড\n"
        "⚙️ /download `[লিংক]` - অডিও/ভিডিও ডাউনলোড\n\n"
        "শুধু যেকোনো গান বা ভিডিওর লিংক আমাকে পাঠান, বাকি কাজ আমি করছি!"
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

# /play কমান্ড (অডিও ডাউনলোড)
@bot.message_handler(commands=['play'])
def play_music(message):
    query = message.text.replace('/play', '').strip()
    if not query:
        bot.reply_to(message, "❌ দয়া করে গানের নাম বা একটি লিংক দিন। যেমন: `/play tum hi ho`", parse_mode='Markdown')
        return

    status_msg = bot.reply_to(message, "🔍 আপনার গানটি খোঁজা হচ্ছে এবং প্রসেস করা হচ্ছে... একটু অপেক্ষা করুন।")
    
    # yt-dlp এর মাধ্যমে অডিও ডাউনলোডের কনফিগারেশন
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    try:
        # সার্চ কুয়েরি হলে ytsearch ব্যবহার করবে
        if not query.startswith("http"):
            query = f"ytsearch:{query}"

        with YoutubeDL(ydl_opts) as ydl:
            bot.edit_message_text("📥 ফাইলটি ডাউনলোড করা হচ্ছে...", chat_id=message.chat.id, message_id=status_msg.message_id)
            info = ydl.extract_info(query, download=True)
            
            # যদি সার্চ রেজাল্ট হয়, তবে প্রথম এলিমেন্টটি নেবে
            if 'entries' in info:
                video_info = info['entries'][0]
            else:
                video_info = info
                
            title = video_info.get('title', 'Audio')
            # yt-dlp এক্সটেনশন অটোমেটিক mp3 করে দেয় পোস্টপ্রসেসরে
            filename = ydl.prepare_filename(video_info).rsplit('.', 1)[0] + ".mp3"

        bot.edit_message_text("📤 টেলিগ্রামে আপলোড করা হচ্ছে...", chat_id=message.chat.id, message_id=status_msg.message_id)
        
        # অডিও ফাইল পাঠানো
        with open(filename, 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption=f"🎵 *{title}* \n\n⚡ Powered by Premium Media Bot", parse_mode='Markdown')
        
        # কাজ শেষে লোকাল ফাইল ডিলিট করা (স্টোরেজ বাঁচানোর জন্য)
        os.remove(filename)
        bot.delete_message(chat_id=message.chat.id, message_id=status_msg.message_id)

    except Exception as e:
        bot.edit_message_text(f"❌ দুঃখিত, গানটি ডাউনলোড করা যায়নি। সঠিক লিংক বা নাম ট্রাই করুন।", chat_id=message.chat.id, message_id=status_msg.message_id)
        print(f"Error: {e}")

# /video কমান্ড (ভিডিও ডাউনলোড)
@bot.message_handler(commands=['video', 'download'])
def download_video(message):
    url = message.text.split(maxsplit=1)
    if len(url) < 2:
        bot.reply_to(message, "❌ দয়া করে ভিডিওর সঠিক লিংকটি দিন। যেমন: `/video https://...`", parse_mode='Markdown')
        return
    
    video_url = url[1].strip()
    status_msg = bot.reply_to(message, "🔍 ভিডিও লিংকটি প্রসেস করা হচ্ছে...")

    # ভিডিও ডাউনলোডের কনফিগারেশন (720p বা তার নিচে যাতে টেলিগ্রামে সহজে আপলোড হয়)
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            bot.edit_message_text("📥 ভিডিও ফাইলটি ডাউনলোড করা হচ্ছে...", chat_id=message.chat.id, message_id=status_msg.message_id)
            info = ydl.extract_info(video_url, download=True)
            title = info.get('title', 'Video')
            filename = ydl.prepare_filename(info)

        bot.edit_message_text("📤 ভিডিওটি টেলিগ্রামে আপলোড করা হচ্ছে...", chat_id=message.chat.id, message_id=status_msg.message_id)
        
        # ভিডিও ফাইল পাঠানো
        with open(filename, 'rb') as video:
            bot.send_video(message.chat.id, video, caption=f"🎥 *{title}* \n\n⚡ Powered by Premium Media Bot", parse_mode='Markdown')
        
        os.remove(filename)
        bot.delete_message(chat_id=message.chat.id, message_id=status_msg.message_id)

    except Exception as e:
        bot.edit_message_text(f"❌ ভিডিওটি ডাউনলোড করা সম্ভব হয়নি। লিংকটি আবার চেক করুন।", chat_id=message.chat.id, message_id=status_msg.message_id)
        print(f"Error: {e}")

# বটটিকে সবসময় সচল রাখার জন্য
bot.infinity_polling()
