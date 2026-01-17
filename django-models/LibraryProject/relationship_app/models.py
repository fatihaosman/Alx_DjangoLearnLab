from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title


# Library model
class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


# Librarian model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name  
      
      
      
# 🔗 1. ForeignKey (Author → Book)
# author = models.ForeignKey(Author, ...)


# ✔ One author can write many books
# ✔ One book belongs to one author


# 🔗 2. ManyToMany (Library ↔ Book)
# books = models.ManyToManyField(Book)


# ✔ A library has many books
# ✔ A book can be in many libraries



# 3. OneToOne (Library ↔ Librarian)
# library = models.OneToOneField(Library, ...)


# ✔ One library has one librarian
# ✔ One librarian manages one library