from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Module(models.Model):
    order_number = models.IntegerField(verbose_name='Порядковый номер')
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['order_number']
