from db import get_furnitures_by_category_and_style


def get_text_furnitures(category_id: int, style_id: int, furniture: int):
    """
    Text for furniture
    """
    furnitures = get_furnitures_by_category_and_style(
        category=category_id,
        style=style_id
    )
    furniture += 1
    for _ in furnitures:
        __text = f'''
Название: {_['title']}

Описание:
{_['description']} 

Категория: {_['get_category_title']} 
Стиль: {_['get_style_title']} 
        '''
        __image = _['image']
        __pk = _['pk']
    
    return __image, __pk, __text, furniture