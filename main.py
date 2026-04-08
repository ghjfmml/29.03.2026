import telebot
import random
from telebot import types
from secrets import API_TOKEN
import keyboards

bot = telebot.TeleBot(API_TOKEN)

# Словарь для хранения статистики: {chat_id: {'wins': 0, 'losses': 0, 'draws': 0}}
user_stats = {}

def get_bot_choice():
    choices = ['камень', 'ножницы', 'бумага']
    bot_choice = random.choice(choices)
    return bot_choice


def update_stats(chat_id, result):
	"""Обновляет статистику пользователя"""
	if chat_id not in user_stats:
		user_stats[chat_id] = {'wins': 0, 'losses': 0, 'draws': 0}
	
	if result == "win":
		user_stats[chat_id]['wins'] += 1
	elif result == "loss":
		user_stats[chat_id]['losses'] += 1
	elif result == "draw":
		user_stats[chat_id]['draws'] += 1

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        text='Давай начнем, выбери камень, ножницы или бумагу',
        reply_markup=keyboards.hru_keyboard()
	)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(callback):
	bot.answer_callback_query(callback.id)
	chat_id = callback.message.chat.id

	# Обработка команды статистики
	if callback.data == 'stats':
		if chat_id not in user_stats:
			bot.send_message(chat_id, "У вас еще нет сыгранных партий.")
		else:
			stats = user_stats[chat_id]
			stats_text = f"📊 Ваша статистика:\n\n🏆 Побед: {stats['wins']}\n❌ Поражений: {stats['losses']}\n🔄 Ничьих: {stats['draws']}"
			bot.send_message(chat_id, stats_text, reply_markup=keyboards.menu_keyboard())
		return

	# Обработка команды обнуления статистики
	if callback.data == 'reset':
		if chat_id in user_stats:
			user_stats[chat_id] = {'wins': 0, 'losses': 0, 'draws': 0}
			bot.send_message(chat_id, "✅ Статистика обнулена!", reply_markup=keyboards.menu_keyboard())
		else:
			bot.send_message(chat_id, "Статистика уже пуста.", reply_markup=keyboards.menu_keyboard())
		return

	# Обработка игровых ходов
	if callback.data == 'ersh':
		user_choice = 'камень'
	elif callback.data == 'no':
		user_choice = 'ножницы'
	elif callback.data == 'by':
		user_choice = 'бумага'
	else:
		return
	
	bot_choice = get_bot_choice()
	result_text, result_type = determine_winner(user_choice, bot_choice)
	update_stats(chat_id, result_type)
	
	message_text = f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n{result_text}"
	bot.send_message(chat_id, message_text, reply_markup=keyboards.hru_keyboard())
		
def determine_winner(user_choice, bot_choice):
	"""Определяет победителя и возвращает (текст результата, тип результата)"""
	if user_choice == bot_choice:
		return "Ничья!", "draw"
	elif (user_choice == 'камень' and bot_choice == 'ножницы') or \
		 (user_choice == 'ножницы' and bot_choice == 'бумага') or \
		 (user_choice == 'бумага' and bot_choice == 'камень'):
		return "Вы выиграли!", "win"
	else:
		return "Вы проиграли!", "loss"

bot.infinity_polling()