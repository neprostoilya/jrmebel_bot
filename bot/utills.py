import requests
import json

from config import URL, BOT_PK

def get(point: str):
    """
    Get
    """
    url = URL + point
    response = requests.get(url)
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

def check_user(chat_id: int):
    """
    Check User
    """
    for _ in get('users/users'):
        if _['telegram_pk'] != chat_id:
            return True


def register_user(username: str, phone: int, chat_id: int):
    """
    Register User
    """
    data = {'username': f'{username}', 'phone': f'{phone}', \
        'telegram_pk': f'{chat_id}'}
    return post('users/register/', data)

def login_user(chat_id: int):
    """
    Login User
    """
    data = {'telegram_pk': f'{chat_id}'}
    return post('users/login/', data)