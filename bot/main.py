from config import TOKEN, ADMIN
from utills import check_user, login_user, register_user, get_categories, \
    get_furnitures_by_category_and_style, get_subcategories_by_category
from keyboards import phone_button_keyboard, main_menu_keyboard, \
    catalog_categories_keyboard, back_to_main_menu_keyboard, \
    catalog_subcategories_keyboard, back_to_categories_keyboard

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery

bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

def default_message(message: Message):
    """
    Default variables
    """
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    first_name = message.from_user.first_name
    username = message.from_user.username,
    message_id = message.message_id
    return chat_id, full_name, first_name, username, message_id

def default_call(call: CallbackQuery):
    """
    Default variables
    """
    chat_id = call.message.chat.id
    full_name = call.from_user.full_name
    first_name = call.from_user.first_name
    username = call.from_user.username,
    message_id = call.message.message_id
    return chat_id, full_name, first_name, username, message_id

@dp.message_handler(commands=['start', 'help', 'about']) 
async def commands(message: Message):
    """
    Reaction on commands
    """
    text = message.text
    match text:
        case '/start':
            await message.answer(
                f'Добро пожаловать <b>{message.from_user.first_name}</b>.'
            )    
            await message.answer(
                'Вас приветсвует Бот заказа Мебели.'
            )
            await register_and_login(message)
          
        case '/about':
            await message.answer(
                'Этот Бот Создан для заказа мебели...'
            )
        case '/help':
            await message.answer(
                'У вас вопросы пишите к <Manager>...'
            )

async def register_and_login(message: Message):
    """
    Login and Registration
    """
    chat_id, _, _, _, _ = default_message(message)
    user = check_user(chat_id=chat_id)
    if user:
        login_user(chat_id)
        await message.answer('Авторизация прошла успешно!')
        await main_menu(message)
    else:
        await message.answer(
            text='Для регистрации вы должны отправить нам контакт.',
            reply_markup=phone_button_keyboard()
        )

@dp.message_handler(content_types=['contact']) 
async def finish_register(message: Message):
    """
    Registration User
    """
    chat_id, _, _, username, _ = default_message(message)
    phone = message.contact.phone_number
    register_user(username, phone, chat_id)
    await message.answer('Регистрация прошла успешно!')
    await main_menu(message)

async def main_menu(message: Message):
    """
    Main Menu
    """
    await message.answer(
        text='Выберите направление:',
        reply_markup=main_menu_keyboard()
    )

@dp.message_handler(lambda message: '🧾 Каталог' in message.text)
async def catalog_categories_list(message: Message):
    """
    Reaction on button
    """
    chat_id = message.chat.id
    await bot.send_message(
        chat_id, 
        text='Погнали', 
        reply_markup=back_to_main_menu_keyboard()
    )
    await message.answer(
        text='Выберите категорию: ', 
        reply_markup=catalog_categories_keyboard()
    )

@dp.message_handler(lambda message: 'Главное меню' in message.text)
async def back_to_main(message: Message):
    """
    Reaction on back button 
    """
    chat_id, _, _, _, message_id = default_message(message)
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id - 1
    )
    await main_menu(message)

@dp.callback_query_handler(lambda call: 'category_' in call.data)
async def catalog_subcategories_list(call: CallbackQuery):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    category_id = int(call.data.split('_')[-1])
    await bot.edit_message_text(
        text='Выберите подкатегорию:',
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=catalog_subcategories_keyboard(category_id)
    )

@dp.callback_query_handler(lambda call: 'Назад' in call.data)
async def back_to_categories(call: CallbackQuery):
    """
    Back to categories list
    """
    chat_id, _, _, _, message_id = default_call(call)
    await bot.edit_message_text(
        text="Выберите категорию: ",
        chat_id=chat_id, 
        message_id=message_id,
        reply_markup=catalog_categories_keyboard()
    )


executor.start_polling(dp)