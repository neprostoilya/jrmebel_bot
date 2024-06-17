def text_for_furniture(furniture):
    styles_info = f"\nСтиль: *{furniture['get_style_title']}*\n" if furniture['get_style_title'] else ''
    return f'''
Название: *{furniture['title']}*

Описание:
__{furniture['description']}__                                                                            

Категория: *{furniture['get_category_title']}*
{styles_info}
Цена: *{furniture['price']}* 
    '''


def text_order(order):
    styles_info = f"\nСтиль: *{order['get_style_furniture']}\n*" if order['get_style_furniture'] else ''
    return f'''
Название мебели: *{order['get_title_furniture']}*

Описание мебели: 
{order['get_description_furniture']}

Категория: *{order['get_category_furniture']}*
{styles_info}
Описание заказа: {order['description']}
Статус: *{order['status']}*
Забронированая дата: *{order['datetime_order']}*
    '''

def get_months_list():
    """
    Get months list by language
    """
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    return months

def get_days_list():
    """
    Get days list by language
    """
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    return days
