import pyowm
import telebot
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ua'

owm = pyowm.OWM('f76d58801c6c3cc69b0e7340a2e55600', config_dict)
bot = telebot.TeleBot('1829573524:AAFWGsvwh3JqRcpowD9eUwH8Jm9nvluridU')

mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    
    answer = "В місті " + message.text + " зараз " + w.detailed_status + "\n"
    answer += "Температура зааз в районі " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Зараз дуже холодно. Вдягайся неймовірно добре!"
    elif temp < 20:
        answer += "Зараз холодно. Вдягайся тепліше!"
    else:
        answer += "Температура нормальна. Вдягайся, як завгодно."
    
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop = True)
