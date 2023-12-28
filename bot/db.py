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

def get_styles():
    """
    Get Styles Firnitures
    """
    data = get('catalog/get_styles/')
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

def create_order(user, furniture, description, status, completed):
    """
    Create Order
    """
    data = {'user': f'{user}', 'furniture': f'{furniture}', 'status': f'{status}',
        'description': f'{description}','completed': f'{completed}'}
        
    return post('order/create_order/', data)

def get_order(user, furniture_pk, description, status, completed):
    """
    Get Order
    """
    return get(f'order/get_order/{user}/{furniture_pk}/{description}/{status}/{completed}/')

def put_order(user, furniture, description, status, completed):
    """
    Put Order
    """
    data = {'user': f'{user}', 'furniture': f'{furniture}', 'status': f'{status}',
        'description': f'{description}','completed': f'{completed}'}
    return put(f'order/put_order/{user}/', data)

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

def get_furniture(furniture_pk: int):
    """
    Get furniture by pk
    """
    data = get(f'catalog/get_furniture/{furniture_pk}/')
    return data