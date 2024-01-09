from datetime import datetime
from datetime import date as date_from_datetime
from calendar import monthrange
from db import get_categories, get_subcategories_by_category, \
    get_styles

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

def phone_button_keyboard(btn) -> dict:
    """
    Phone button keyboard
    """
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text=f"📞{btn}", request_contact=True)]
        ], resize_keyboard=True
    )

def main_menu_keyboard(catalog, orders, settings) -> dict:
    """
    Main menu with buttons
    """
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text=f"🧾 {catalog}"),
             KeyboardButton(text=f"🛍️ {orders}"), 
             KeyboardButton(text=f"⚙️ {settings}")]
        ], resize_keyboard=True
    )

def back_to_main_menu_keyboard(back_btn) -> dict:
    """
    Back to main menu
    """
    return ReplyKeyboardMarkup([
        [KeyboardButton(text=f'↩ {back_btn}')]
    ], resize_keyboard=True)

def catalog_categories_keyboard(language) -> dict:
    """
    Catalog categories keyboard
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []
    categories = get_categories()
    for category in categories:
        bnt = InlineKeyboardButton(
            text=category[f'title_{language}'],
            callback_data=f"categories_{category['pk']}"
        )
        buttons.append(bnt)
    markup.add(*buttons)
    return markup

def catalog_subcategories_keyboard(language, back_btn, category_id: int) -> dict:
    """
    Catalog subcategories keyboard
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []
    subcategories = get_subcategories_by_category(category_id)
    for subcategory in subcategories:
        bnt = InlineKeyboardButton(
            text=subcategory[f'title_{language}'],
            callback_data=f"subcategory_{subcategory['pk']}"
        )
        buttons.append(bnt)
    markup.add(*buttons)
    markup.row(
    InlineKeyboardButton(text=f'⬅ {back_btn}', callback_data='back_to_categories')
    )
    return markup

def catalog_styles_keyboard(language, back_btn) -> dict:
    """
    Catalog styles keyboard
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []
    styles = get_styles()
    for style in styles:
        bnt = InlineKeyboardButton(
            text=style[f'title_{language}'],
            callback_data=f"style_{style['pk']}"
        )
        buttons.append(bnt)
    markup.add(*buttons)
    markup.row(
    InlineKeyboardButton(text=f'⬅ {back_btn}', callback_data='back_to_subcategories')
    )
    return markup

def catalog_furnitures_keyboard(create_order, pk: int, quantity_furnitures: int, get_pk_furniture: int) -> dict:
    """
    View and buy furnitures
    """
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton(text='⬅', callback_data='action_-'),
        InlineKeyboardButton(text=f'{pk + 1}/{quantity_furnitures}', callback_data=f'furnitures_{pk}'),
        InlineKeyboardButton(text='➡', callback_data='action_+'),
        InlineKeyboardButton(text=f'✅ {create_order}', callback_data=f'create_order_{get_pk_furniture}'),
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

def confirmation_order_keyboard(order_pk: int):
    """
    Buttons for group
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text='❎', callback_data=f'confirmation_rejected_order_{order_pk}'),
        InlineKeyboardButton(text='✅', callback_data=f'confirmation_accepted_order_{order_pk}'),
    ]
    markup.add(*buttons)
    return markup

def choose_language_keyboard():
    """
    Choose language keyboard
    """
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text='🇷🇺 Русский'),
            KeyboardButton(text="🇺🇿 O'zbekcha")]
        ], resize_keyboard=True
    )

def choose_month_keyboard():
    """
    Choose month keyboard
    """
    markup = InlineKeyboardMarkup(row_width=3)
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    buttons = []

    for i, month in enumerate(months, start=4):
        btn = InlineKeyboardButton(
            month, 
            callback_data=f'select_month_{i}'
        )
        buttons.append(btn)

    markup.add(*buttons)
    return markup

def choose_day_keyboard(month):
    """
    Choose day keyboard
    """
    year = datetime.now().year
    days_month = monthrange(year, month)[1]
    markup = InlineKeyboardMarkup(row_width=7)
    buttons = []
    num = 0
    name_days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

    for day in range(days_month):
        if num <= 6:
            if name_days[num] == 'Вс':
                btn = InlineKeyboardButton(
                    f'{name_days[num]} {day+1}', 
                    callback_data=f'ignore'
                )
            else:
                btn = InlineKeyboardButton(
                    f'{name_days[num]} {day+1}', 
                    callback_data=f'select_day_{name_days[num]}_{day+1}'
                )
            buttons.append(btn)
            num += 1
        else:
            num = 0
            btn = InlineKeyboardButton(
                f'{name_days[num]} {day+1}', 
                callback_data=f'select_day_{name_days[num]}_{day+1}'
            )
            buttons.append(btn)
            num += 1

    markup.add(*buttons)
    return markup

def choose_time_keyboard(times_list):
    """
    Choose time keyboard
    """
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []

    for time in times_list:
        btn = InlineKeyboardButton(
            time, 
            callback_data=f'select_time_{time}'
        )
        buttons.append(btn)

    markup.add(*buttons)
    return markup

