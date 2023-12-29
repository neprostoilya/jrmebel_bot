from db import get_furnitures_by_category_and_style, get_gallery, \
    get_furniture, put_order, get_order, get_user

def get_furnitures(category_id: int, style_id: int, pk: int):
    furnitures = get_furnitures_by_category_and_style(
        category=category_id,
        style=style_id
    )
    quantity_furnitures = len(furnitures)
    if pk <= quantity_furnitures - 1 and pk >= 0:
        furniture = furnitures[pk]
        text = f'''
Название: {furniture['title']}

Описание:
{furniture['description']}                                                                                 

Категория: {furniture['get_category_title']} 
Стиль: {furniture['get_style_title']} 
    '''
        get_pk = furniture['pk']
        images_path = []
        images_path += get_gallery(get_pk)
        images_path.append(furniture['image'])
        return images_path, pk, text, quantity_furnitures, get_pk
    else:
        raise ValueError
    
def get_text_to_manager(phone, username, furniture_pk, description, status):
    """
    Get text to manager
    """
    furniture = get_furniture(
        furniture_pk=furniture_pk
    )
    title = furniture[0]['title']
    description_furniture = furniture[0]['description']
    category = furniture[0]['get_category_title']
    style = furniture[0]['get_style_title']

    text = f'''
Название мебели: *{title}*

Описание мебели: {description_furniture}

Категория мебели: *{category}*
Стиль мебели: *{style}*

Пользователь: @{username[0]}

Описание заказа: {description}

Номер: *{phone}*

Статус заказа: *{status}*
    '''
    return text

def get_text_order(order):
    """
    Text for order
    """
    text = f'''
    Название мебели: *{order['get_title_furniture']}*

    Описание мебели: 
    {order['get_description_furniture']}

    Категория: *{order['get_category_furniture']}*

    Стиль: *{order['get_style_furniture']}*

    Описание заказа: {order['description']}

    Статус: *{order['status']}*

    Выполнен: *{'Да' if order['completed'] else 'Нет'}*
    '''
    return text

# def put_order_user(chat_id, order):
#     """
#     Put order
#     """
    