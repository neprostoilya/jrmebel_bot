translations = {
        "uz": {
            "succes_auth": "Avtorizatsiya muvaffaqiyatli o'tdi!",
            "registration_text": "Ro'yxatdan o'tish uchun iltimos aloqa ma'lumotlarini qoldiring.",
            "finished_register": "Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!",
            "main_menu": "Yo'nalishni tanlang:",
            "phone_btn_keyboard": "Kontakt yuborish",
            "catalog_btn_keyboard": "Katalog",
            "orders_btn_keyboard": "Buyurtmalar",
            "settings_btn_keyboard": "Sozlamalar",
            "back_to_main_menu_btn_keyboard": "Asosiy menyu",
            "lets_go": "Boshlaymiz",
            "choose_category": "Kategoriyani tanlang:",
            "choose_subcategory": "Podkategoriyani tanlang:",
            "choose_style": "Stilni tanlang:",
            "confirmation_order": "Ushbu mebelni buyurtma bermoqchimisiz?",
            "description_for_order": "Buyurtma berish uchun buyurtma haqida ma'lumot yuboring.",
            "success_create_order": "Buyurtma yaratildi, buyurtmani qabul qilish uchun bir oz vaqt kuting.",
            "last_orders": "Sizning oxirgi buyurtmalaringiz.",
            "create_order": "Buyurtma bermoq",
            "back": "Orqaga"
        },
        "ru": {
            "succes_auth": "Авторизация прошла успешно!",
            "registration_text": "Для регистрации пожалуйста оставьте контакт.",
            "finished_register": "Регистрация прошла успешно!",
            "main_menu": "Выберите направление:",
            "phone_btn_keyboard": "Отправить контакт",
            "catalog_btn_keyboard": "Каталог",
            "orders_btn_keyboard": "Заказы",
            "settings_btn_keyboard": "Настройки",
            "back_to_main_menu_btn_keyboard": "Главное меню",
            "lets_go": "Погнали",
            "choose_category": "Выберите категорию:",
            "choose_subcategory": "Выберите подкатегорию:",
            "choose_style": "Выберите стиль:",
            "confirmation_order": "Вы уверены что хотите заказать эту мебель?",
            "description_for_order": "Для заказа отправьте описание заказа.",
            "success_create_order": "Заказ создан, подождите некторое время пока мененджеры примут ваш заказ.",
            "last_orders": "Ваши последние заказы.",
            "create_order": "Заказать",
            "back": "Назад",
        }
    }

def text_for_furniture(language, furniture):
    if language == 'ru':
        return f'''
Название: *{furniture['title']}*

Описание:
__{furniture['description']}__                                                                            

Категория: *{furniture['get_category_title']}*

Стиль: *{furniture['get_style_title']}*

Цена: *{furniture['price']}* сумм
        '''
    else:
        return f'''
Nomi: *{furniture['title']}*

Tavsif:
{furniture['description']}

Kategoriya: *{furniture['get_category_title']}*

Stil: *{furniture['get_style_title']}*

Narx: *{furniture['price']}* so'm
        '''

def text_order(language, order):
    if language == 'ru':
        return f'''
Название мебели: *{order['get_title_furniture']}*

Описание мебели: 
{order['get_description_furniture']}

Категория: *{order['get_category_furniture']}*

Стиль: *{order['get_style_furniture']}*

Описание заказа: {order['description']}

Статус: *{order['status']}*

Выполнен: *{'Да' if order['completed'] else 'Нет'}*
        '''
    else: 
        return f'''
Nomi: *{order['get_title_furniture']}*

Mebel tavsifi:
{order['get_description_furniture']}

Kategoriya: *{order['get_category_furniture']}*

Stil: *{order['get_style_furniture']}*

Buyurtma tavsifi: {order['description']}

Holati: *{order['status']}*

Bajarildi: *{'Ha' if order['completed'] else "Yo'q"}*
        '''
