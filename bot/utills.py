import requests

from config import URL

def get_users():
    """
    Get Users
    """
    url = URL + 'users/users'
    response = requests.get(url)
    data = response.json()
    return data