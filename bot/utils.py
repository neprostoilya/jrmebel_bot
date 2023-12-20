from db import get_furnitures_by_category_and_style


def get_furnitures(category_id: int, style_id: int, pk: int):
    furnitures = get_furnitures_by_category_and_style(
        category=category_id,
        style=style_id
    )
    quantity_furnitures = len(furnitures)
    if pk <= quantity_furnitures - 1:
        furniture = furnitures[pk]
        text = f'''
Название: {furniture['title']}

Описание:
{furniture['description']} 

Категория: {furniture['get_category_title']} 
Стиль: {furniture['get_style_title']} 
    '''
        image = furniture['image']
        pk = pk + 1
        return image, pk, text, quantity_furnitures
    else:
        raise ValueError