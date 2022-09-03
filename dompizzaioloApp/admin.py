from django.contrib import admin
from dompizzaioloApp.models import User, Food, Order

# Register your models here.


class Users(admin.ModelAdmin):
    list_display = ('id', 'name_user', 'email', 'user_permission')
    list_display_links = ('id', 'name_user', 'email')
    search_fields = ('id', 'name_user')
    list_per_page: 30


admin.site.register(User, Users)


class Foods(admin.ModelAdmin):
    list_display = ('id', 'name_food', 'price_food')
    list_display_links = ('id', 'name_food')
    search_fields = ('id', 'name_food', 'price_food')
    list_per_page: 30


admin.site.register(Food, Foods)


class Orders(admin.ModelAdmin):
    list_display = ('id', 'name_user', 'name_food', 'status')
    list_display_links = ('id', 'name_user', 'name_food')
    search_fields = ('id', 'name_user', 'name_food' 'status')
    list_per_page: 30


admin.site.register(Order, Orders)
