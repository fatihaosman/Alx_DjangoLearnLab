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
