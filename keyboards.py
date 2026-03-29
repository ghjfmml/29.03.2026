import telebot
from telebot import types

def hru_keyboard():
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types	.InlineKeyboardButton(
			text = 'Камень',
			callback_data = 'ersh'
        ),
		types.InlineKeyboardButton(
			text = 'Ножницы',
			callback_data='no'
        ),
		types.InlineKeyboardButton(
			text = 'Бумага',
			callback_data='by'
        )
    )
	return keyboard