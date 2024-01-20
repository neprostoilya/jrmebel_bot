import datetime
import calendar
from db import get_categories, get_order_by_datetime, get_subcategories_by_category, \
    get_styles, get_times

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

def catalog_furnitures_keyboard(call_to_manager: str, create_order: str, pk: int, quantity_furnitures: int, get_pk_furniture: int) -> dict:
    """
    View and buy furnitures
    """
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton(text='⬅', callback_data='action_-'),
        InlineKeyboardButton(text=f'{pk + 1}/{quantity_furnitures}', callback_data=f'furnitures_{pk}'),
        InlineKeyboardButton(text='➡', callback_data='action_+'),
        InlineKeyboardButton(text=f'✅ {create_order}', callback_data=f'create_order_{get_pk_furniture}'),
        InlineKeyboardButton(text=f'📞 {call_to_manager}', callback_data=f'call_to_manager_{get_pk_furniture}'),
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

def choose_month_keyboard(back: str, months: list):
    """
    Choose month keyboard
    """
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = []

    for i, month in enumerate(months, start=1):
        btn = InlineKeyboardButton(
            text=month, 
            callback_data=f'select_month_{i}'
        )
        buttons.append(btn)

    markup.add(*buttons)
    
    markup.row(
        InlineKeyboardButton(text=f"⬅️ {back}", callback_data="back_to_furniture")
    )
    return markup

def choose_day_keyboard(month: int, back: str, days: int):
    """
    Choose day keyboard
    """
    markup = InlineKeyboardMarkup(row_width=7)

    year = datetime.datetime.now().year

    markup.row(*[InlineKeyboardButton(days[i], callback_data="ignore") for i in range(7)])

    first_day = datetime.datetime(year=year, month=month, day=1)
    first_weekday = first_day.weekday()
    num_days = calendar.monthrange(year, month)[1]

    buttons = []

    if first_weekday > 0:
        for _ in range(first_weekday):
            btn = InlineKeyboardButton(text=" ", callback_data="ignore")
            buttons.append(btn)

    for day in range(1, num_days + 1):
        date = datetime.date(year=year, month=month, day=day)
        day_name = calendar.day_name[date.weekday()]

        if day_name == "Sunday":
            btn = InlineKeyboardButton(text="-", callback_data="ignore")
            buttons.append(btn)
        else:
            btn = InlineKeyboardButton(
                text=str(day), callback_data=f"select_day_{year}_{month}_{day}"
            )
            buttons.append(btn)

    while len(buttons) % 7 != 0:
        btn = InlineKeyboardButton(text=" ", callback_data="ignore")
        buttons.append(btn)

    markup.add(*buttons)

    markup.row(
        InlineKeyboardButton(text=f"⬅️ {back}", callback_data="select_month_back")
    )

    return markup

def choose_time_keyboard(year: int, month: int, day: int, back: str):
    """
    Choose time keyboard
    """
    markup = InlineKeyboardMarkup(row_width=2)
    
    date = datetime.date(
        year=year, 
        month=month, 
        day=day
    )

    day_name = calendar.day_name[date.weekday()]

    buttons = []

    times_list = get_times(str(day_name))


    for _ in times_list:
        time = _['time']

        btn = (
            InlineKeyboardButton(
                text=time, 
                callback_data=f'select_time_{time}'
            )
        )
        buttons.append(btn)

    markup.add(*buttons)

    markup.row(
        InlineKeyboardButton(
            text=f'⬅ {back}', 
            callback_data='select_day_back'
        )
    )

    return markup


