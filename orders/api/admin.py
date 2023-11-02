from django.contrib import admin
from .models import User, Category, Shop, ProductInfo, Product, ProductParameter, OrderItem, Order, Contact

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('model', 'product', 'shop', 'quantity', 'price', 'price_rrc')

class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ('parameter', 'value')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_product_info_model', 'quantity', 'order')

    def get_product_info_model(self, obj):
        return obj.product_info.model
    get_product_info_model.short_description = 'Product Model'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dt', 'status')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'value')

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
admin.site.register(ProductParameter, ProductParameterAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Contact, ContactAdmin)
