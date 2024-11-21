import telebot
from fog import gen_pass 
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7750500369:AAGh5wDBuievLpxTsW5CAjyy4tt1mFAPVvc")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=['pass'])
def send_pass(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['plastic'])
def send_plastic(message):
    with open(f'plastic.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  
    bot.reply_to(message, "пластмассовые изделия созданных по разным технологиям, колеблется от 6 месяцев до 700 лет. Полиэтиленовые пакеты разлагаются от 100 до 200 лет.")

@bot.message_handler(commands=['glass'])
def glass_plastic(message):
    with open(f'glass.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
    bot.reply_to(message, "Стекло разлагается более 1000 лет")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    

    
bot.polling()