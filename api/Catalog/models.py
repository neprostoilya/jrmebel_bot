from django.db import models
from Users.models import UserProfile
from django.utils.safestring import mark_safe

class Categories(models.Model):
    """
    Categories Furniture
    """
    title = models.CharField(
        max_length=100,
        verbose_name='Название Категории'
    )
    subcategory = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Категория',
    )

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'Category: pk={self.pk}, category={self.title}, subcategory={self.subcategory}'
    
    class Meta:
        verbose_name = 'Категория Мебели'
        verbose_name_plural = 'Категории Мебели'
 
class Styles(models.Model):
    """
    Styles Furniture
    """
    title = models.CharField(
        max_length=100,
        verbose_name='Название Стиля'
    )

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'Style: pk={self.pk}, title={self.title}'
    
    class Meta:
        verbose_name = 'Стиль Категории Мебели'
        verbose_name_plural = 'Стили Категорий Мебель'

class Furnitures(models.Model):
    """
    Furnitures
    """
    title = models.CharField(
        max_length=155,
        verbose_name='Название Мебели'
    )
    image = models.ImageField(
        upload_to='furnitures/', 
        null=True, 
        blank=True, 
        verbose_name='Фото'
    )
    description = models.TextField(
        verbose_name='Описание'
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
        return self.title
    
    def __repr__(self):
        return f'Furniture: pk={self.pk}, title={self.title}, image={self.image}, \
        description={self.description}, category={self.category}, style={self.image}'
            
    
    def descriptiontrim(self):
        return u"%s..." % (self.description[:100],)
    
    descriptiontrim.allow_tags = True
    descriptiontrim.short_description = 'Описание'

    def img_preview(self): 
            return mark_safe(f'<img src="{self.image.url}" width="75px" height="75px"/>')
    
    img_preview.allow_tags = True
    img_preview.short_description = 'Миниатюра'

    def get_category_title(self):
        return self.category.title

    def get_style_title(self):
        return self.style.title

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



