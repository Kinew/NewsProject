from django.contrib import admin
from .models import Category, Post, Author, News


def nullfy_quantity(modeladmin, request,
                    queryset):  # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(quantity=0)


nullfy_quantity.short_description = 'Обнулить товары'  # описание для более понятного представления в админ панеле задаётся, как будто это объект


# создаём новый класс для представления товаров в админке
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'on_stock', 'quantity')
    list_filter = ('post', 'quantity', 'name')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category__name')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullfy_quantity]  # добавляем действия в список


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(News)
# Register your models here.