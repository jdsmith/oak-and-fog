from django.contrib import admin
from .models import Category, Candle, ProductImage

class InlineImage(admin.TabularInline):
    model = ProductImage

class CandleAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

# Register your models here.
admin.site.register(Candle, CandleAdmin)
admin.site.register(Category)

