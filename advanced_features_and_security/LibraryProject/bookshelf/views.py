from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request):
    # code to view books
    return render(request, 'bookshelf/view_books.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # code to edit book
    return render(request, 'bookshelf/edit_book.html')

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# views.py
# LibraryProject/bookshelf/views.py
from django.shortcuts import render
from .models import Book
from .forms import ExampleForm

def book_list(request):
    form = ExampleForm(request.GET or None)
    books = Book.objects.all()
    
    if form.is_valid():
        search_term = form.cleaned_data.get('title')
        if search_term:
            # Safe ORM query to avoid SQL injection
            books = books.filter(title__icontains=search_term)
    
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

