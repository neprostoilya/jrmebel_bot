from config import TOKEN, ADMIN
from utills import check_user, login_user, register_user
from keyboards import phone_button_keyboard, main_menu_keyboard

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery

bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

def default(message: Message):
    """
    Default variables
    """
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    first_name = message.from_user.first_name
    username = message.from_user.username
    return chat_id, full_name, first_name, username

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
    chat_id, _, _, _ = default(message)
    user = check_user(chat_id=chat_id)
    print(user)
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
    chat_id, _, _, username = default(message)
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

executor.start_polling(dp)