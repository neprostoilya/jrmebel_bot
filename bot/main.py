from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, ReplyKeyboardRemove

from utils import  get_furnitures, get_text_order, get_text_to_manager, get_text_to_manager_for_call
from config import MANAGER, TOKEN
from template import get_days_list, get_months_list
from db import *
from keyboards import *


storage = MemoryStorage()

class CreateOrder(StatesGroup):
    description = State()
    month = State()
    day = State()
    time = State()

class CallToManager(StatesGroup):
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

@dp.message_handler(commands=['start', 'help', 'about'], state='*') 
async def commands(message: Message, state: FSMContext):
    """
    Reaction on commands
    """
    text = message.text
    await state.finish()
    
    match text:
        case '/start':
            await register_and_login(message, state)
        case '/about':
            await message.answer(
                'Этот Бот Создан для заказа мебели...',
                parse_mode='Markdown'
            )
        case '/help':
            await message.answer(
                'У вас вопросы пишите к <Manager>...',
                parse_mode='Markdown'
            )


async def register_and_login(message: CallbackQuery, state: FSMContext):
    """
    Login and Registration
    """
    chat_id, _, _, _, _ = default_message(message)
    data = await state.get_data()

    user = check_user(chat_id=chat_id)

    if user:
        login_user(chat_id)

        await message.answer(
            text='Авторизация прошла успешно!',
        )

        await main_menu(message, state)
    else:
        await message.answer(
            text='Для регистрации пожалуйста оставьте контакт.',
            reply_markup=phone_button_keyboard('Отправить контакт')
        )

@dp.message_handler(content_types=['contact'], state='*') 
async def finish_register(message: Message, state: FSMContext):
    """
    Registration User
    """
    chat_id, _, _, username, message_id = default_message(message)
    data = await state.get_data()

    phone = message.contact.phone_number
    register_user(username, phone, chat_id)

    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id-1
    )

    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )

    await message.answer(
        text='Регистрация прошла успешно!',
    )

    await main_menu(message, state)

async def main_menu(message: Message, state: FSMContext):
    """
    Main Menu
    """
    chat_id, _, _, _, _ = default_message(message)
    data = await state.get_data()
    
    await bot.send_message(
        chat_id=chat_id,
        text='Выберите направление:',
        reply_markup=main_menu_keyboard('Каталог', 'Заказы',  'Контакты')
    )

async def main_menu_call(call: CallbackQuery, state: FSMContext):
    """
    Main Menu
    """
    chat_id, _, _, _, _ = default_call(call)
    data = await state.get_data()

    await bot.send_message(
        chat_id=chat_id,
        text=main_menu,
        reply_markup=main_menu_keyboard('Каталог', 'Заказы',  'Контакты')
    )

@dp.message_handler(lambda message: 'Каталог' in message.text, state='*')
async def catalog_categories_list(message: Message, state: FSMContext):
    """
    Reaction on button
    """
    chat_id, _, _, _, _ = default_message(message)
    data = await state.get_data()

    await bot.send_message(
        chat_id,
        text='*Каталог*',
        reply_markup=back_to_main_menu_keyboard('Назад'),
        parse_mode='Markdown'
    )

    await bot.send_message(
        chat_id, 
        text='Выберите категорию:',
        reply_markup=catalog_categories_keyboard()
    )

@dp.callback_query_handler(lambda call: 'categories_' in call.data)
async def catalog_subcategories_list(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data()

    category_id = int(call.data.split('_')[-1])

    await state.update_data(
        category_id=category_id
    ) 

    await bot.edit_message_text(
        chat_id=chat_id,
        text='Выберите подкатегорию:',
        message_id=message_id,
        reply_markup=catalog_subcategories_keyboard('Назад', category_id)
    )

@dp.callback_query_handler(lambda call: 'subcategory_' in call.data)
async def catalog_styles_list(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data()

    subcategory_id = int(call.data.split('_')[-2])
    without_style = call.data.split('_')[-1]

    await state.update_data(
        subcategory_id=subcategory_id
    ) 
    
    if without_style == 'False':
        styles = get_styles(subcategory_id)
        await bot.edit_message_text(
            chat_id=chat_id,
            text='Выберите стиль:',
            message_id=message_id,
            reply_markup=catalog_styles_keyboard(styles, 'Назад', subcategory_id)
        )
    else:
        await state.update_data(
            pk=0,
            style_id=None,
            without_style=without_style
        ) 

        images_path, pk, text, quantity_furnitures, get_pk = get_furnitures(
            without_style=without_style,
            style_id=None,
            category_id=subcategory_id,
            pk=0
        )
        
        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )

        count = 0
        media = MediaGroup()

        for path in images_path:
            media.attach_photo(
                photo=InputFile(f'/api/api{path}'),   
                caption='Фото'
            )
            count += 1

        await state.update_data(count=count) 

        await bot.send_media_group(
            chat_id=chat_id,
            media=media
        )
        
        await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=catalog_furnitures_keyboard('Звонок от менеджера', 'Заказать замер', pk, quantity_furnitures, get_pk),
            parse_mode='Markdown'
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

    await state.update_data(
        pk=0,
        style_id=style_id,
    ) 

    images_path, pk, text, quantity_furnitures, get_pk = get_furnitures(
        category_id=category_id,
        style_id=style_id,
        without_style=None,
        pk=0
    )
    
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )

    count = 0
    media = MediaGroup()

    for path in images_path:
        media.attach_photo(
            photo=InputFile(f'/api/api{path}'),   
            caption='Фото'
        )
        count += 1

    await state.update_data(count=count) 

    await bot.send_media_group(
        chat_id=chat_id,
        media=media
    )
    
    await bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=catalog_furnitures_keyboard('Звонок от менеджера', 'Заказать замер', pk, quantity_furnitures, get_pk),
        parse_mode='Markdown'
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
    without_style = data.get('without_style')
    pk = data.get('pk') + 1

    await state.update_data(
        pk=pk,
        style_id=style_id,
        without_style=without_style
    ) 

    images_path, _, text, quantity_furnitures, get_pk = get_furnitures(
        category_id=category_id,
        style_id=style_id,
        without_style=without_style,
        pk=pk
    )
    get_count = data.get('count')

    for _ in range(get_count+1):
        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id-_
        )

    count = 0
    media = MediaGroup()

    for path in images_path:
        media.attach_photo(
            photo=InputFile(f'/api/api{path}'), 
            caption='Фото'
        )
        count += 1

    await state.update_data(
        count=count
    ) 

    await bot.send_media_group(
        chat_id=chat_id,
        media=media
    )

    await bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=catalog_furnitures_keyboard('Звонок от менеджера', 'Заказать замер', pk, quantity_furnitures, get_pk),
        parse_mode='Markdown'
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
    without_style = data.get('without_style')
    pk = data.get('pk') - 1

    await state.update_data(
        pk=pk,
        style_id=style_id,
        without_style=without_style
    ) 

    images_path, _, text, quantity_furnitures, get_pk = get_furnitures(
        category_id=category_id,
        style_id=style_id,
        without_style=without_style,
        pk=pk
    )
    get_count = data.get('count')

    for _ in range(get_count+1):
        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id-_
        )

    count = 0
    media = MediaGroup()

    for path in images_path:
        media.attach_photo(
            photo=InputFile(f'/api/api{path}'), 
            caption='Фото'
        )
        count += 1

    await state.update_data(
        count=count
    ) 

    await bot.send_media_group(
        chat_id=chat_id,
        media=media
    )

    await bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=catalog_furnitures_keyboard('Звонок от менеджера', 'Заказать замер', pk, quantity_furnitures, get_pk),
        parse_mode='Markdown'
    )

@dp.callback_query_handler(lambda call: 'back_to_categories' in call.data)
async def back_to_categories(call: CallbackQuery, state: FSMContext):
    """
    Back to categories list
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data() 

    await bot.edit_message_text(
        text='Выберите категорию:',
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
        text='Выберите подкатегорию:',
        chat_id=chat_id, 
        message_id=message_id,
        reply_markup=catalog_subcategories_keyboard('Назад', category_id)
    )

@dp.callback_query_handler(lambda call: 'back_to_main_menu' in call.data)
async def back_to_main(call: CallbackQuery, state: FSMContext):
    """
    Reaction on back button 
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data()

    count = data.get('count')
    
    if count:
        for _ in range(count+1):
            await bot.delete_message(
                chat_id=chat_id,
                message_id=message_id-_
            )
    else:
        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )

        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id - 1
        )
        
    await main_menu_call(call, state)

@dp.callback_query_handler(lambda call: 'call_to_manager_' in call.data)
async def call_to_manager(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data() 

    furniture = int(call.data.split('_')[-1])
    num = data.get('count')

    for _ in range(num+1):
        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id - _
        )   

    
    await bot.send_message(
        chat_id=chat_id,
        text='Опишите, что Вас интересует.',
        reply_markup=back_to_main_menu_keyboard('Главное меню')
    )
    
    async with state.proxy() as data:
        data['furniture_pk'] = furniture

    await CallToManager.description.set()

@dp.message_handler(content_types=['text'], state=CallToManager.description)
async def get_description_for_call(message: Message, state: FSMContext):
    """
    Reaction on description
    """
    chat_id, _, _, username, message_id = default_message(message)
    data = await state.get_data() 

    if 'Главное меню' in message.text:
        await main_menu(message, state)
    else:
        phone = get_phone(chat_id)  
        description = message.text
        furniture_pk = data['furniture_pk']

        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id - 1
        )

        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )

        await bot.send_message(
            chat_id=chat_id,
            text='Заявка успешно отправлена, ожидайте звонка.'
        )

        await bot.send_message(
            chat_id=MANAGER,
            text=get_text_to_manager_for_call(phone, username, furniture_pk, description),
            parse_mode='HTML'
        )

        await state.finish()

        await main_menu(message, state)

@dp.message_handler(lambda message: 'Главное меню'  in message.text, state='*')
async def back_to_main(message: Message, state: FSMContext):
    """
    Reaction on back button 
    """
    chat_id, _, _, _, message_id = default_message(message)
    data = await state.get_data()

    count = data.get('count')
    await main_menu(message, state)


@dp.message_handler(lambda message: '↩ Назад'  in message.text, state='*')
async def back_to_main(message: Message, state: FSMContext):
    """
    Reaction on back button 
    """
    await main_menu(message, state)

@dp.callback_query_handler(lambda call: 'create_order_' in call.data)
async def confirmation(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data() 

    furniture = int(call.data.split('_')[-1])
    num = data.get('count')

    for _ in range(num+1):
        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id - _
        )

    await bot.send_message(
        chat_id=chat_id,
        text='Для заказа отправьте описание заказа.',
        reply_markup=back_to_main_menu_keyboard('Главное меню')
    )
    
    async with state.proxy() as data:
        data['furniture_pk'] = furniture

    await CreateOrder.description.set()

@dp.message_handler(content_types=['text'], state=CreateOrder.description)
async def get_description_for_order(message: Message, state: FSMContext):
    """
    Reaction on description
    """
    chat_id, _, _, _, message_id = default_message(message)
    data = await state.get_data() 

    if 'Главное меню' in message.text in message.text:
        await main_menu(message, state)
    else:    
        description = message.text
        
        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id - 1
        )

        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )

        await bot.send_message(
            chat_id=chat_id, 
            text='Выберите дату для бронирования',
            reply_markup=back_to_main_menu_keyboard('Главное меню')
        )
        
        await bot.send_message(
            chat_id=chat_id,
            text='Выберите месяц:',
            reply_markup=choose_month_keyboard('Назад', get_months_list())
        )

        async with state.proxy() as data:
            data['description'] = description

        await CreateOrder.next()

@dp.callback_query_handler(lambda call: 'back_to_furniture' in call.data, state=CreateOrder.month)
async def back_to_furniture(call: CallbackQuery, state: FSMContext):
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data()


    category_id = data.get('subcategory_id')
    style_id = data.get('style_id')

    images_path, pk, text, quantity_furnitures, get_pk = get_furnitures(
        category_id=category_id,
        style_id=style_id,
        pk=0
    )
    
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )

    count = 0
    media = MediaGroup()

    for path in images_path:
        media.attach_photo(
            photo=InputFile(f'/api/api{path}'),   
            caption='Фото'
        )
        count += 1

    await bot.send_media_group(
        chat_id=chat_id,
        media=media
    )
    
    await bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=catalog_furnitures_keyboard('Звонок от менеджера', 'Заказать замер', pk, quantity_furnitures, get_pk),
        parse_mode='Markdown'
    )

    await state.finish()

    await state.update_data(
        count=count,
        pk=0,
        style_id=style_id
    )

@dp.callback_query_handler(lambda call: 'select_month_' in call.data, state=CreateOrder.month)
async def get_month_for_order(call: CallbackQuery, state: FSMContext):
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data() 

    month = int(call.data.split('_')[-1])

    await bot.edit_message_text(
        chat_id=chat_id, 
        message_id=message_id,
        text='Выберите день: Примечание в воскресение мы не работаем.',
        reply_markup=choose_day_keyboard(month, 'Назад', get_days_list())
    )

    async with state.proxy() as data:
        data['month'] = month

    await CreateOrder.next()

@dp.callback_query_handler(lambda call: 'select_month_back' in call.data, state=CreateOrder.day)
async def select_month_back(call: CallbackQuery, state: FSMContext):
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data()

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Выберите месяц:',
        reply_markup=choose_month_keyboard('Назад', get_months_list())
    )

    await CreateOrder.month.set()

@dp.callback_query_handler(lambda call: 'select_day_' in call.data, state=CreateOrder.day)
async def get_day_for_order(call: CallbackQuery, state: FSMContext):
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data() 

    day = int(call.data.split('_')[-1])
    month = int(call.data.split('_')[-2])
    year = int(call.data.split('_')[-3])

    await bot.edit_message_text(
        chat_id=chat_id, 
        message_id=message_id,
        text='Выберите время:',
        reply_markup=choose_time_keyboard(year, month, day, 'Назад')
    )

    async with state.proxy() as data:
        data['day'] = day
        data['year'] = year

    await CreateOrder.next()

@dp.callback_query_handler(lambda call: 'select_day_back' in call.data, state=CreateOrder.time)
async def select_day_back(call: CallbackQuery, state: FSMContext):
    chat_id, _, _, _, message_id = default_call(call)
    data = await state.get_data()

    month = data['month']
    
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Выберите день: Примечание в воскресение мы не работаем.',
        reply_markup=choose_day_keyboard(month, 'Назад', get_days_list())
    )

    await CreateOrder.day.set()

@dp.callback_query_handler(lambda call: 'select_time_' in call.data, state=CreateOrder.time)
async def get_time_for_order(call: CallbackQuery, state: FSMContext):
    chat_id, _, _, username, message_id = default_call(call)
    data = await state.get_data()

    user = get_user(chat_id)
    time = str(call.data.split('_')[-1])

    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )

    async with state.proxy() as data:
        furniture_pk = data['furniture_pk']
        description = data['description']
        year = data['year']
        month = data['month']
        day = data['day']
    
    datetime = f'{year}-{month}-{day}, {time}'

    create_order(
        user=user,
        furniture=furniture_pk,
        description=description,
        status='Ожидание принятия',
        datetime_order=datetime
    )

    text = send_message_to_manager(
        chat_id=chat_id, 
        username=username, 
        furniture_pk=furniture_pk, 
        description=description, 
        status='Ожидание принятия',
        datetime_order=datetime
    )

    order = get_order(
        user=user, 
        furniture_pk=furniture_pk, 
        description=description, 
        status='Ожидание принятия',
        datetime=datetime
    )
    
    await bot.send_message(
        chat_id=MANAGER,
        text=text,
        reply_markup=confirmation_order_keyboard(order[0]['pk']),
        parse_mode='HTML'
    )

    await bot.send_message(
        chat_id=chat_id,
        text='Ваше время замеров зарезервировано.  Ожидайте звонка менеджера, для уточнения деталей замера.'
    )

    await state.finish()

    await main_menu_call(call, state)

        
def send_message_to_manager(chat_id, username, furniture_pk, description, status, datetime_order):
    """
    Send message to manager group
    """
    if get_phone(chat_id):
        phone = get_phone(chat_id)
    else:
        phone = 'Без Номера'

    text = get_text_to_manager(
        phone=phone,
        username=username, 
        furniture_pk=furniture_pk, 
        description=description,
        status=status,
        datetime_order=datetime_order
    )
    return text
    
@dp.callback_query_handler(lambda call: 'confirmation_accepted_order_' in call.data)
async def confirmed_order(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    order = int(call.data.split('_')[-1])

    await state.update_data(
        order_pk=order
    )

    await state.update_data(
        status='принят'
    )

    await state.update_data(
        note='Через некоторое время к вам позвонит или напишет наш представитель.'
    )

    await bot.send_message(
        chat_id=MANAGER,
        text='Отправьте сообщение пользователю.'
    )
   
@dp.message_handler(content_types=['text'], chat_id=MANAGER)
async def send_message_order_accepted_to_user(message: Message, state: FSMContext):
    chat_id, _, _, _, message_id = default_message(message)
    data = await state.get_data()

    order_pk = data.get('order_pk')
    status = data.get('status')
    note = data.get('note')

    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )

    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id - 1
    )

    if order_pk:
        await bot.send_message(
            chat_id=MANAGER,
            text='Сообщение отправлено пользователю.'
        )

        chat_id = get_chat_id_by_order(order_pk)

        await bot.send_message(
            chat_id=chat_id,
            text=f'''
Ваш заказ был {status}!
        
Сообщение:
{message.text}

{note}
            '''
        )

        order = get_order_by_pk(order_pk)[0]

        update_order(
            order_pk, 
            order['user'], 
            status.capitalize(), 
            order['completed']
        )

        await state.update_data(
            confirmed_order_pk=None 
        )

@dp.message_handler(lambda message: 'Заказы'  in message.text or 'Buyurtmalar' in message.text, state='*')
async def user_orders(message: Message, state: FSMContext):
    """
    Reaction on button
    """
    chat_id, _, _, _, _ = default_message(message)
    data = await state.get_data() 

    await bot.send_message(
        chat_id=chat_id,
        text='Ваши последние заказы.', 
        reply_markup=back_to_main_menu_keyboard('Главное меню')
    )

    orders = get_orders_by_user(
        user=get_user(chat_id)
    )[::-1]

    for order in orders[:5]:
        await bot.send_message(
            chat_id=chat_id,
            text=get_text_order(order),
            parse_mode='Markdown'
        )
    
@dp.callback_query_handler(lambda call: 'confirmation_rejected_order_' in call.data)
async def confirmed_rejected_order(call: CallbackQuery, state: FSMContext):
    """
    Reaction on call button
    """
    order = int(call.data.split('_')[-1])

    await state.update_data(
        order_pk=order
    )

    await state.update_data(
        order_pk=order
    )

    await state.update_data(
        status='отказан'
    )
    
    await state.update_data(
        note='Статус вашего заказа изменен на отказ.'
    )

    await bot.send_message(
        chat_id=MANAGER,
        text='Отправьте причину отказа пользователю.'
    )

@dp.message_handler(lambda message: 'Контакты'  in message.text or 'Kontaktlar' in message.text, state='*')
async def about_the_bot(message: Message, state: FSMContext):
    """
    Reaction on button
    """
    chat_id, _, _, _, _ = default_message(message)
    data = await state.get_data() 

    await bot.send_message(
        chat_id=chat_id,
        text='''
Режим работы:  
ПН - ПТ: 9:00 - 18:00  
СБ: 9:00 - 14:00  
ВС: Выходной  

Менеджер: +998 (94) 080-33-99  
Наш адрес: г. Алмалык ул. Бабушкина 39''', 
    )
    
    latitude = 40.836576
    longitude = 69.620056
    
    await bot.send_location(chat_id, latitude, longitude)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)