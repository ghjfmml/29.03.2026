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
	keyboard.add(
		types.InlineKeyboardButton(
			text = '📊 Статистика',
			callback_data='stats'
		),
		types.InlineKeyboardButton(
			text = '🔄 Обнулить',
			callback_data='reset'
		)
	)
	return keyboard

def menu_keyboard():
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types.InlineKeyboardButton(
			text = '📊 Статистика',
			callback_data='stats'
		),
		types.InlineKeyboardButton(
			text = '🔄 Обнулить',
			callback_data='reset'
		)
	)
	return keyboard