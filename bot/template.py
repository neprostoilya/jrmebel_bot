translations = {
        "uz": {
            "succes_auth": "Muafiyatli autentifikatsiya!",
            "registration_text": "Ro'yxatdan o'tish uchun iltimos aloqani qoldiring.",
            "finished_register": "Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!",
            "main_menu": "Keyingi harakatni tanlang:",
            "phone_btn_keyboard": "Kontaktni yuborish",
            "catalog_btn_keyboard": "Katalog",
            "orders_btn_keyboard": "Buyurtmalar",
            "settings_btn_keyboard": "Sozlamalar",
            "back_to_main_menu_btn_keyboard": "Bosh menyu",
            "choose_category": "Toifani tanlang:",
            "choose_subcategory": "Alohida toifani tanlang:",
            "choose_style": "Stilni tanlang:",
            "description_for_order": "Buyurtmangiz uchun ta'rifni yuboring.",
            "success_create_order": "Sizning vaqt o'lchash uchun rezervlangan.   O'lchashning tafsilotlarini aniqlash uchun menejer telefon qilishini kuting.",
            "last_orders": "Sizning oxirgi buyurtmalaringiz.",
            "create_order": "O'lchov buyurtirish",
            "back": "Orqaga",
            "create_order_btn_text": "O'lchovga buyurtma bering",
            "change_language": "Tilni tanlang:",
            "select_month": "Oy tanlang:",
            "select_day": "Kunni tanlang: E'tibor bering, biz yakshanba kuni ishlamaymiz.",
            "select_time": "Vaqtni tanlang:",
            "description_for_call": "Menejerga qo'ng'iroq qilish uchun qo'ng'iroq tavsifini o'zbek lotin tiliga yuboring",
            "success_send_message_for_call": "Ariza muvaffaqiyatli yuborildi, qo'ng'iroqni kuting.",
            "call_btn_text": "Qo'ng'iroq qiling"
        },
        "ru": {
            "succes_auth": "Авторизация прошла успешно!",
            "registration_text": "Для регистрации пожалуйста оставьте контакт.",
            "finished_register": "Регистрация прошла успешно!",
            "main_menu": "Выберите дальнейшее действие:",
            "phone_btn_keyboard": "Отправить контакт",
            "catalog_btn_keyboard": "Каталог",
            "orders_btn_keyboard": "Заказы",
            "settings_btn_keyboard": "Настройки",
            "back_to_main_menu_btn_keyboard": "Главное меню",
            "choose_category": "Выберите категорию:",
            "choose_subcategory": "Выберите подкатегорию:",
            "choose_style": "Выберите стиль:",
            "description_for_order": "Для заказа отправьте описание заказа.",
            "success_create_order": "Ваше время замеров зарезервировано.  Ожидайте звонка менеджера, для уточнения деталей замера.",
            "last_orders": "Ваши последние заказы.",
            "create_order_btn_text": "Заказать замер",
            "back": "Назад",
            "change_language": "Выберите язык:",
            "select_month": "Выберите месяц:",
            "select_day": "Выберите день: Примечание в воскресение мы не работаем.",
            "select_time": "Выберите время:",
            "description_for_call": "Для звонка менеджеру отправьте описание звонка",
            "success_send_message_for_call": "Заявка успешно отправлена, ожидайте звонка.",
            "call_btn_text": "Позвонить"
        }
    }

def text_for_furniture(language, furniture):
    if language == 'ru':
        return f'''
Название: *{furniture['title_ru']}*

Описание:
__{furniture['description_ru']}__                                                                            

Категория: *{furniture['get_category_title_ru']}*

Стиль: *{furniture['get_style_title_ru']}*

Цена: *{furniture['price']}* 
        '''
    else:
        return f'''
Nomi: *{furniture['title_uz']}*

Tavsif:
{furniture['description_uz']}

Kategoriya: *{furniture['get_category_title_uz']}*

Stil: *{furniture['get_style_title_uz']}*

Narx: *{furniture['price']}* 
        '''

def text_order(language, order):
    if language == 'ru':
        return f'''
Название мебели: *{order['get_title_furniture_ru']}*

Описание мебели: 
{order['get_description_furniture_ru']}

Категория: *{order['get_category_furniture_ru']}*

Стиль: *{order['get_style_furniture_ru']}*

Описание заказа: {order['description']}

Статус: *{order['status']}*

Забронированая дата: *{order['datetime_order']}*
        '''
    else: 
        return f'''
Nomi: *{order['get_title_furniture_ru']}*

Mebel tavsifi: 
{order['get_description_furniture_ru']}

Kategoriya: *{order['get_category_furniture_ru']}*

Usul: *{order['get_style_furniture_ru']}*

Buyurtma tavsifi: {order['description']}

Holat: *{order['status']}*

Bronlangan sanasi: *{order['datetime_order']}*
        '''

def get_months_list(language):
    """
    Get months list by language
    """
    if language == 'ru':
        months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    else:
        months = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr']
    return months

def get_days_list(language):
    """
    Get days list by language
    """
    if language == 'ru':
        days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    else:
        days = ['Dush', 'Sesh', 'Chor', 'Pay', 'Jum', 'Shan', 'Yak']
    return days



