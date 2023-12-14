from Users.models import UserProfile


def authenticate(telegram_pk: str):
    user = UserProfile.objects.get(telegram_pk=telegram_pk)
    return user