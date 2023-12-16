from utills import get_categories, get_subcategories_by_category, \
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

def catalog_furnitures_keyboard(quantity_furnitures: int, furniture: int) -> dict:
    """
    View and buy furnitures
    """
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton(text='⬅', callback_data='action_-'),
        InlineKeyboardButton(text=f'{furniture}/{quantity_furnitures}', callback_data=f'{furniture}'),
        InlineKeyboardButton(text='➡', callback_data='action_+'),
        InlineKeyboardButton(text='✅ Заказать', callback_data='create_order'),
        InlineKeyboardButton(text='↩ Главное меню', callback_data='back_to_main_menu')
    ]
    markup.add(*buttons)
    return markup
