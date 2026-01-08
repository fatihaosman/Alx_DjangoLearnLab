from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality for these fields
    search_fields = ('title', 'author')
    
    # Optional: add filters by year
    list_filter = ('publication_year',)

# Register Book with the customized admin
admin.site.register(Book, BookAdmin)
