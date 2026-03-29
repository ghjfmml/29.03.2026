import telebot
import random
from telebot import types
from secrets import API_TOKEN
import keyboards

bot = telebot.TeleBot(API_TOKEN)

def get_bot_choice():
    choices = ['камень', 'ножницы', 'бумага']
    bot_choice = random.choice(choices)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    bot.send_message(
        message.chat.id,
        text='Давай начнем, выбери камень ножницы или бумагу',
        reply_markup=keyboards.hru_keyboard()
	)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(callback):
	# bot.answer_callback_query(callback.id)

	if callback.data == 'ersh':
		user_choice = 'камень'
	elif callback.data == 'no':
		user_choice = 'ножницы'
	elif callback.data == 'pap':
		user_choice = 'бумага'
		
def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and bot_choice == 'ножницы') or \
         (user_choice == 'ножницы' and bot_choice == 'бумага') or \
         (user_choice == 'бумага' and bot_choice == 'камень'):
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"

bot.infinity_polling()