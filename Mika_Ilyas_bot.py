import telebot

from telebot import types
from parsing import valuta
from decouple import config

# Токен бота
bot = telebot.TeleBot(config('bot'))

# создаем кнопки главного меню
keyboard_buy = types.InlineKeyboardMarkup(row_width=2)
button1 = types.InlineKeyboardButton('USD', callback_data='USD')
button2 = types.InlineKeyboardButton('EUR', callback_data='EUR')
button3 = types.InlineKeyboardButton('RUB', callback_data='RUB')
button4 = types.InlineKeyboardButton('KZT', callback_data='KZT')
button5 = types.InlineKeyboardButton('EXIT', callback_data='EXIT')

# кнопки для выхода в главное меню для каждого курса
back_dol = types.InlineKeyboardButton('Главное меню', callback_data='BACK_DOL')
back_eur = types.InlineKeyboardButton('Главное меню', callback_data='BACK_EUR')
back_rub = types.InlineKeyboardButton('Главное меню', callback_data='BACK_RUB')
back_kzt = types.InlineKeyboardButton('Главное меню', callback_data='BACK_KZT')
keyboard_buy.add(button1, button2, button3, button4, button5)



# Курс доллара
musd = types.InlineKeyboardMarkup(row_width=2)
buy_usd = types.InlineKeyboardButton('Покупка', callback_data='BUY_USD')
sell_usd = types.InlineKeyboardButton('Продажа', callback_data='SELL_USD')
pokupka_usd = types.InlineKeyboardButton('Банк по покупке', url="https://valuta.kg/rates/buy/usd/84-75/", callback_data='POKUPKA_USD')
prodaja_usd = types.InlineKeyboardButton('Банк по продаже', url="https://valuta.kg/rates/sell/usd/84-90/", callback_data='PRODAJA_USD')
musd.add(buy_usd, sell_usd, pokupka_usd, prodaja_usd, back_dol)



# Курс евро
meur = types.InlineKeyboardMarkup(row_width=2)
buy_eur = types.InlineKeyboardButton('Покупка', callback_data='BUY_EUR')
sell_eur = types.InlineKeyboardButton('Продажа', callback_data='SELL_EUR')
pokupka_eur = types.InlineKeyboardButton('Банк по покупке', url="https://valuta.kg/rates/buy/eur/102-80/", callback_data='POKUPKA_EUR')
prodaja_eur = types.InlineKeyboardButton('Банк по продаже', url="https://valuta.kg/rates/sell/eur/103-50/", callback_data='PRODAJA_EUR')
meur.add(buy_eur, sell_eur, pokupka_eur, prodaja_eur, back_eur)



# Курс рубля
mrub = types.InlineKeyboardMarkup(row_width=2)
buy_rub = types.InlineKeyboardButton('Покупка', callback_data='BUY_RUB')
sell_rub = types.InlineKeyboardButton('Продажа', callback_data='SELL_RUB')
pokupka_rub = types.InlineKeyboardButton('Банк по покупке', url="https://valuta.kg/rates/buy/rub/1-133/", callback_data='POKUPKA_RUB')
prodaja_rub = types.InlineKeyboardButton('Банк по продаже', url="https://valuta.kg/rates/sell/rub/1-140/", callback_data='PRODAJA_RUB')
mrub.add(buy_rub, sell_rub, pokupka_rub, prodaja_rub, back_rub)



# Курс Тенге
mkzt = types.InlineKeyboardMarkup(row_width=2)
buy_kzt = types.InlineKeyboardButton('Покупка', callback_data='BUY_KZT')
sell_kzt = types.InlineKeyboardButton('Продажа', callback_data='SELL_KZT')
pokupka_kzt = types.InlineKeyboardButton('Банк по покупке', url="https://valuta.kg/rates/buy/kzt/0-2005/", callback_data='POKUPKA_KZT')
prodaja_kzt = types.InlineKeyboardButton('Банк по продаже', url="https://valuta.kg/rates/sell/kzt/0-2020/", callback_data='PRODAJA_KZT')
mkzt.add(buy_kzt, sell_kzt, pokupka_kzt, prodaja_kzt, back_kzt)
   

# Создание функций бота
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    pic = open("photo.img", "rb")
    bot.send_photo(chat_id, pic)
    bot.send_message(chat_id, 'Добро пожаловать в Exchange Portal!', message.chat.first_name, reply_markup=keyboard_buy)
    


# создание условий для каждой кнопки
@bot.callback_query_handler(lambda call:True)
def call_data(call):    
    
    chat_id = call.message.chat.id
    user = call.message.chat.first_name
        

    # Доллар
    if call.data == 'USD':
        bot.edit_message_text(f"Благодарим Вас! Пожалуйста, выберите дальнейшую операцию: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=musd)
    if call.data == 'BUY_USD':
        bot.edit_message_text(f"Курс покупки USD составляет: {valuta[0]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=musd)
    if call.data == 'SELL_USD':
        bot.edit_message_text(f"Курс продажи USD составляет: {valuta[1]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=musd)
    if call.data == 'BACK_DOL':
        bot.edit_message_text(f"Добро пожаловать в Exchange Portal!: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard_buy)
    

    # Евро
    if call.data == 'EUR':
        bot.edit_message_text(f"Благодарим Вас! Пожалуйста, выберите дальнейшую операцию: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=meur)
    if call.data == 'BUY_EUR':
        bot.edit_message_text(f"Курс покупки EUR составляет: {valuta[2]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=meur)
    if call.data == 'SELL_EUR':
        bot.edit_message_text(f"Курс продажи EUR составляет: {valuta[3]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=meur)
    if call.data == 'BACK_EUR':
        bot.edit_message_text(f"Добро пожаловать в Exchange Portal!: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard_buy)


    # Рубль
    if call.data == 'RUB':
        bot.edit_message_text(f"Благодарим Вас! Пожалуйста, выберите дальнейшую операцию: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=mrub)
    if call.data == 'BUY_RUB':
        bot.edit_message_text(f"Курс покупки RUB составляет: {valuta[4]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=mrub)
    if call.data == 'SELL_RUB':
        bot.edit_message_text(f"Курс продажи RUB составляет: {valuta[5]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=mrub)
    if call.data == 'BACK_RUB':
        bot.edit_message_text(f"Добро пожаловать в Exchange Portal!: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard_buy)


    # Тенге
    if call.data == 'KZT':
        bot.edit_message_text(f"Благодарим Вас! Пожалуйста, выберите дальнейшую операцию: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=mkzt)
    if call.data == 'BUY_KZT':
        bot.edit_message_text(f"Курс покупки KZT составляет: {valuta[6]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=mkzt)
    if call.data == 'SELL_KZT':
        bot.edit_message_text(f"Курс продажи KZT составляет: {valuta[7]}", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=mkzt)
    if call.data == 'BACK_KZT':
        bot.edit_message_text(f"Добро пожаловать в Exchange Portal!: ", message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard_buy)


    if call.data == 'EXIT':
        bot.send_message(chat_id, 'Спасибо, что выбрали нас! До свидания!')


def dollar(message):
    chat_id = message.chat.id
    msg1 = bot.send_message(message.chat.id, text='Cпасибо', reply_markup=keyboard_buy)
    bot.register_next_step_handler(msg1, get_finish)


def get_finish(message):
    chat_id = message.chat.id
    show_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)   

def keyb(message):
    # msg2 = bot.send_message(message.chat.id, text='Cпасибо', reply_markup=keyboard)
    bot.send_message_text(f'Вы в калькуляторе! \nЗдесь вы можете подсчитать нужную сумму)', message_id=call.message.message_id, chat_id=chat_id)
    bot.send_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=keyboard)

        
bot.polling(none_stop=True) 