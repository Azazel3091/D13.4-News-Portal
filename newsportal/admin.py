from django.contrib import admin
from .models import Post, Category


# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title', 'author', 'rating', 'categoryType',) # оставляем только имя и цену товара
    list_filter = ('author', 'postCategory', 'categoryType') # добавляем примитивные фильтры в нашу админку
    search_fields = ('title',) # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Post, PostAdmin)
admin.site.register(Category)