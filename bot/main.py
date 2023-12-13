from config import TOKEN, ADMIN
from utills import get_users

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery

bot = Bot(TOKEN)
dp = Dispatcher(bot)

def default(message):
    """
    Default variables
    """
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    first_name = message.from_user.first_name
    return chat_id, full_name, first_name

@dp.message_handler(commands=['start', 'help', 'about']) 
async def commands(message: Message):
    """
    Reaction on commands
    """
    text = message.text
    match text:
        case '/start':
            await message.answer(
                f'Добро пожаловать <b>{message.from_user.first_name}</b>.\n \
                Вас приветствует Бот заказа мебели.'
            )    
            await register(message)
          
        case '/about':
            await message.answer(
                'Этот Бот Создан для заказа мебели...'
            )
        case '/help':
            await message.answer(
                'У вас вопросы пишите к <Manager>...'
            )

async def register(message: Message):
    """
    Authorization and Registration
    """
    chat_id, full_name, _ = default(message)
    print(get_users())
    # user = db_check_user(chat_id)
    # if user:
    #     await message.answer('Авторизация прошла успешно')
    #     await show_main_menu(message)
    # else:
    #     db_first_register_user(full_name=full_name, telegram_id=chat_id)

    #     await message.answer(
    #         text='Для регистрации нажмите на кнопку',
    #         reply_markup=generate_phone_button()
    #     )

executor.start_polling(dp)