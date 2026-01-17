##  the crud opearions i performed 

PS C:\Users\HP 1030 G4\Desktop\Introduction_to_Django\Introduction_to_Django\LibraryProject> python manage.py shell
>> 
13 objects imported automatically (use -v 2 for details).

Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
>>> book = Book.objects.create(
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
... )
>>> book
<Book: 1984>
>>>
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>
>>>
>>> book = Book.objects.get(title="1984")
>>> book.title
'1984'
>>> book.author
'George Orwell'
>>> book.publication_year
1949
>>>
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>>
>>> book.title
'Nineteen Eighty-Four'
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four>]>
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
>>>
>>>  