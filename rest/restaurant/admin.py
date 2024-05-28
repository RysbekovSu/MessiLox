from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Table, Category, Food, CustomUser, Book, Order, OrderItem, Payment, OrderItemCook

admin.site.register(Table)
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(CustomUser)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItemCook)

admin.site.register(Payment)
