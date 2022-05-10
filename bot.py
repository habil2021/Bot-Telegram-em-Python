import telebot

botToken = "5330182492:AAE6bQYsaTauFsWEScJhWy6SdXWa0-F1g1Y"



bot = telebot.TeleBot(botToken)
@bot.message_handler(commands=['info'])
def menu(mensagem):
 bot.reply_to(mensagem,f"""ℹSuas informações \n\n 🌏Linguagem: {mensagem.from_user.language_code} \n 👤Nome de usuario: {mensagem.from_user.username} \n 📄Primeiro nome: {mensagem.from_user.first_name} \n 📄Último nome: {mensagem.from_user.last_name} \n 💬ID: {mensagem.from_user.id} \n\n 🤖Created by @habil_hb""")

 
bot.polling()