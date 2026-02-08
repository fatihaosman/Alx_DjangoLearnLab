
# Create your models here.
from django.db import models

# Create your models here.
"""
Author model:
- Represents a book author
- One author can have many books (one-to-many relationship)
"""

class Author(models.Model): # “This class should become a database table”
    name = models.CharField(max_length=255)  #This creates a column in the table

    def __str__(self):   #not reqyuired but it’s a good practice to have a string representation of the model--Author object (1)  withit we have --Chimamanda Ngozi Adichie

        return self.name
      
      
"""
Book model:
- Represents a book written by an author
- Each book belongs to one author
"""
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, #“Each book belongs to one Author”
        related_name='books', #allows us to: author.books.all()
        on_delete=models.CASCADE #“If an author is deleted, delete all their books too”
    )

    def __str__(self):
        return self.title   



