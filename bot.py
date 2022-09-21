from ast import parse
import telebot
from telebot import types
from random import choice
from datetime import datetime
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    text = f'привет, <b>{message.from_user.first_name}</b>'
    stk = open('static/negr.tgs', 'rb')
    bot.send_message(message.chat.id, text, parse_mode='html')
    bot.send_sticker(message.chat.id, stk)
    
    


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('понедельник')
    button2 = types.KeyboardButton('вторник')
    button3 = types.KeyboardButton('среда')
    button4 = types.KeyboardButton('четверг')
    button5 = types.KeyboardButton('пятница')
    button6 = types.KeyboardButton('суббота')
    button7 = types.KeyboardButton('Автор🦠')
    button8 = types.KeyboardButton('список📄')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
    # bot.send_message(message.chat.id, text, reply_markup = markup)
    


@bot.message_handler(content_types=['text'])
def lalalalala(message):
    
    if message.text == 'понедельник':
        text =  '''
    8:00		----------
9:00		----------
10:00		----------
11:20	Кыргызский язык    116.k
12:20	Русский язык       
13:20	Русский язык       108А.k
14:20	----------	
15:20	----------	
            '''
        bot.send_message(message.chat.id, text)
    elif message.text == 'вторник':
        text = '''
8:00	----------	
9:00	Химия      106
10:00	Химия      106
11:20	Граждановедение   205
12:20	Французский язык / Корейский язык                                                                                                                                	
13:20	Французский язык / Корейский язык    
14:20	Математика      116
15:20	----------
            '''
        bot.send_message(message.chat.id, text)
    elif message.text == 'среда':
        text = '''
8:00	Физика     104
9:00	Физика     104
10:00	Начальная военная подготовка    113
11:20	География        116
12:20	Эдвайзерский час	107
13:20	Математика    116
14:20	----------
15:20	----------	
            '''         
        bot.send_message(message.chat.id, text)
    elif message.text == 'четверг':
        text = '''
8:00	----------	
9:00	Истроия КР  108
10:00	Начальная военная подготовка  108
11:20	Французский язык / Корейский язык 
12:20	Французский язык / Корейский язык                                                                                                                              	
13:20	Кыргызская Литратура  114 
14:20	Кыргызская Литратура  114 
15:20	----------
            '''
        bot.send_message(message.chat.id, text)
    elif message.text == 'пятница':
        text = '''
8:00    Англиский язык
9:00	Англиский язык
10:00	Биология 115
11:20	Математика   115
12:20	Математика  115
13:20	----------
14:20	Физическая культура
15:20	Физическая культура	
            ''' 
        bot.send_message(message.chat.id, text)

        bot.send_message(message.chat.id, text)
    elif message.text == 'суббота':
        text = '''
8:00    Кыргызский язык  116
9:00	Физика    104
10:00	Всеобщая история  201
11:20	Основы критическое мышления 108
12:20	Основы критическое мышления 108
13:20	Математика   115
14:20	----------
15:20	----------	
            ''' 
        bot.send_message(message.chat.id, text)

    elif message.text == 'Автор🦠':
            foto = open('static/foto.jpg', 'rb')
            bot.send_photo(message.chat.id, foto)
            text = 'Гапаров Байэл'
            bot.send_message(message.chat.id, text)
    elif message.text == 'список📄':
        text = '''
    1. Абдиганиев Бекзат 
    2. Абдукаимов Аман 
    3. Абдусаттаров Маруфф 
    4. Асанбаев Самат 
    5. Базарбаев Назар 
    6. Беделбаев Умар 
    7. Бейшенбеков Марсель 
    8. Алекова Мээрим
    9. Эгембердиев Рустам
    10. Гапаров Байел 
    11. Камилов Карыбек 
    12. Камчыбеков Эрбол  
    13. Кубанычбек уулу Куткелди
    15. Мурзабаев Руслан
    16. Мырзакулов Даниел
    17. Нурканов Айтенир
    18. Раимбердиев Азатбек
    19. Райымбеков Кыдырсейит
    20. Сабыров Байсалбек 
    21. Узакбаев Даниель
            ''' 
        bot.send_message(message.chat.id, text)
            

bot.polling(non_stop=True)