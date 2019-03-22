from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, models.PROTECT, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=200, db_index=True)
    available = models.BooleanField(default=True, verbose_name='Доступен')
    stock = models.PositiveIntegerField(verbose_name='На складе')

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
          return reverse('shop:ProductDetail', args=[self.id, self.slug])