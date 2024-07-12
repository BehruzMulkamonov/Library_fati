from django.contrib import admin

from .models import Book, Discuss, Magazine


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Discuss)
class DiscussAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
