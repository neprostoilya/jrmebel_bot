from django.db import models
from django.utils.safestring import mark_safe

from Users.models import UserProfile
from Catalog.models import Furnitures

class Orders(models.Model):
    """
    Order of user
    """
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Заказчик',
    )
    furniture = models.ForeignKey(
        Furnitures,
        on_delete=models.CASCADE,
        verbose_name='Мебель',
        related_name='furnitures',
        blank=True,
        null=True
    )
    size = models.CharField(
        verbose_name='Размер',
        blank=True,
        null=True
    )
    material = models.CharField(
        verbose_name='Материал',
        blank=True,
        null=True
    )
    color = models.CharField(
        verbose_name='Цвет',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='orders/', 
        verbose_name='Фото',
        blank=True,
        null=True
    )
    status = models.CharField(
        verbose_name='Статус'
    )
    completed = models.BooleanField(
        verbose_name='Выполнен'
    )

    def descriptiontrim(self):
        return u"%s..." % (self.description[:100],)
    
    descriptiontrim.allow_tags = True
    descriptiontrim.short_description = 'Описание'

    def img_preview(self): 
            return mark_safe(f'<img src="{self.image.url}" width="75px" height="75px"/>')
    
    img_preview.allow_tags = True
    img_preview.short_description = 'Миниатюра'

    def __str__(self):
        return self.user.username
    
    def __repr__(self):
        return f'Order: pk={self.pk}, user={self.user}, furniture={self.furniture}, \
            size={self.size}, color={self.color}, image={self.image}, \
            description={self.description}, material={self.material}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    