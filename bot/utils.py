from db import get_furnitures_by_category_and_style


def get_furnitures(category_id: int, style_id: int, pk: int):
    """
    Text for furniture
    """
    furnitures = get_furnitures_by_category_and_style(
        category=category_id,
        style=style_id
    )
    for _ in furnitures[pk]:
        text = f'''
Название: {_['title']}

Описание:
{_['description']} 

Категория: {_['get_category_title']} 
Стиль: {_['get_style_title']} 
        '''
        image = _['image']
        pk = _['pk']
    get_furniture = pk + 1
    quantity_furnitures = len(furnitures)
    return image, pk, text, get_furniture, quantity_furnitures