from db import get_furnitures_by_category_and_style


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
        image = furniture['image']
        get_pk = furniture['pk']
        return image, pk, text, quantity_furnitures, get_pk
    else:
        raise ValueError
    
