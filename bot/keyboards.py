from utills import get_categories, get_subcategories_by_category

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

def phone_button_keyboard() -> dict:
    """
    Phone button keyboard
    """
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="📞 Отправить контакт", request_contact=True)]
        ], resize_keyboard=True
    )

def main_menu_keyboard() -> dict:
    """
    Main menu with buttons
    """
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text='🧾 Каталог'),
             KeyboardButton(text='🛍️ Заказы'), 
             KeyboardButton(text='⚙️ Настройки')]
        ], resize_keyboard=True
    )

def back_to_main_menu_keyboard() -> dict:
    """
    Back to main menu
    """
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='Главное меню')]
    ], resize_keyboard=True)

def back_to_categories_keyboard() -> dict:
    """ Кнопка возвращения назад. """
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='⬅ Назад')]
    ], resize_keyboard=True)

def catalog_categories_keyboard() -> dict:
    """
    Catalog categories keyboard
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []
    categories = get_categories()
    for category in categories:
        bnt = InlineKeyboardButton(
            text=category['title'],
            callback_data=f"category_{category['pk']}"
        )
        buttons.append(bnt)
    markup.add(*buttons)
    return markup

def catalog_subcategories_keyboard(category_id: int) -> dict:
    """
    Catalog subcategories keyboard
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []
    subcategories = get_subcategories_by_category(category_id)
    for subcategory in subcategories:
        bnt = InlineKeyboardButton(
            text=subcategory['title'],
            callback_data=f"subcategory_{subcategory['pk']}"
        )
        buttons.append(bnt)
    markup.add(*buttons)
    markup.row(
    InlineKeyboardButton(text='⬅ Назад', callback_data='Назад')
    )
    return markup