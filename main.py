# This is a sample Python script.
import telebot
from telebot import types
from datetime import datetime
bot = telebot.TeleBot('5695208283:AAEzuZD4qPJ4qlcH2eqYUF2YAEh50YO7Kjw')
name = ''
@bot.message_handler(content_types = ['text'])
@bot.message_handler(commands=['start'])
def bd(message):
    user_id = str(message.from_user.id)                                                                     #1.
    file_open1 = open('bd.txt', 'r')                                                                        #1.
    with open('bd.txt', 'r') as file_open1:                                                                 #1.
        if user_id in file_open1.read():                                                                    #1.
            bot.send_message(message.chat.id, "У вас есть доступ, напишите 'Привет'")                       #1.
            bot.register_next_step_handler(message, sta_rt)                                                 #1.
        else:                                                                                               #1.
            if message.text == 'Arsenich!bo1t@':                                                            #1.  ПРОВЕРКА НА, ТО ЕСТЬ ЛИ
                with open('bd.txt', 'a') as file_open1:                                                     #1.  ПОЛЬЗОВАТЕЛЬ В БАЗЕ ДАННЫХ.
                    file_open1.write(user_id + ' ')                                                         #1.  ЕСЛИ НЕТ, ТО ИДЁТ ЗАПРАШИВАНИЕ ПАРОЛЯ,
                bot.send_message(message.chat.id, "Теперь у вас есть доступ, напишите 'Привет'")            #1.  ПРИ ПРАВИЛЬНОМ ПАРОЛЕ ИДЁТ ДАЛЬНЕЙШИЕ
                bot.register_next_step_handler(message, sta_rt)                                             #1.  ДОБАВЛЕНИЕ ПОДЬЗОВАТЕЛЯ В БАЗУ ДАННЫХ.
            else:                                                                                           #1.
                bot.send_message(message.chat.id, "Введите пароль")                                         #1.
                bot.register_next_step_handler(message, bd)                                                 #1.
def sta_rt(message):
    if message.text.lower() == 'регистрация':                                                                                               #2.
        reg(message)                                                                                                                        #2.
    else:                                                                                                                                   #2.
        bot.send_message(message.from_user.id, "Привет, Кожаный! Если хочешь, чтобы я знал твоё имя, то пришли мне слово 'регистрация'")    #2.
        bot.register_next_step_handler(message, sta_rt)                                                                                     #2.  ПРОИСХОДИТ ЗАПОМИНАНИЕ БОТОМ
def reg(message):                                                                                                                           #2.  ИМЕНИ ПОЛЬЗОВАТЕЛЯ
    bot.send_message(message.from_user.id, 'Тут должна быть твоя регистрация, кожаный, напиши своё имя')                                    #2.
    bot.register_next_step_handler(message, get_name)                                                                                       #2.
def get_name(message):                                                                                                                      #2.
    global name                                                                                                                             #2.
    name = message.text                                                                                                                     #2.
    if message.text == name:                                                                                                                #2.
        bot.send_message(message.from_user.id, "Здравствуйте, " + name + ", если вам что-нибудь нужно, то просто напишите 'бот'")           #2.
        bot.register_next_step_handler(message, get_text_messages)                                                                          #3.   КОМАНДА 'БОТ', КОТОРАЯ
def get_text_messages(message):                                                                                                             #3.   ДАЁТ ЗАПРОС НА ВЫВЕДЕНИЕ КНОПОК
    if message.text.lower() == "бот":                                                                                                       #3.
        def _keyboard_(message):                                                                                                            #4.
            keyboard = types.InlineKeyboardMarkup()                                                                                         #4.
            key_budilnik_shtor = types.InlineKeyboardButton(text = 'Завести будильник', callback_data = 'budilnik_shtor')                   #4.
            keyboard.add(key_budilnik_shtor)                                                                                                #4.   ВЫВЕДЕНИЕ КНОПОК
            key_nastroyki = types.InlineKeyboardButton(text = 'Настройки', callback_data = 'nastroyki')                                     #4.
            keyboard.add(key_nastroyki)                                                                                                     #4.
            bot.send_message(message.from_user.id, text =  'Здравствуйте, ' + name + '. Вот список моих команд:', reply_markup = keyboard)  #4.
        _keyboard_(message)                                                                                                                 #4.
        @bot.callback_query_handler(func = lambda call: True)                                                                               #5.
        def callback_worker(call):                                                                                                          #5.
            if call.data == 'budilnik_shtor':                                                                                               #5.
                def _key_budilnik_shtor_(message):                                                                                          #5.
                    _keyboard_ = types.InlineKeyboardMarkup()                                                                               #5.
                    key_budilniki = types.InlineKeyboardButton(text = 'Все ваши будильники', callback_data = 'okno_budilnikov')             #5.   ВЫВЕДЕНИЕ КНОПОК ПРИ
                    _keyboard_.add(key_budilniki)                                                                                           #5.   НАЖАТИИ НА КНОПКУ 'Завести будильник'
                    key_plus_budilnik = types.InlineKeyboardButton(text = 'Добавить будильник', callback_data = 'plus_budilnik')            #5.
                    _keyboard_.add(key_plus_budilnik)                                                                                       #5.
                    bot.send_message(message.from_user.id, text = name + ', что вы хотите сделать из этого:', reply_markup = _keyboard_)    #5.
                _key_budilnik_shtor_(message)                                                                                               #5.
                @bot.callback_query_handler(func = lambda call: True)                                                                       #6.
                def callback_budilnik_shtor_(call):                                                                                         #6.
                    if call.data == 'okno_budilnikov':                                                                                      #6.1   ВЫВЕДЕНИЕ КНОПОК ПРИ
                        bot.send_message(message.chat.id, 'окно будильников')                                                               #6.1   НАЖАТИИ НА КНОПКУ 'Все ваши будильники'
                    if call.data == 'plus_budilnik':                                                                                        #6.2   ВЫВЕДЕНИЕ КНОПОК ПРИ
                        bot.send_message(message.chat.id, name + ' на какое время вы хотите добавить будильник?')                           #6.2   НАЖАТИИ НА КНОПКУ 'Добавить будильник'
                        _key_b_ = types.InlineKeyboardMarkup()                                                                              #6.2
                        key_first = types.InlineKeyboardButton(text = first, callback_data = 'first_budilnik')                              #6.2
                        _key_b_.add(key_first)                                                                                              #6.2
                        bot.send_message(message.from_user.id, text = name + ' на какое время вы хотите добавить будильник?', reply_markup = _key_b_)  #6.2
                        knopki_budilniki_(massage)                                                                                          #6.2
            if call.data == 'nastroyki':                                                                                                    #7.
                def _key_nastroyki_(message):                                                                                               #7.
                    _keyboard_ = types.InlineKeyboardMarkup()                                                                               #7.   ВЫВЕДЕНИЕ КНОПОК ПРИ
                    key_song = types.InlineKeyboardButton(text = 'Мелодия будильника', callback_data = 'song_budilnik')                     #7.   НАЖАТИИ НА КНОПКУ 'Настройки'
                    _keyboard_.add(key_song)                                                                                                #7.
                    key_len_song = types.InlineKeyboardButton(text = 'Длительность сигнала будильника', callback_data = 'len_song')         #7.
                    _keyboard_.add(key_len_song)                                                                                            #7.
                    bot.send_message(message.from_user.id, text = name + ', что вы хотите сделать из этого:', reply_markup = _keyboard_)    #7.
                _key_nastroyki_(message)                                                                                                    #7.
                @bot.callback_query_handler(func = lambda call: True)
                def callback_nastroyki_(call):
                    if call.data == 'song_budilnik':
                        bot.send_message(message.from_user.id, 'мелодия будильника')
                    if call.data == 'len_song':
                            bot.send_message(message.from_user.id, 'длительность мелодии')
    else:
        bot.register_next_step_handler(message, get_text_messages)                                                                          #8.   ПОСЛЕ ОКОНЧАНИИ ПРОГРАММЫ
#    if message.text == "/help":                                                                                                            #8.   ОНА ВОЗВРАЩАЕТ ВАС НА КОМАНДУ 'БОТ'
#        bot.send_message(message.from_user.id, "Напишите 'бот'")
 # elif message.text == "Сколько времени":
    #  bot.send_message(message.from_user.id, datetime.now().time())
  #elif message.text == "Какой день":
   #   bot.send_message(message.from_user.id, datetime.now().date())
#    else:
#        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop = True, interval = 0)