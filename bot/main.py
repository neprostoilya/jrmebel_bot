import requests
from utils import get_furnitures
from config import TOKEN, URL
from db import check_user, create_order, get_user, login_user, register_user, get_categories, \
    get_furnitures_by_category_and_style, get_subcategories_by_category
from keyboards import confirmation_keyboard, phone_button_keyboard, main_menu_keyboard, \
    catalog_categories_keyboard, back_to_main_menu_keyboard, \
    catalog_subcategories_keyboard, catalog_styles_keyboard, \
    catalog_furnitures_keyboard

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile

storage = MemoryStorage()

class Create_order(StatesGroup):
    furniture = State()
    description = State()

bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

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

async def main_menu_call(call: CallbackQuery):
    """
    Main Menu
    """
    await bot.answer(
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

@dp.callback_query_handler(lambda call: 'categories_' in call.data)
async def catalog_subcategories_list(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    category_id = int(call.data.split('_')[-1])
    await state.update_data(category_id=category_id) 
    await bot.edit_message_text(
        text='Выберите подкатегорию:',
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=catalog_subcategories_keyboard(category_id)
    )

@dp.callback_query_handler(lambda call: 'subcategory_' in call.data)
async def catalog_styles_list(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    subcategory_id = int(call.data.split('_')[-1])
    await state.update_data(subcategory_id=subcategory_id) 
    await bot.edit_message_text(
        text='Выберите стиль:',
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=catalog_styles_keyboard()
    )

@dp.callback_query_handler(lambda call: 'style_' in call.data)
async def catalog_furnitures(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data() 
    category_id = data.get('subcategory_id')
    style_id = int(call.data.split('_')[-1])
    await state.update_data(style_id=style_id) 

    images_path, pk, text, quantity_furnitures, get_pk = get_furnitures(
        category_id=category_id,
        style_id=style_id,
        pk=0
    )
    
    await state.update_data(pk=0) 
    
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )

    # media = MediaGroup()
    # media.attach_photo(InputFile('media_bot/2023-12-19_21-07-19.png'), 'Превосходная фотография')
    # media.attach_photo(InputFile('media_bot/12_ayYtArI.jpg'), 'Превосходная фотография 2')
    # media.attach_photo(InputFile('media_bot/category_модульная спальня Леди.jpg'), 'Превосходная фотография 3')
    # media.attach_photo(InputFile('media_bot/category_модульная спальня Леди.jpg'), 'Превосходная фотография 3')
    # await bot.send_media_group(
    #     chat_id=chat_id,
    #     media=media
    # )

    

    await bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=catalog_furnitures_keyboard(pk, quantity_furnitures, get_pk)
    )

@dp.callback_query_handler(lambda call: 'action_+' in call.data)
async def catalog_action_plus(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data() 
    category_id = data.get('subcategory_id')
    style_id = data.get('style_id')
    pk = data.get('pk') + 1
    await state.update_data(pk=pk) 

    image, pk, text, quantity_furnitures, get_pk = get_furnitures(
        category_id=category_id,
        style_id=style_id,
        pk=pk
    )
    
    
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )

    response = requests.get(f'{URL}{image[1::]}/')
    if response.status_code == 200:
        with open("media/image.jpg", "wb") as file:
            file.write(response.content)
    
    with open("media/image.jpg", "rb") as photo:
        await bot.send_photo(
            chat_id=chat_id, 
            photo=photo, 
            caption=text, 
            reply_markup=catalog_furnitures_keyboard(pk, quantity_furnitures, get_pk)
        )

@dp.callback_query_handler(lambda call: 'action_-' in call.data)
async def catalog_action_minus(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data() 
    category_id = data.get('subcategory_id')
    style_id = data.get('style_id')
    pk = data.get('pk')-1
    await state.update_data(pk=pk) 

    image, pk, text, quantity_furnitures, get_pk = get_furnitures(
        category_id=category_id,
        style_id=style_id,
        pk=pk
    )
    
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )

    response = requests.get(f'{URL}{image[1::]}/')
    if response.status_code == 200:
        with open("media/image.jpg", "wb") as file:
            file.write(response.content)
    
    with open("media/image.jpg", "rb") as photo:
        await bot.send_photo(
            chat_id=chat_id, 
            photo=photo, 
            caption=text, 
            reply_markup=catalog_furnitures_keyboard(pk, quantity_furnitures, get_pk)
        )

@dp.callback_query_handler(lambda call: 'back_to_categories' in call.data)
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

@dp.callback_query_handler(lambda call: 'back_to_subcategories' in call.data)
async def back_to_subcategories(call: CallbackQuery, state: FSMContext):
    """
    Back to subcategories list
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data() 
    category_id = data.get('category_id')
    await bot.edit_message_text(
        text="Выберите подкатегорию: ",
        chat_id=chat_id, 
        message_id=message_id,
        reply_markup=catalog_subcategories_keyboard(category_id)
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

@dp.callback_query_handler(lambda call: 'confirmation_rejected' in call.data)
async def confirmation_rejected(call: CallbackQuery, state: FSMContext):
    """
    Back to main menu
    """
    await main_menu_call(call)
    
@dp.callback_query_handler(lambda call: 'create_order_' in call.data)
async def confirmation(call: CallbackQuery):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    furniture = int(call.data.split('_')[-1])

    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )
    await bot.send_message(
        chat_id=chat_id,
        text='Вы уверены что хотите заказать эту мебель?',
        reply_markup=confirmation_keyboard(furniture)
    )
    await Create_order.furniture.set()

@dp.callback_query_handler(lambda call: 'confirmation_confirmed_' in call.data, state=Create_order.furniture)
async def get_furniture_for_order(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    await bot.send_message(
        chat_id=chat_id,
        text='Для заказа отправьте описание заказа.'
    )
    async with state.proxy() as data:
        data['furniture'] = int(call.data.split('_')[-1])

    await Create_order.next()

@dp.message_handler(content_types=['text'], state=Create_order.description)
async def get_description_for_order(message: Message, state: FSMContext):
    """
    Reaction on description
    """
    chat_id = message.chat.id
    description = message.text
    
    await bot.send_message(
        chat_id=chat_id,
        text='Заказ создан, подождите некторое время пока мененджеры примут ваш заказ.'
    )
    async with state.proxy() as data:
        data['description'] = description
        furniture = int(data['furniture'])

    create_order(
        user=get_user(chat_id),
        furniture=furniture,
        description=description,
        status='Ожидание принятия заказа',
        completed=False
    )
    
    await state.finish()
    await main_menu(message)

executor.start_polling(dp)