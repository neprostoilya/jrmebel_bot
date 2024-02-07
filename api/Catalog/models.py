from django.db import models
from django.utils.safestring import mark_safe

from Users.models import UserProfile


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
    without_style = models.BooleanField(
        verbose_name='Без стиля'
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
    category = models.ForeignKey(
        Categories, 
        on_delete=models.CASCADE, 
        verbose_name='Категория',
    )
    
    def __str__(self):
        return self.title_ru
    
    def __repr__(self):
        return f'Style: pk={self.pk}, title_ru={self.title_ru}, title_uz={self.title_uz}, category={self.category}'
    
    class Meta:
        verbose_name = 'Стиль Категории Мебели'
        verbose_name_plural = 'Стили Категорий Мебель'

class Furnitures(models.Model):
    """
    Furnitures
    """
    image = models.ImageField(
        verbose_name='Фото'
    )
    title_ru = models.CharField(
        max_length=155,
        verbose_name='Название мебели на русском'
    )
    title_uz = models.CharField(
        max_length=155,
        verbose_name='Название мебели на узбекском'
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
        related_name='style',
        null=True,
        blank=True,
    )
    price = models.CharField(
        verbose_name='Цена'
    )

    def __str__(self):
        return self.title_ru
    
    def __repr__(self):
        return f'Furniture: pk={self.pk}, image={self.image}, title_ru={self.title_ru}, title_uz={self.title_uz},  \
        description_ru={self.description_ru}, description_uz={self.description_uz}, category={self.category}, style={self.style}, price={self.price}'
    
    def descriptiontrim(self):
        return u"%s..." % (self.description_ru[:15],)
    
    descriptiontrim.allow_tags = True
    descriptiontrim.short_description = 'Описание'

    def img_preview(self): 
        if self.image.url:
            return mark_safe(f'<img src="{self.image.url}" width="75px" height="75px"/>')
        
    img_preview.allow_tags = True
    img_preview.short_description = 'Миниатюра'

    def get_category_title_ru(self):
        return self.category.title_ru

    def get_category_title_uz(self):
        return self.category.title_uz

    def get_style_title_ru(self):
        if self.style:
            return self.style.title_ru

    def get_style_title_uz(self):
        if self.style:
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



