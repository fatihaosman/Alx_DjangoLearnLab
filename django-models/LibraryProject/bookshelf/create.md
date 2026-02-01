# create operation

```python
**comman used**
>>> from bookshelf.models import Book
>>> book = Book.objects.create(
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
... )
>>> book
**expected output**
<Book: 1984>



# python manage.py shell