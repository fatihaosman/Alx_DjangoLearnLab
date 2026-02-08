from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

"""
BookSerializer:
- Serializes all fields of the Book model
- Includes custom validation to prevent future publication years
"""
class BookSerializer(serializers.ModelSerializer): # “Serializers are like forms but for APIs, they convert complex data types to JSON and validate input data”
  # ModelSerializer → “DRF, please auto-generate fields from the model”

    class Meta:   #“Meta class is where we specify which model to serialize and which fields to include”
      #Meta is a configuration class--Django looks here for instructions
        model = Book  #“This serializer is for the Book model”
        fields = '__all__'  #“Include ALL model fields”

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


"""
AuthorSerializer:
- Serializes the author's name
- Includes a nested representation of related books
- Uses the related_name 'books' from the Book model
"""
class AuthorSerializer(serializers.ModelSerializer): #Name comes from related_name='books'
    books = BookSerializer(many=True, read_only=True) #Use the book serializer inside the author serializer
    
    # many=True
    # One author → many books
    
    #read_only=True
    #➡️ You can:
    # View books ✔️
    # Not create books through author ✔️
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']



# python manage.py shellp\Introduction_to_Django\advanced_api_pr
# >> ct>
# 14 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from api.models import Author, Book
# >>> from api.serializers import AuthorSerializer
# >>> 
# >>> author = Author.objects.create(name="Chimamanda Ngozi Adichie")
# >>> Book.objects.create(title="Half of a Yellow Sun", publication_year=2006, author=author)
# <Book: Half of a Yellow Sun>
# >>> 
# >>> serializer = AuthorSerializer(author)
# >>> print(serializer.data)
# {'id': 1, 'name': 'Chimamanda Ngozi Adichie', 'books': [{'id': 1, 'title': 'Half of a Yellow Sun', 'publication_year': 2006, 'author': 1}]}
# >>>