from Catalog.models import Categories

def get_subcategories_by_category(category):
    """
    Get Subcategories by category
    """
    subcategories = Categories.objects.all().filter(
        subcategory=category
    )
    return subcategories

