from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

from django.contrib.auth import login


from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404



def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    
    
# log in view
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# log out view
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# register view
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")

    return render(request, "relationship_app/register.html", {"form": form})




# Role-check helpers
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Role-based views (ALX checker requires @user_passes_test and exact template paths)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")  # ✅ exact path

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")  # ✅ exact path

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")  # ✅ exact path



@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        from .models import Author, Book
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('list_books')  # you can create a list_books view
    from .models import Author
    authors = Author.objects.all()
    return render(request, "relationship_app/add_book.html", {"authors": authors})


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    from .models import Book
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        from .models import Author
        book.author = get_object_or_404(Author, id=author_id)
        book.save()
        return redirect('list_books')

    from .models import Author
    authors = Author.objects.all()
    return render(request, "relationship_app/edit_book.html", {"book": book, "authors": authors})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    from .models import Book
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, "relationship_app/delete_book.html", {"book": book})
