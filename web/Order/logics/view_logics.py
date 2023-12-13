from Order.models import Orders

def get_orders(user):
    """
    Get Orders User
    """
    orders = Orders.objects.filter(
        user=user
    )
    return orders