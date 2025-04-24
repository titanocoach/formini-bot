import telebot

BOT_TOKEN = "7981028674:AAFzz_e6hlUbUJJJJ1GXD1Twg2bo20V36Aw"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue sur Formini 🎓 ! Tape /module1 pour commencer la formation.")

@bot.message_handler(commands=['module1'])
def module1(message):
    bot.send_message(message.chat.id, "📘 Module 1 : L’écoute active\n\nL'écoute active est la clé d'une bonne relation client. Vrai ou faux ?\n\nRépondez : /vrai ou /faux")

@bot.message_handler(commands=['vrai'])
def vrai(message):
    bot.send_message(message.chat.id, "✅ Bonne réponse ! L'écoute active est essentielle. Bravo ! 🎉")

@bot.message_handler(commands=['faux'])
def faux(message):
    bot.send_message(message.chat.id, "❌ Mauvaise réponse. Revois le module puis retente !")

bot.polling()
