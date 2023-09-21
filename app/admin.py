from django.contrib import admin
from .models import *


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')
    list_display_links = ('firstname', 'lastname',)
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    list_display_links = ('title',)
    list_filter = ['publish_date']
    inlines = [ReviewInline]

admin.site.register(Book, BookAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating')
    list_display_links = ('user',)

admin.site.register(Review, ReviewAdmin)
