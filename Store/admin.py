from django.contrib import admin
from .models import Product, Category, Tag, ProductTag

# Register your models here.
class ProductInline(admin.TabularInline):
    model = Product
    readonly_fields = ('name', 'description', 'price', 'category') 

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

class ProductTagInline(admin.TabularInline):
    model = ProductTag
    

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductTagInline]
    search_fields = ('name',)
    list_display = ('name', 'price')
    list_filter = ('tag',)

    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)

