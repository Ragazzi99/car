from django.contrib import admin
from . models import *

# Register your models here.
# class AppInfo(admin.ModelAdmin):
#     list_display = ['id', 'appname']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brand',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('model',)}
    list_display = ['id', 'typee', 'model', 'year', 'price', 'uploaded_at', 'updated_at']

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'car', 'amount']



admin.site.register(AppInfo)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact,)
admin.site.register(Customer,)
admin.site.register(Cart, CartAdmin)
admin.site.register(Payment)

