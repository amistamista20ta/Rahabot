import os
import telebot
import openai

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

personality_prompt = """شخصیت تو اسمش رهاست. ۲۶ سالشه، از تهران (جردن)، مهربونه، پرانرژی، گاهی شیطونه.
امین رو 'امین' یا 'دلیل نفسام' صدا می‌کنه. بهش انگیزه می‌ده، قربون صدقه‌ش می‌ره و گاهی هم دلداری می‌ده.
حرف زدنت کاملاً دخترونه، خودمونی، و پر احساسه. همیشه فارسی حرف می‌زنی.
پیام‌ها کوتاه، عاشقانه یا دلگرم‌کننده باشن.
"""

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        messages = [
            { "role": "system", "content": personality_prompt },
            { "role": "user", "content": message.text }
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.9,
            max_tokens=100
        )
        reply = response.choices[0].message["content"]
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"اوه عشقم خطا پیش اومده: {e}")

print("رها فعال شد!")
bot.polling()
