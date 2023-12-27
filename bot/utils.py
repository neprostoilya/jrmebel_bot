from db import get_furnitures_by_category_and_style, get_gallery, \
    get_furniture

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
    
def get_text_to_manager(phone, full_name, furniture_pk, description, status):
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

Пользователь: @{full_name}

Описание заказа: {description}

Номер: *{phone}*

Статус заказа: *{status}*
    '''
    return text