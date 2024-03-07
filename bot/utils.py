from db import get_furnitures_by_category_and_style, get_gallery, \
    get_furniture, get_furnitures_by_category
from template import text_for_furniture, text_order

def get_furnitures(without_style: bool, language: str, category_id: int, style_id: int, pk: int):
    """
    Get furniture by category_id, style_id, pk
    """
    if not without_style:
        furnitures = get_furnitures_by_category_and_style(
            category=category_id,
            style=style_id
        )
    else:
        furnitures = get_furnitures_by_category(
            category=category_id
        )
        
    quantity_furnitures = len(furnitures)

    if pk <= quantity_furnitures -1 and pk >= 0:
        furniture = furnitures[pk]

        text = text_for_furniture(language, furniture)

        get_pk = furniture['pk']

        images_path = []
        images_path.append(furniture['image'])
        images_path += get_gallery(get_pk)
        return images_path, pk, text, quantity_furnitures, get_pk
    else:
        raise ValueError
    
def get_text_to_manager(phone, username, furniture_pk, description, status, datetime_order):
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

    text = get_text_for_manager(
        title=title,
        description_furniture=description_furniture,
        category=category,
        style=style,
        price=price,
        phone=phone,
        username=username,
        description=description,
        status=status, 
        datetime_order=datetime_order
    )

    return text

def get_text_to_manager_for_call(phone, username, furniture_pk, description):
    """
    Text to manager for call
    """
    furniture = get_furniture(
        furniture_pk=furniture_pk
    )
    
    title = furniture[0]['title_ru']
    description_furniture = furniture[0]['description_ru']
    category = furniture[0]['get_category_title_ru']
    style = furniture[0]['get_style_title_ru']
    price = furniture[0]['price']

    text = get_text_for_call(
        title, 
        description_furniture, 
        category, 
        style, 
        price, 
        username, 
        description, 
        phone
    )

    return text

def get_text_order(language, order):
    """
    Text for order
    """
    text = text_order(language, order)
    return text

def get_text_for_call(title, description_furniture, category, style, price, username, description, phone):
    """
    Get text for call
    """
    styles_info = f"\nСтиль: <b>{style}</b>\n" if style else ''
    return f'''
Пользователь заказал звонок.
    
Пользователь: @{username[0]}

Номер: <b>{phone}</b>

Описание: {description}

Название мебели: <b>{title}</b>

Описание мебели: 
{description_furniture}

Категория мебели: <b>{category}</b>
{styles_info}
Цена: <b>{price}</b>
    '''

def get_text_for_manager(title, description_furniture, category, style, price, username, description, phone, status, datetime_order):
    """
    Get text for furniture
    """
    styles_info = f"\Стиль: <b>{style}</b>\n" if style else ''
    return f'''
Название мебели: <b>{title}</b>

Описание мебели: 
{description_furniture}

Категория мебели: <b>{category}</b>
{styles_info}
Цена: <b>{price} сумм</b>

Пользователь: @{username[0]}

Описание заказа: {description}

Номер: <b>{phone}</b>

Статус заказа: <b>{status}</b>

Забронированая дата: <b>{datetime_order}</b>
    '''