from django.contrib import admin

from .models import Category,Book,Comments

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["slug", "name"]
    list_filter = ['name','slug']
    search_fields = [list_display]

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment', 'likes']
    list_filter = ['comment', 'likes']
    search_fields = [list_display]
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name","author","status"]
    list_filter = ["name","author","status"]
    search_fields = [list_display]

