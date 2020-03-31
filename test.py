import telebot
import datetime
from time import monotonic



bot = telebot.TeleBot('1089871348:AAHc4mtSCdmU3cLXMRPzBcwhYWyMehAkK7o')


def grafik_degurstv(message):
    t = monotonic()
    t_h = monotonic()
    count = 5
    count_house = 5
    x = 0
    while x == 0:
        if datetime.datetime.today() >= datetime.datetime(2020, 3, 2, 10, 0,0):
            count = 0
            while x == 0:
                if monotonic() - t > 1 and count == 0:
                    t = monotonic()
                    bot.send_message(message.chat.id, 'Сегодня плиту моет Лёха.')
                    count = 1
                elif monotonic() - t > 1 and count == 1:
                    t = monotonic()
                    bot.send_message(message.chat.id, 'Сегодня плиту моет Дима.')
                    count = 2
                elif monotonic() - t > 1 and count == 2:
                    t = monotonic()
                    bot.send_message(message.chat.id, 'Сегодня плиту моет Бодя.')
                    count = 3
                elif monotonic() - t > 1 and count == 3:
                    t = monotonic()
                    bot.send_message(message.chat.id, 'Сегодня плиту моет Стёпа.')
                    count = 4
                elif monotonic() - t > 1 and count == 4:
                    t = monotonic()
                    bot.send_message(message.chat.id, 'Сегодня плиту моет Саша.')
                    count = 0

                elif datetime.datetime.today() >= datetime.datetime(2020, 3, 4, 10, 0,0):
                    bot.send_message(message.chat.id, 'Завтра квартиру убирает Дима.')
                    count_house = 0
                    x = 1

    while True:
        if monotonic() - t_h > 3 and count_house == 0:
            t_h = monotonic()
            bot.send_message(message.chat.id, 'Завтра квартиру убирает Дима.')
            count_house = 1
        elif monotonic() - t_h > 3 and count_house == 1:
            t_h = monotonic()
            bot.send_message(message.chat.id, 'Завтра квартиру убирает Бодя.')
            count_house = 2
        elif monotonic() - t_h > 3 and count_house == 2:
            t_h = monotonic()
            bot.send_message(message.chat.id, 'Завтра квартиру убирает Стёпа.')
            count_house = 3
        elif monotonic() - t_h > 3 and count_house == 3:
            t_h = monotonic()
            bot.send_message(message.chat.id, 'Завтра квартиру убирает Саша.')
            count_house = 4
        elif monotonic() - t_h > 3 and count_house == 4:
            t_h = monotonic()
            bot.send_message(message.chat.id, 'Завтра квартиру убирает Лёха.')
            count_house = 0
        elif monotonic() - t > 1 and count == 0:
            t = monotonic()
            bot.send_message(message.chat.id, 'Сегодня плиту моет Дима.')
            count = 1
        elif monotonic() - t > 1 and count == 1:
            t = monotonic()
            bot.send_message(message.chat.id, 'Сегодня плиту моет Бодя.')
            count = 2
        elif monotonic() - t > 1 and count == 2:
            t = monotonic()
            bot.send_message(message.chat.id, 'Сегодня плиту моет Стёпа.')
            count = 3
        elif monotonic() - t > 1 and count == 3:
            t = monotonic()
            bot.send_message(message.chat.id, 'Сегодня плиту моет Саша.')
            count = 4
        elif monotonic() - t > 1 and count == 4:
            t = monotonic()
            bot.send_message(message.chat.id, 'Сегодня плиту моет Лёха.')
            count = 0


@bot.message_handler(commands=['start'])
def get_text_meesages(message):
    grafik_degurstv(message)

bot.polling(none_stop=True, interval=0)