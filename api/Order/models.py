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
    description = models.TextField(
        verbose_name='Описание',
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

    def __str__(self):
        return self.user.username
    
    def __repr__(self):
        return f'Order: pk={self.pk}, user={self.user}, furniture={self.furniture}, description={self.description}'
           

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    