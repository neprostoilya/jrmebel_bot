import requests
import json

from config import URL, BOT_PK


def get(point: str):
    """
    Get
    """
    url = URL + point

    response = requests.get(url)
    response.raise_for_status()  

    if response.status_code != 204:
        data = response.json()
        return data

def post(point: str, data: json):
    """
    Post
    """
    url = URL + point

    try:
        response = requests.post(url, json=data)
        data = response.json()
        return data
    except:
        return None

def put(point: str, data: json):
    """
    PUT
    """
    url = URL + point

    try:
        response = requests.put(url, json=data)
        data = response.json()
        return data
    except:
        return None

def check_user(chat_id: str):
    """
    Check User
    """
    data = get('users/users')

    for _ in data:
        if _['telegram_pk'] == str(chat_id):
            return True
        
def register_user(username: str, phone: int, chat_id: int):
    """
    Register User
    """
    data = {'username': f'{username[0]}', 'phone': f'{phone}', \
        'telegram_pk': f'{chat_id}'}
    
    return post('users/register/', data)

def login_user(chat_id: int):
    """
    Login User
    """
    data = {'telegram_pk': f'{chat_id}'}

    return post('users/login/', data)

def get_categories():
    """
    Get Categories Firnitures
    """
    data = get('catalog/get_categories/')

    return data

def get_styles(category):
    """
    Get Styles Firnitures
    """
    data = get(f'catalog/get_styles/{category}')

    return data

def get_subcategories_by_category(category: str):
    """
    Get Subcategories Firnitures by category
    """
    data = get(f'catalog/get_subcategories/{category}/')

    return data

def get_furnitures_by_category_and_style(category, style):
    """
    Get Furnitures by Category and Style
    """
    data = get(f'catalog/get_furnitures/{category}/{style}/')

    return data

def create_order(user: int, furniture: int, description: str, status: str, datetime_order: str):
    """
    Create Order
    """
    fields = {'user': f'{user}', 'furniture': f'{furniture}', 'status': f'{status}',
        'description': f'{description}', 'datetime_order': f'{datetime_order}'}
    
    data = post('order/create_order/', fields)

    return data

def get_order(user, furniture_pk, description, status, datetime):
    """
    Get Order
    """
    data = get(f'order/get_order/{user}/{furniture_pk}/{description}/{status}/{datetime}')

    return data

def update_order(pk, user, status):
    """
    Put Order
    """
    fields = {'status': f'{status}', 'user': f'{user}'}

    data = put(f'order/update_order/{pk}/', fields)
    
    return data

def get_user(chat_id: str):
    """
    Get User
    """
    data = get('users/users')

    for _ in data:
        if _['telegram_pk'] == str(chat_id):
            return _['pk']

def get_gallery(furniture_pk: int):
    """
    Get Gallery by furniture pk
    """
    data = get(f'catalog/get_gallery/{furniture_pk}/')

    images_path = []

    for _ in data:
        images_path.append(_['image'])

    return images_path

def get_phone(chat_id: str):
    """
    Get phone
    """
    data = get('users/users')

    for _ in data:
        if _['telegram_pk'] == str(chat_id):
            return _['phone']

def get_orders_by_user(user):
    """
    Get Orders by User
    """
    data = get(f'order/get_orders/{user}/')

    return data

def get_chat_id_by_order(order):
    """
    Get chat_id by order
    """
    data = get(f'order/get_order_by_pk/{order}/')

    return get_chat_id_by_pk(data[0]['user'])

def get_chat_id_by_pk(pk: int):
    """
    Get User chat_id
    """
    data = get('users/users')

    for _ in data:
        if _['pk'] == pk:
            return _['telegram_pk']

def get_times(day):
    """
    Get times 
    """
    data = get(f'times/get_times/{day}')

    return data

def get_furniture(furniture_pk: int):
    """
    Get furniture by pk
    """
    data = get(f'catalog/get_furniture/{furniture_pk}/')

    return data

def get_order_by_pk(pk):
    """
    Get Order by pk
    """
    data = get(f'order/get_order_by_pk/{pk}/')

    return data

def get_order_by_datetime(datetime):
    """
    Get Order by time
    """
    try:
        get(f'order/get_order_by_datetime/{datetime}/')
    except:
        return False
    return True

