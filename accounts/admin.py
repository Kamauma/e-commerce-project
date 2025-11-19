from django.contrib import admin
# Register your models here.
from .models import Profile, Product

admin.site.register(Profile)
@admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    list_filter = ('category',)
    search_fields = ('name', 'description')

