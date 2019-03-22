from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':  ('name',)}

class ProductAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Product._meta.fields]
    list_display = ['name', 'slug', 'price', 'stock', 'available',]
    list_filter = ['available',]
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)



