from Catalog.models import Categories, Styles, Furnitures

def get_categories():
    """
    Get Categories 
    """
    categories = Categories.objects.filter(
        subcategory=None
    )
    return categories

def get_subcategories_by_category(category):
    """
    Get Subcategories by category
    """
    subcategories = Categories.objects.all().filter(
        subcategory=category
    )
    return subcategories

def get_all_styles():
    """
    Get Styles
    """
    return Styles.objects.all()

def get_furniture_by_category_and_style(category, style):
    """
    Get Furnitures by category and style
    """
    furnitures = Furnitures.objects.filter(
        category=category,
        style=style
    )
    return furnitures