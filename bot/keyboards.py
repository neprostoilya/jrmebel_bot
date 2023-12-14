from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

def phone_button_keyboard() -> dict:
    """
    Phone button keyboard
    """
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="Отправить контакт", request_contact=True)]
        ], resize_keyboard=True
    )

def main_menu_keyboard() -> dict:
    """
    Main menu with buttons
    """
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text='Каталог'),
             KeyboardButton(text='Заказы'), 
             KeyboardButton(text='Настройки')]
        ], resize_keyboard=True
    )