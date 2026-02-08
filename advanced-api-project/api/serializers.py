from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

"""
BookSerializer:
- Serializes all fields of the Book model
- Includes custom validation to prevent future publication years
"""
class BookSerializer(serializers.ModelSerializer): #“Serializes all fields of the Book model” : modelserialzer- “DRF, please auto-generate fields from the model”

    class Meta: #“Meta class is where we specify which model to serialize and which fields to include”
        model = Book # tells DRF “This serializer is for the Book model”
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
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    
#     books
# ➡️ Name comes from related_name='books'
# BookSerializer
# ➡️ Use the book serializer inside the author serializer

# many=True
# ➡️ One author → many books

# read_only=True
# ➡️ You can:
# View books ✔️
# Not create books through author

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']






# TESTING

# python manage.py shell

# from api.models import Author, Book
# from api.serializers import AuthorSerializer

# author = Author.objects.create(name="Chimamanda Ngozi Adichie")
# Book.objects.create(title="Half of a Yellow Sun", publication_year=2006, author=author)

# serializer = AuthorSerializer(author)
# print(serializer.data)
