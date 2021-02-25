from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Candle(models.Model):
    title = models.CharField(max_length=255)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subtitle = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name='candles')

class ProductImage(models.Model):
    candle = models.ForeignKey(Candle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/')

