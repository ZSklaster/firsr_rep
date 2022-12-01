# Skillf_kurs_bot
import telebot as tb
from config import keys, TOKEN
from extensions import API_exeption, Skillf_mein

bot = tb.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: tb.types.Message):
    text = '''Чтобы начать работу введите команду боту в следующем формате: \n
     <название валюты> <в какую валюту перевести> <количество валюты>(все поля обязательные)
     чтобы увидеть все доступные валюты, наберите /values'''
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: tb.types.Message):
    text = 'доступные валюты'
    for key in keys:
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: tb.types.Message):
    try:

        val = message.text.split()
        if len(val) > 3:
            raise API_exeption('Cлишком много(мало) параметров')
        base, quote, amount = val

        total_base = Skillf_mein.get_price(base.lower(), quote.lower(), amount)
    except API_exeption as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'цена {amount} {base} в {quote} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
