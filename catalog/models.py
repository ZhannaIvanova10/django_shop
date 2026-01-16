from django.db import models


class Category(models.Model):
    """Модель категории товаров"""
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']
    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='Изображение',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='products'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения'
    )
    
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['-created_at']
    def __str__(self):
        return f'{self.name} ({self.price} руб.)'
