from db import get_categories, get_subcategories_by_category, \
    get_styles

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
        [KeyboardButton(text='↩ Главное меню')]
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
            callback_data=f"categories_{category['pk']}"
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
    InlineKeyboardButton(text='⬅ Назад', callback_data='back_to_categories')
    )
    return markup

def catalog_styles_keyboard() -> dict:
    """
    Catalog styles keyboard
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []
    styles = get_styles()
    for style in styles:
        bnt = InlineKeyboardButton(
            text=style['title'],
            callback_data=f"style_{style['pk']}"
        )
        buttons.append(bnt)
    markup.add(*buttons)
    markup.row(
    InlineKeyboardButton(text='⬅ Назад', callback_data='back_to_subcategories')
    )
    return markup

def catalog_furnitures_keyboard(pk: int, quantity_furnitures: int, get_pk_furniture: int) -> dict:
    """
    View and buy furnitures
    """
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton(text='⬅', callback_data='action_-'),
        InlineKeyboardButton(text=f'{pk + 1}/{quantity_furnitures}', callback_data=f'furnitures_{pk}'),
        InlineKeyboardButton(text='➡', callback_data='action_+'),
        InlineKeyboardButton(text='✅ Заказать', callback_data=f'create_order_{get_pk_furniture}'),
    ]
    markup.add(*buttons)
    return markup

def confirmation_keyboard(furniture: int):
    """
    Confirmation
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text='❎', callback_data='confirmation_rejected_'),
        InlineKeyboardButton(text='✅', callback_data=f'confirmation_confirmed_{furniture}'),
    ]
    markup.add(*buttons)
    return markup

def confirmation_order_keyboard():
    """
    Buttons for group
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text='❎', callback_data='confirmation_rejected_order_'),
        InlineKeyboardButton(text='✅', callback_data='confirmation_confirmed_order_'),
    ]
    markup.add(*buttons)
    return markup