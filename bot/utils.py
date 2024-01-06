from db import get_furnitures_by_category_and_style, get_gallery, \
    get_furniture
from template import text_for_furniture, text_order

def get_furnitures(language, category_id: int, style_id: int, pk: int):
    furnitures = get_furnitures_by_category_and_style(
        category=category_id,
        style=style_id
    )
    quantity_furnitures = len(furnitures)
    if pk <= quantity_furnitures -1 and pk >= 0:
        furniture = furnitures[pk]
        text = text_for_furniture(language, furniture)
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
    title = furniture[0]['title_ru']
    description_furniture = furniture[0]['description_ru']
    category = furniture[0]['get_category_title_ru']
    style = furniture[0]['get_style_title_ru']
    price = furniture[0]['price']

    text = f'''
Название мебели: *{title}*

Описание мебели: 
{description_furniture}

Категория мебели: *{category}*

Стиль мебели: *{style}*

Цена: *{price} сумм*

Пользователь: @{username[0]}

Описание заказа: {description}

Номер: *{phone}*

Статус заказа: *{status}*
    '''
    return text

def get_text_order(language, order):
    """
    Text for order
    """
    text = text_order(language, order)
    return text

# def put_order_user(chat_id, order):
#     """
#     Put order
#     """
    