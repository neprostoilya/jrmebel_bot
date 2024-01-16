from django.db import models


choices = (
    ('Monday', 'Понедельник'),
    ('Tuesday', 'Вторник'),
    ('Wednesday', 'Среда'),
    ('Thursday', 'Четверг'),
    ('Friday', 'Пятница'),
    ('Saturday', 'Суббота'),
)

class Times(models.Model):
    """
    Model times
    """
    time = models.CharField(
        verbose_name='Время'
    )
    day = models.CharField(
        choices=choices,
        verbose_name='День'
    )

    def __str__(self) -> str:
        return self.time
    
    def __repr__(self) -> str:
        return f'Times: time={self.time}, day={self.day}'

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'