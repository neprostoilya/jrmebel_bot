from django.db import models
from Users.models import UserProfile
from django.utils.safestring import mark_safe

class Categories(models.Model):
    """
    Categories Furniture
    """
    title_ru = models.CharField(
        max_length=100,
        verbose_name='Название категории на русском'
    )
    title_uz = models.CharField(
        max_length=100,
        verbose_name='Название категории на узбекском'
    )
    subcategory = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Категория',
    )

    def __str__(self):
        return self.title_ru
    
    def __repr__(self):
        return f'Category: pk={self.pk}, title_ru={self.title_ru}, title_uz={self.title_uz}, subcategory={self.subcategory}'
    
    class Meta:
        verbose_name = 'Категория Мебели'
        verbose_name_plural = 'Категории Мебели'
 
class Styles(models.Model):
    """
    Styles Furniture
    """
    title_ru = models.CharField(
        max_length=100,
        verbose_name='Название cтиля категории на русском'
    )
    title_uz = models.CharField(
        max_length=100,
        verbose_name='Название cтиля категории на узбекском'
    )

    def __str__(self):
        return self.title_ru
    
    def __repr__(self):
        return f'Style: pk={self.pk}, title_ru={self.title_ru}, title_uz={self.title_uz}'
    
    class Meta:
        verbose_name = 'Стиль Категории Мебели'
        verbose_name_plural = 'Стили Категорий Мебель'

class Furnitures(models.Model):
    """
    Furnitures
    """
    title_ru = models.CharField(
        max_length=155,
        verbose_name='Название мебели на русском'
    )
    title_uz = models.CharField(
        max_length=155,
        verbose_name='Название мебели на узбекском'
    )
    image = models.ImageField(
        upload_to='furnitures/', 
        null=True, 
        blank=True, 
        verbose_name='Фото'
    )
    description_ru = models.TextField(
        verbose_name='Описание на русском'
    )
    description_uz = models.TextField(
        verbose_name='Описание на узбекском'
    )
    category = models.ForeignKey(
        Categories, 
        on_delete=models.CASCADE, 
        verbose_name='Категория',
        related_name='category'
    )
    style = models.ForeignKey(
        Styles, 
        on_delete=models.CASCADE, 
        verbose_name='Стиль',
        related_name='style'
    )
    price = models.FloatField(
        verbose_name='Цена'
    )

    def __str__(self):
        return self.title_ru
    
    def __repr__(self):
        return f'Furniture: pk={self.pk}, title_ru={self.title_ru}, title_uz={self.title_uz}, image={self.image}, \
        description_ru={self.description_ru}, description_uz={self.description_uz}, category={self.category}, style={self.style}'
    
    def descriptiontrim(self):
        return u"%s..." % (self.description_ru[:100],)
    
    descriptiontrim.allow_tags = True
    descriptiontrim.short_description = 'Описание'

    def img_preview(self): 
            return mark_safe(f'<img src="{self.image.url}" width="75px" height="75px"/>')
    
    img_preview.allow_tags = True
    img_preview.short_description = 'Миниатюра'

    def get_category_title_ru(self):
        return self.category.title_ru

    def get_category_title_uz(self):
        return self.category.title_uz

    def get_style_title_ru(self):
        return self.style.title_ru

    def get_style_title_uz(self):
        return self.style.title_uz

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'

class Gallery(models.Model):
    """
    Images for Furniture
    """
    image = models.ImageField(
        upload_to='furnitures/', 
        verbose_name='Фото'
    )
    furniture = models.ForeignKey(
        Furnitures, 
        on_delete=models.CASCADE, 
        related_name='images'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Галлерея'



